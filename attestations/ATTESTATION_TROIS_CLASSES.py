# -*- coding: utf-8 -*-
"""ATTESTATION_TROIS_CLASSES — écume (زبد) · globe (تكوير) · « bulle » (proscrite).
Usage : python3 ATTESTATION_TROIS_CLASSES.py [dossier_FP] [dossier_PAQUET]
Recompte tout depuis le rasm et les FP ; vérifie les corrections dans les livrables.
"""
import sys, os, re, csv, unicodedata

FP = sys.argv[1] if len(sys.argv) > 1 else '/mnt/project'
PQ = sys.argv[2] if len(sys.argv) > 2 else '/home/claude'
n, ecarts = 0, 0

def att(label, ok, detail=""):
    global n, ecarts
    n += 1
    print(f"  [{n:>2}] {'OK ' if ok else 'ÉCART'} — {label}" + (f" ({detail})" if detail else ""))
    if not ok: ecarts += 1

A = {'ا':1,'ب':2,'ج':3,'د':4,'ه':5,'و':6,'ز':7,'ح':8,'ط':9,'ي':10,'ك':20,'ل':30,'م':40,
     'ن':50,'س':60,'ع':70,'ف':80,'ص':90,'ق':100,'ر':200,'ش':300,'ت':400,'ث':500,'خ':600,
     'ذ':700,'ض':800,'ظ':900,'غ':1000,'ة':5,'ء':1,'ؤ':6,'ئ':10,'ى':10}
J = lambda w: sum(A.get(c, 0) for c in w)
def nu(s):
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.replace('ٱ','ا').replace('أ','ا').replace('إ','ا').replace('آ','ا')

txt = open(f'{FP}/LE_CORAN.txt', encoding='utf-8').read().split('\n')
versets = {}
for l in txt:
    m = re.match(r'(\d+)\|(\d+)\|(.*)', l)
    if m: versets[(int(m.group(1)), int(m.group(2)))] = nu(m.group(3))
jv = {}
with open(f'{FP}/01_DATA_jummal_114_par_verset.csv', encoding='utf-8') as fh:
    for r in csv.DictReader(fh):
        jv[(int(r['sourate']), int(r['verset']))] = int(r['jummal'])

print("== 1 · ÉCUME (زبد) ==")
hits = [sv for sv, t in versets.items() if 'زبد' in t]
att("racine زبد : verset unique 13:17", hits == [(13, 17)], str(hits))
formes = [w2 for w in versets[(13,17)].split() for w2 in [''.join(c for c in w if c in A)] if 'زبد' in w2]
att("trois formes dans 13:17 (زبدا، زبد، الزبد)", sorted(formes) == sorted(['زبدا','زبد','الزبد']), str(formes))
att("J(زبد) = 13 = numéro de sa sourate", J('زبد') == 13)
att("J(13:17) = 13272 = 2³·3·7·79, charge 0", jv[(13,17)] == 13272 == 8*3*7*79 and 13272 % 3 == 0)
att("le repoussoir natif جفاء est DANS 13:17", 'جفاء' in versets[(13,17)])
att("J(جفاء) = 85 = 5·17 (le 17 de la trame ; verset 17 ; 153 = 9·17)", J('جفاء') == 85 == 5*17 and 153 == 9*17)
att("J(رابيا) = 214 = J(روح) (la montée est le souffle)", J('رابيا') == 214 == J('روح'))

print("== 2 · GLOBE (تكوير) ==")
kur = []
for sv, t in versets.items():
    for w in t.split():
        w2 = ''.join(c for c in w if c in A)
        if re.match(r'^و?(يكور|كورت)$', w2): kur.append((sv, w2))
att("racine كور : exactement 3 attestations en 2 versets", len(kur) == 3 and {sv for sv, _ in kur} == {(39,5),(81,1)}, str(kur))
att("يكور ×2 en 39:5 — la seconde portée par le waw (ويكور = 242)",
    [w for sv, w in kur if sv == (39,5)] == ['يكور','ويكور'] and J('ويكور') == 242)
att("كورت en 81:1 (V1 de la sourate)", [(sv, w) for sv, w in kur if sv == (81,1)] == [((81,1),'كورت')])
with open(f'{FP}/01_DATA_noms_jummal_114.csv', encoding='utf-8') as fh:
    noms = {int(r['sourate']): (r['nom'], int(r['jummal_nom'])) for r in csv.DictReader(fh)}
