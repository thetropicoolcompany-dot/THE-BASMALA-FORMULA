# -*- coding: utf-8 -*-
"""
ATTESTATION_AUDIT_ROLES.py — qui prouve la doctrine du protocole d'audit
(le mandat du rapporteur, la chaine des offices, le perimetre dynamique).
Toutes les assertions sont recomptees sur les FP, en arithmetique entiere exacte [bi].
FP requis (lecture seule) :
  LE_CORAN.txt · 01_DATA_jummal_114_par_verset.csv · jummal_par_sourate.csv
  01_DATA_toniques_114_apex_P2.csv
Usage : python3 ATTESTATION_AUDIT_ROLES.py [dossier_FP]   (defaut : /mnt/project)
"""
import csv, re, sys, unicodedata
from collections import Counter

import os as _os
def _resolve_fp():
    for c in (_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'data'), '/mnt/project'):
        if _os.path.exists(_os.path.join(c, 'LE_CORAN.txt')): return _os.path.normpath(c)
    raise FileNotFoundError('data/ introuvable')
FP = sys.argv[1] if len(sys.argv) > 1 else _resolve_fp()
N = 0
def A(cond, label):
    global N
    N += 1
    assert cond, f"ECHEC assertion {N}: {label}"
    print(f"  [{N:02d}] OK — {label}")

# ---------------------------------------------------------------- table abjad (protocole §2)
ABJAD = {'ا':1,'ب':2,'ج':3,'د':4,'ه':5,'و':6,'ز':7,'ح':8,'ط':9,'ي':10,'ك':20,'ل':30,
         'م':40,'ن':50,'س':60,'ع':70,'ف':80,'ص':90,'ق':100,'ر':200,'ش':300,'ت':400,
         'ث':500,'خ':600,'ذ':700,'ض':800,'ظ':900,'غ':1000,
         'ة':5,'ء':1,'أ':1,'إ':1,'آ':1,'ؤ':6,'ئ':10,'ى':10}
J = lambda w: sum(ABJAD.get(c, 0) for c in w)

def isprime(n):
    if n < 2: return False
    d = 2
    while d * d <= n:
        if n % d == 0: return False
        d += 1
    return True

print("— I. Le rapporteur est le +1 —")
A(J('بسم') == 102 and J('باسم') == 103, "باسم = 103 = بسم + 1 (le +1 de la lecture)")
A(isprime(103) and not isprime(102) and 102 == 2*3*17, "103 premier ; الحساب = 102 = 2·3·17 compose")
A(J('الحساب') == 102, "الحساب = 102 = بسم (le Compte est le Nom)")
A(J('القارئ') == 342 and 342 % 3 == 0, "القارئ = 342, charge 0 (le lecteur n'est pas un jeton)")

print("— II. Le mandat : حسيبا, la delegation 3+1 —")
A(J('حسيبا') == 81 == 3**4, "حسيبا = 81 = 3^4")
A(J('كفى') == 110 == J('على'), "كفى = 110 = على (l'axe du pli)")
A(J('حاسبين') == 131 and isprime(131), "حاسبين = 131, premier")
A(786 == 2*3*131 and J('بسم')+J('الله')+J('الرحمن')+J('الرحيم') == 786,
  "786 = 2·3·131 = ΣJ(basmala) — la place du rapporteur dans la factorisation de l'origine")

# ---------------------------------------------------------------- rasm
txt = open(f'{FP}/LE_CORAN.txt', encoding='utf-8').read().split('\n')
def nu(s):
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.replace('ٱ','ا').replace('أ','ا').replace('إ','ا').replace('آ','ا')
def refs(pattern):
    out = []
    for line in txt:
        if re.search(pattern, nu(line)):
            m = re.match(r'(\d+)\|(\d+)\|', line)
            if m: out.append((int(m.group(1)), int(m.group(2))))
    return out

r_hasib = refs(r'\bحسيبا?\b')
A(len(r_hasib) == 4 and set(r_hasib) == {(4,6),(4,86),(17,14),(33,39)},
  "حسيب attesté exactement 4× : {4:6, 4:86, 33:39} divines + {17:14} déléguée = 3+1")
r_iqra = refs(r'\bاقرا\b')
A(len(r_iqra) == 3 and set(r_iqra) == {(96,1),(96,3),(17,14)},
  "اقرأ (l'ordre) attesté exactement 3× : 96:1 (باسم), 96:3, 17:14")
r_hasibin = refs(r'حاسبين')
A(len(r_hasibin) == 2 and set(r_hasibin) == {(6,62),(21,47)},
  "حاسبين (les comptables) attesté exactement 2× : 6:62, 21:47")
l_982 = [l for l in txt if l.startswith('98|2|')]
A(len(l_982) == 1 and 'يتلو صحفا مطهرة' in nu(l_982[0]),
  "98:2 porte يتلو صحفا مطهرة (le lecteur-récitant, siège S98)")
A(all('بِاسْمِ' in l for l in txt if l.startswith('96|1|')),
  "96:1 : l'ordre اقرأ est donné بِاسْمِ — au Nom (le donneur d'ordre délègue l'origine)")

print("— III. La chaine des offices : les ancres —")
A(J('القصص') == 311 == J('شهداء'), "القصص = شهداء = 311 — le raconté EST le témoignage (siège S4)")
A(J('زبد') == 13, "زبد = 13 — « auditer, c'est ce tri » (siège S13)")
A(J('البينة') == 98, "البينة = 98 — le nom porte le numéro (siège S98)")
A(J('الحمد') == 83, "الحمد = 83 — le quitus (siège S1)")
A(J('كاتب') == 423 == J('كتاب'), "كاتب = كتاب = 423 — le scribe est le livre (le rédacteur S1)")
A(J('كتاب') + J('مبين') == 525 == J('الفاتحة'), "كتاب مبين = 525 = الفاتحة — le registre manifeste est l'Ouvrante")
A(J('مبين') == 102, "مبين = 102 = بسم = الحساب")
A(J('أحصى') == 109 and isprime(109), "أحصى = 109, premier (les dénombrées)")

