# -*- coding: utf-8 -*-
"""ATTESTATION_LEDGER — la partie double computationnelle du Grand Livre.
Spec : doctrine/NOTE_GRAND_LIVRE.md · Module : engine/build_ledger.py
Deux chemins indépendants :
  A · moteur + bibliothèque beancount (loader) — soldes, comptes, dates, métadonnées ;
  B · rasm brut (LE_CORAN.txt, table abjad locale) + fichier ledger parsé EN TEXTE PUR (regex).
Usage : python3 ATTESTATION_LEDGER.py [dossier_FP]
"""
import sys, csv, re, unicodedata, os as _os
from datetime import date, timedelta
from collections import defaultdict

def _resolve_fp():
    for c in (_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'data'), '/mnt/project'):
        if _os.path.exists(_os.path.join(c, 'LE_CORAN.txt')):
            return _os.path.normpath(c)
    raise FileNotFoundError('data/ introuvable')

FP = sys.argv[1] if len(sys.argv) > 1 else _resolve_fp()
_HERE = _os.path.dirname(_os.path.abspath(__file__))
sys.path.insert(0, _os.path.join(_HERE, '..', 'engine'))
from basmala_engine import ANCRES, ANNEES
LEDGER = _os.path.normpath(_os.path.join(_HERE, '..', 'ledger', 'GRAND_LIVRE.beancount'))

n, ecarts = 0, 0
def att(label, ok, detail=""):
    global n, ecarts
    n += 1
    print(f"  [{n:>2}] {'OK ' if ok else 'ÉCART'} — {label}" + (f" ({detail})" if detail else ""))
    if not ok:
        ecarts += 1

T = ANNEES['moyenne']; t0 = ANCRES[1447]; tclot = t0 + timedelta(days=int(T))

# ── attendus depuis les FP (CSV) ──
SJ_s = {int(r['sourate']): int(r['jummal']) for r in csv.DictReader(open(f'{FP}/jummal_par_sourate.csv', encoding='utf-8'))}
SJ = sum(SJ_s.values())
vers = [(int(r['sourate']), int(r['verset']), int(r['jummal']))
        for r in csv.DictReader(open(f'{FP}/01_DATA_jummal_114_par_verset.csv', encoding='utf-8'))]
phr = list(csv.DictReader(open(f'{FP}/MASTER_CALENDRIER_PHRASE.csv', encoding='utf-8')))
f = {int(r['sourate']): int(r['pointe_sourate'])
     for r in csv.DictReader(open(f'{FP}/01_DATA_toniques_114_apex_P2.csv', encoding='utf-8'))}
aff = defaultdict(list)
for s, t in f.items():
    if t != s:
        aff[t].append(s)

print("== A · Le Grand Livre par la bibliothèque beancount (chemin moteur) ==")
from beancount import loader
from beancount.core.data import Transaction, Open
entries, errors, opts = loader.load_file(LEDGER)
att("bean-check : 0 erreur (l'opinion)", len(errors) == 0, f"{len(errors)}")
att("racines renommées = D1", all(opts[k] == v for k, v in (
    ('name_assets', 'Registre'), ('name_liabilities', 'Contrepartie'), ('name_equity', 'Source'),
    ('name_income', 'Revelation'), ('name_expenses', 'Lecture'))))
att("comptes ouverts = 114 tiroirs + 4 têtes", sum(1 for x in entries if isinstance(x, Open)) == 118)

bal = defaultdict(int); tot = 0
cat = defaultdict(int); retours = []; conn = []; extc = 0
for x in entries:
    if not isinstance(x, Transaction):
        continue
    for p in x.postings:
        v = int(p.units.number); bal[p.account] += v; tot += v
    w = x.narration.split(' ')[0]
    cat[w] += 1
    if w == 'QIRAA':
        retours.append(x)
    elif w == 'CONNEXION':
        conn.append(x)
    elif x.narration.startswith('EXTOURNE CONNEXION'):
        extc += 1

att("Σ livre = 0 (la balance)", tot == 0, str(tot))
att("les 114 tiroirs soldent chacun à 0", all(bal[f'Registre:S{s:03d}'] == 0 for s in range(1, 115)))
att("Revelation = −ΣJ", bal['Revelation:Tanzil'] == -SJ, f"{bal['Revelation:Tanzil']} vs −{SJ}")
att("Lecture = +ΣJ", bal['Lecture:Recitation'] == SJ)
att("Source = 0 (dépôt + extourne)", bal['Source:Basmala-Cadre'] == 0)
att("Contrepartie = 0 (déclarée, non mouvementée)", bal['Contrepartie:DetteDeLecture'] == 0)
att("6236 pièces-aller (TANZIL)", cat['TANZIL'] == 6236, str(cat['TANZIL']))
att("10642 pièces-retour (QIRAA)", cat['QIRAA'] == 10642, str(cat['QIRAA']))
att("36 pièces-connexions + 36 extournes", len(conn) == 36 and extc == 36, f"{len(conn)}/{extc}")
att("brins 3 + 3 · à-nouveau 1 + 1", cat['SOUFFLE'] == 3 and cat['A-NOUVEAU'] == 1
    and sum(1 for x in entries if isinstance(x, Transaction) and x.narration.startswith('EXTOURNE SOUFFLE')) == 3
    and sum(1 for x in entries if isinstance(x, Transaction) and x.narration.startswith('EXTOURNE A-NOUVEAU')) == 1)