att("S81 se nomme التكوير, J = 667 = 23·29", noms[81][0] == 'التكوير' and noms[81][1] == 667 == 23*29, str(noms[81]))
att("J(يكور) = 236 = 2²·59 · J(كورت) = 626 = 2·313", J('يكور') == 236 == 4*59 and J('كورت') == 626 == 2*313)
att("faux ami كرة = كرّة (un retour) : 4 attestations, aucune sphère",
    sum(1 for sv, t in versets.items() if re.search(r'\bكرة\b', t)) == 4)
att("فقاع/نفاخ/حباب (bulle) : 0 attestation",
    all(sum(1 for t in versets.values() if rac in t) == 0 for rac in ('فقاع','نفاخ','حباب')))

print("== 3 · LA SOUDURE (le mur, 61:4) ==")
att("بنيان مرصوص est dans 61:4", 'بنيان مرصوص' in versets[(61,4)])
att("J(بنيان) = 113 (premier) ; بنيان + 1 = 114", J('بنيان') == 113 and 113 + 1 == 114
    and all(113 % p for p in (2,3,5,7)))
att("J(بنيان مرصوص) = 539 = 7²·11 (anse du cadre)", J('بنيان') + J('مرصوص') == 539 == 49*11)
att("ΣJ(61:4) = 2548 = 14²·13 = زبدا²·زبد (le mur soudé, puissance de l'écume)",
    jv[(61,4)] == 2548 == J('زبدا')**2 * J('زبد'))
att("J(سورة) + J(زبد) = 284 = J(الرحمة) (l'enclos + l'écume = le dedans du mur)",
    J('سورة') + J('زبد') == 284 == J('الرحمة'))

print("== 4 · LES LIVRABLES CORRIGÉS ET GRAVÉS ==")
def lit(f):
    for base in (PQ, '/mnt/user-data/outputs', FP):
        p = os.path.join(base, f)
        if os.path.exists(p): return open(p, encoding='utf-8').read()
    return None
for f in ('FEUILLE_AUDIT_S1_v1.tex', 'RECUEIL_FIGURES_NATIF_TIKZ_v1.tex', 'FIGURES_GLOBE_ECUME_S1_TIKZ_v1.tex'):
    s = lit(f)
    att(f"{f} : zéro « bulle », جفاء présent", s is not None and 'bulle' not in s.lower() and 'جفاء' in s)
proto = lit('00_PROTOCOLE.md')
att("protocole §1 : globe (تكوير) gravé + « bulle » proscrite",
    proto is not None and '**globe** (`تكوير`' in proto and '**« bulle »** : **proscrit**' in proto)
cadre = lit('PROTOCOLE_GENERAL_AUDIT.md')
att("cadre §IX·F : « le globe = l'enroulement » + anses (زبد=13, بنيان=113, 14²·13)",
    cadre is not None and "le globe = l'enroulement" in cadre and 'زبد=13' in cadre
    and 'بنيان=113' in cadre and '14²·13' in cadre)
feuille = lit('FEUILLE_AUDIT_S1_v1.tex')
att("feuille S1 : le globe-sourate ancré (تكوير, 39:5 ; 81:1)",
    feuille is not None and 'licite (\\ar{تكوير}' in feuille)

print("== 5 · LA TOPOLOGIE DES TROIS ÉTATS (la paroi, le flux, la dynamique S81) ==")
att("زبدا رابيا (l'écume montante) est dans 13:17, indéfinie", 'زبدا رابيا' in versets[(13,17)])
att("J(زبدا رابيا) = 228 = 2×114 (le double du volume, le مثاني en mouvement)",
    J('زبدا') + J('رابيا') == 228 == 2*114)
att("J(السيل) = 131 = J(حاسبين), premiers (le flux porteur = les comptables)",
    J('السيل') == 131 == J('حاسبين') and all(131 % p for p in (2,3,5,7,11)))
att("786 = 6·السيل (la basmala est six fois le flux)", 786 == 6 * J('السيل'))
att("J(فاحتمل) = 559 = 13·43 (le porteur porte le 13 de l'écume)", J('فاحتمل') == 559 == 13*43)
att("la séquence S81 au rasm : كورت(1) نشرت(10) كشطت(11) — pli, dépli, paroi retirée",
    'كورت' in versets[(81,1)] and 'نشرت' in versets[(81,10)] and 'كشطت' in versets[(81,11)])
att("J(كشطت) = 729 = 3⁶ (la paroi retirée : pur ternaire de la charge)", J('كشطت') == 729 == 3**6)
att("81:14 : علمت نفس ما احضرت (le compte présenté clôt la dislocation)",
    'علمت نفس ما احضرت' in versets[(81,14)])
with open(f'{FP}/MASTER_114_CONTE_COMPTE.csv', encoding='utf-8') as fh:
    s81 = next(r for r in csv.DictReader(fh) if int(r['sourate']) == 81)