# ---------------------------------------------------------------- masses (l'ordre de la chaine)
sj = {}
with open(f'{FP}/jummal_par_sourate.csv', encoding='utf-8') as fh:
    for row in csv.DictReader(fh):
        sj[int(row['sourate'])] = int(row['jummal'])
print("— IV. L'ordre de la chaine = l'ordre des masses —")
A(sj[4] == 1118210 and sj[13] == 239874 and sj[98] == 28891 and sj[1] == 10147,
  "ΣJ : S4=1 118 210 · S13=239 874 · S98=28 891 · S1=10 147")
A(sj[4] > sj[13] > sj[98] > sj[1],
  "raconté > audité > lu > compté : l'ordre terrestre→divin (§3) EST l'ordre des conditions")

# ---------------------------------------------------------------- versets
v1 = {}; j1714 = None
with open(f'{FP}/01_DATA_jummal_114_par_verset.csv', encoding='utf-8') as fh:
    for row in csv.DictReader(fh):
        s, v, j = int(row['sourate']), int(row['verset']), int(row['jummal'])
        if v == 1: v1[s] = j
        if (s, v) == (17, 14): j1714 = j
print("— V. Les versets-clés —")
A(sorted(s for s, j in v1.items() if j == 786) == [1],
  "J(1:1) = 786, unique des 114 : l'audit séquentiel commence à l'origine manifestée")
A(j1714 == 1365 == 3*5*7*13, "J(17:14) = 1365 = 3·5·7·13 — le mandat porte la signature du Compte (13)")

# ---------------------------------------------------------------- flux f (le perimetre)
f = {}
with open(f'{FP}/01_DATA_toniques_114_apex_P2.csv', encoding='utf-8') as fh:
    for row in csv.DictReader(fh):
        f[int(row['sourate'])] = int(row['pointe_sourate'])
print("— VI. Le périmètre : la partition dynamique des 114 —")
A(len(f) == 114, "le flux f est défini sur les 114")
A([s for s in f if f[s] == s] == [13], "point fixe unique : {13} (l'ermite immobile)")
A(f[1] == 4 and f[4] == 98 and f[98] == 1, "le cycle de l'œil : 1→4→98→1")
A(f[96] == 2, "f(96) = 2 (le donneur d'ordre pointe, rien ne lui revient par f)")
indeg = Counter(f.values())
A(indeg.get(96, 0) == 0 and indeg[1] == 57 and indeg[4] == 3 and indeg[98] == 1 and indeg[13] == 1,
  "deg_in : S96=0 · S1=57=3·19 · S4=3 · S98=1 · S13=1")
A(sum(1 for s in f if indeg.get(s, 0) == 0) == 77, "77 sources (deg_in 0)")
A(len(set(f.values()) - {13}) == 36, "36 connexions (cibles non-fixes)")
COEUR = {1, 4, 98, 13}
def terminal(s):
    vus = set()
    while s not in vus:
        vus.add(s); s = f[s]
    return s
A(all(terminal(s) in COEUR for s in f), "décantation totale : toutes les orbites finissent dans le cœur")
trans = [s for s in f if s not in COEUR and s != 96]
A(len(trans) == 109 and 1 + 4 + 109 == 114,
  "la partition : 114 = 1 (S96) + 4 (le cœur = les 4 témoins) + 109 (les transitoires)")
def bassin(s):
    while s not in COEUR: s = f[s]
    return s
bas = Counter(bassin(s) for s in f if s not in COEUR)
A(bas == Counter({1: 108, 4: 2}), "bassins des 110 hors-cœur : 108 → S1, 2 → S4")
A(bassin(96) == 1 and bassin(9) == 1, "S96 et S9 (le creux) décantent vers S1")

print("— VII. La face-source : بسم^(0) et le solde des charges —")
A(J('بسم') % 3 == 0, "بسم = 102 ≡ 0 : l'exposant de la face-source est (0) ; le +1 est la lecture (باسم=103)")
ch = lambda n: {0: 0, 1: +1, 2: -1}[n % 3]
A(ch(J('الله')) == 0 and ch(J('الرحمن')) == -1 and ch(J('الرحيم')) == +1,
  "les trois Noms portent les trois brins : الله 0 · الرحمن −1 · الرحيم +1")
A(ch(102) + ch(66) + ch(329) + ch(289) == 0 == ch(786),
  "Σ(exposants de la face 3+1) = 0 = charge(786) — le solde exact")
A(ch(sj[4]) == -1 and ch(sj[13]) == 0 and ch(sj[98]) == +1 and ch(sj[1]) == +1,
  "charges-corps des témoins : شهداء −1 · الحساب 0 · البينة +1 · الحمد +1")
A(ch(sj[4]) + ch(sj[13]) + ch(sj[98]) + ch(sj[1]) == +1 and ch(sj[96]) == -1,
  "Σ(4 témoins) = +1, refermé par S96 (corps −1) = 0 — le rapport soldé")
A(114 + 36 == 150 and 150 + 3 == 153 and 153 + 1 == 154 == 77 + 77,
  "la bascule : 114 →+36→ 150 →+3→ 153 →+1→ 154 = 77+77")

print(f"\nATTESTATION COMPLÈTE — {N} assertions — 0 ÉCART — [bi]")