# connexions conformes au renvoi f
okc = True
vus = set()
for x in conn:
    m = re.match(r'CONNEXION — cible S(\d{3}), (\d+) affluent', x.narration)
    t, k = int(m.group(1)), int(m.group(2)); vus.add(t)
    credits = sorted(int(p.account[-3:]) for p in x.postings if int(p.units.number) == -1)
    debit = [p for p in x.postings if p.account == f'Registre:S{t:03d}' and int(p.units.number) == k]
    okc &= (credits == sorted(aff[t]) and k == len(aff[t]) and len(debit) == 1)
att("les 36 cibles et leurs affluents = le renvoi f (113 arêtes, 1 JML)", okc and vus == set(aff), )
att("l'ermite muet : aucune pièce S013→S013", all('S013' not in x.narration for x in conn))

# dates et métadonnées : la formule vérifiée sur les 10642
attendu = {}
for r in phr:
    attendu[(int(r['sourate']), int(r['phrase']))] = t0 + timedelta(days=int(float(r['frac_debut']) * T))
okd = okm = True
for x in retours:
    m = re.match(r'QIRAA S(\d{3}) phrase (\d+)', x.narration)
    okd &= (x.date == attendu[(int(m.group(1)), int(m.group(2)))])
    okm &= ('fraction' in x.meta and 'hijri' in x.meta)
att("date de chaque retour = t0 + ⌊frac_debut·T⌋ (10642/10642)", okd)
att("métadonnées fraction+hijri sur chaque retour", okm)
dates = [x.date for x in entries if isinstance(x, Transaction)]
att(f"toutes les dates ∈ [{t0}, {tclot}]", min(dates) == t0 and max(dates) == tclot)
att("l'aller entier à t0 (la réception du dossier)",
    all(x.date == t0 for x in entries if isinstance(x, Transaction) and x.narration.startswith('TANZIL')))
att("conservation par sourate : ΣJ(QIRAA) = ΣJ(TANZIL) = FP, 114/114", all(
    sum(int(p.units.number) for x in retours if f'S{s:03d} ' in x.narration for p in x.postings
        if p.account == 'Lecture:Recitation') == SJ_s[s] for s in range(1, 115)))

print("== B · Chemin indépendant : rasm brut + ledger parsé en texte pur ==")
ABJAD = {'ا':1,'ب':2,'ج':3,'د':4,'ه':5,'و':6,'ز':7,'ح':8,'ط':9,'ي':10,'ك':20,'ل':30,'م':40,'ن':50,
         'س':60,'ع':70,'ف':80,'ص':90,'ق':100,'ر':200,'ش':300,'ت':400,'ث':500,'خ':600,'ذ':700,
         'ض':800,'ظ':900,'غ':1000,'ة':5,'ء':1,'ؤ':6,'ئ':10,'ى':10}
def nu(s):
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.replace('ٱ','ا').replace('أ','ا').replace('إ','ا').replace('آ','ا')
SJ_rasm = 0; nv = 0
for l in open(f'{FP}/LE_CORAN.txt', encoding='utf-8'):
    m = re.match(r'(\d+)\|(\d+)\|(.*)', l)
    if m:
        nv += 1
        SJ_rasm += sum(ABJAD.get(c, 0) for c in nu(m.group(3)))
att("rasm brut : 6236 versets", nv == 6236, str(nv))
att("rasm brut : ΣJ = 23 476 120 = |Revelation| du livre", SJ_rasm == 23476120 == -bal['Revelation:Tanzil'], str(SJ_rasm))

txt = open(LEDGER, encoding='utf-8').read()
montants = [int(x) for x in re.findall(r'^  \S+\s+(-?\d+) JML$', txt, re.M)]
att("texte pur : Σ de tous les montants = 0", sum(montants) == 0, str(sum(montants)))
att("texte pur : nombre de lignes-montants = chemin A",
    len(montants) == sum(len(x.postings) for x in entries if isinstance(x, Transaction)), str(len(montants)))
pieces_txt = re.findall(r'^\d{4}-\d{2}-\d{2} \* "(\w[\w-]*)', txt, re.M)
from collections import Counter
ct = Counter(pieces_txt)
att("texte pur : TANZIL 6236 · QIRAA 10642 · CONNEXION 36 · SOUFFLE 3 · A-NOUVEAU 1 · EXTOURNE 40",
    ct['TANZIL'] == 6236 and ct['QIRAA'] == 10642 and ct['CONNEXION'] == 36
    and ct['SOUFFLE'] == 3 and ct['A-NOUVEAU'] == 1 and ct['EXTOURNE'] == 40, dict(ct))
k1 = sum(1 for t in aff if len(aff[t]) == 1)  # cibles à un seul affluent (débit extourné = −1)
att("texte pur : lignes Registre à −1 JML = 113 arêtes + 3 brins extournés + cibles k=1 extournées",
    len(re.findall(r'^  Registre:S\d{3}  -1 JML$', txt, re.M)) == 113 + 3 + k1, f"attendu {113+3+k1}")
att("texte pur : 786 sur S001 — ×2 en débit (α + TANZIL 1:1, J(1:1)=786) et ×2 en crédit (ω + QIRAA basmala S1)",
    len(re.findall(r'^  Registre:S001  786 JML$', txt, re.M)) == 2
    and len(re.findall(r'^  Registre:S001  -786 JML$', txt, re.M)) == 2)

print()
print(f"ATTESTATION LEDGER — {n} assertions — {ecarts} ÉCART{'S' if ecarts != 1 else ''}"
      + (" — le Grand Livre est ÉTABLI [bi] (la machine poste, l'audit solde)" if ecarts == 0 else " — À CORRIGER"))