att("S81 : 29 versets → 30 phrases (le globe défait rend le +1)",
    int(s81['versets']) == 29 and int(s81['phrases']) == 30)

print("== 6 · LA FORME FINALE : les trois écritures = les trois états (table des objets) ==")
from math import gcd
from functools import reduce
def sym(rac):
    """e1, e2, e3 par sommes symétriques exactes (entiers)."""
    e1 = sum(rac)
    e2 = sum(rac[i]*rac[j] for i in range(len(rac)) for j in range(i+1, len(rac)))
    e3 = sum(rac[i]*rac[j]*rac[k] for i in range(len(rac)) for j in range(i+1, len(rac)) for k in range(j+1, len(rac)))
    return e1, e2, e3
with open(f'{FP}/OBJETS_ALGEBRIQUES_TABLE.csv', encoding='utf-8') as fh:
    objs = {(r['sourate'], r['partie'][:1]): r for r in csv.DictReader(fh)}
for cle, nomobj in [(('S1','A'), "S1·A"), (('S1','B'), "S1·B"), (('S96','b'), "basmala S96")]:
    r = objs[cle]
    rac = [int(x) for x in r['racines'].split()]
    e1, e2, e3 = sym(rac)
    ch = [((ri % 3) + 1) % 3 - 1 for ri in rac]
    ok_depl = (e1 == int(r['trace_e1'])
               and (len(rac) < 2 or e2 == int(r['e2']))
               and (len(rac) < 3 or e3 == int(r['e3'])))
    ok_red = (ch.count(1), ch.count(0), ch.count(-1)) == tuple(int(r[k]) for k in ('charge_pos','charge_zero','charge_neg'))
    ok_g = reduce(gcd, rac) == int(r['pgcd'])
    att(f"{nomobj} : déployée (e1..e3) = نشرت, réduite mod 3 = كشطت, paroi = pgcd — colonnes exactes",
        ok_depl and ok_red and ok_g, f"deg {len(rac)}, e1={e1}")
att("l'invariant traverse les écritures : e1 identique en close, déployée, réduite (le قصاص)",
    all(sum(int(x) for x in objs[c]['racines'].split()) == int(objs[c]['trace_e1'])
        for c in (('S1','A'), ('S1','B'), ('S96','b'))))

print("== 7 · LA VIE ET LA FORME : les liaisons avec les trois états ==")
att("صورة + الحياة = صوركم (301+55=356, le mot de 40:64/64:3)",
    J('صورة') + J('الحياة') == J('صوركم') == 356)
att("ركبك = ويكور = 242 (l'assemblé-en-forme = l'enroulant : la vie au globe)",
    J('ركبك') == J('ويكور') == 242 and 'ركبك' in versets[(82,8)] and 'ويكور' in versets[(39,5)])
att("علق + مرصوص = كورت (200+426=626 : l'adhérence scellée = l'enroulé)",
    J('علق') + J('مرصوص') == J('كورت') == 626)
att("المصور + وصوركم = كشطت = 3⁶ (le Nom + l'acte de former = la paroi retirée)",
    J('المصور') + J('وصوركم') == J('كشطت') == 729)
att("الحي × الحياة = باب × بنيان مرصوص = 2695",
    J('الحي') * J('الحياة') == J('باب') * (J('بنيان') + J('مرصوص')) == 2695)
with open(f'{FP}/MASTER_114_CONTE_COMPTE.csv', encoding='utf-8') as fh:
    sj81 = next(int(r['SJ']) for r in csv.DictReader(fh) if int(r['sourate']) == 81)
att("ΣJ(S81) = صورناكم × 101 = 11·37·101 (la sourate du Globe pèse la formation ×101)",
    sj81 == 41107 == J('صورناكم') * 101 and J('صورناكم') == 11*37 and 'صورناكم' in versets[(7,11)])
att("زبد + حياة = 37 = l'image du pli (153 = 77+37+36+3)",
    J('زبد') + J('حياة') == 37 and 153 == 77 + 37 + 36 + 3)
att("pgcd(صورة, فاحتمل) = 43 (la forme et le porteur : paroi commune)",
    gcd(J('صورة'), J('فاحتمل')) == 43)
att("علق = القسط = 200 (la première forme du vivant = l'équité de la pesée)",
    J('علق') == J('القسط') == 200)
att("l'homographe du rasm : الصور = 327 (la Forme = le Cor, نفخ في الصور)",
    J('الصور') == 327 and 'الصور' in versets[(39,68)])

print()
print(f"ATTESTATION TROIS CLASSES — {n} assertions — {ecarts} ÉCART{'S' if ecarts != 1 else ''}"
      + (" — [bi]" if ecarts == 0 else " — À CORRIGER"))
