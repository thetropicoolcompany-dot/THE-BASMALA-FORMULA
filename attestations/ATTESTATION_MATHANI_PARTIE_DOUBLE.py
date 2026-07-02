# -*- coding: utf-8 -*-
"""
ATTESTATION_MATHANI_PARTIE_DOUBLE.py — prouve l'étude du doublement :
le مثاني, le cycle qui solde, la série doublée {228,300,306,308,310},
et l'ancrage natif du « compter deux fois » (2:282).
Tout est recompté sur les FP, en arithmétique entière exacte [bi].
Usage : python3 ATTESTATION_MATHANI_PARTIE_DOUBLE.py [dossier_FP]   (defaut : /mnt/project)
"""
import csv, re, sys, unicodedata
from collections import Counter, defaultdict

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

ABJAD = {'ا':1,'ب':2,'ج':3,'د':4,'ه':5,'و':6,'ز':7,'ح':8,'ط':9,'ي':10,'ك':20,'ل':30,
         'م':40,'ن':50,'س':60,'ع':70,'ف':80,'ص':90,'ق':100,'ر':200,'ش':300,'ت':400,
         'ث':500,'خ':600,'ذ':700,'ض':800,'ظ':900,'غ':1000,
         'ة':5,'ء':1,'أ':1,'إ':1,'آ':1,'ؤ':6,'ئ':10,'ى':10}
J = lambda w: sum(ABJAD.get(c, 0) for c in w)
def isprime(n):
    if n < 2: return False
    d = 2
    while d*d <= n:
        if n % d == 0: return False
        d += 1
    return True

txt = open(f'{FP}/LE_CORAN.txt', encoding='utf-8').read().split('\n')
def nu(s):
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.replace('ٱ','ا').replace('أ','ا').replace('إ','ا').replace('آ','ا')
def refs(motif):
    out = []
    for l in txt:
        if re.search(motif, nu(l)):
            m = re.match(r'(\d+)\|(\d+)\|', l)
            if m: out.append((int(m.group(1)), int(m.group(2))))
    return out

print("— I. La structure et son amplitude (le socle du doublement) —")
f = {}
with open(f'{FP}/01_DATA_toniques_114_apex_P2.csv', encoding='utf-8') as fh:
    for row in csv.DictReader(fh):
        f[int(row['sourate'])] = int(row['pointe_sourate'])
indeg = Counter(f.values())
A(sum(1 for s in f if indeg.get(s,0)==0) == 77 and [s for s in f if f[s]==s] == [13]
  and len(set(f.values())-{13}) == 36, "114 = 77 sources + 36 connexions + 1 fixe {13}")
A(114+36 == 150 and 150+3 == 153 and 153+1 == 154 == 77+77, "la bascule 114→150→153→154 = 77+77")
A(sum(len(re.findall(r'\bكلا\b', nu(l))) for l in txt if l.startswith('96|')) == 3
  and 3*J('كلا') == 153, "les 3 كلا de S96 (rasm) × 51 = 153")
A(154-114 == 40 == 36+3+1, "amplitude aller = 40 = 36+3+1")
A(2*40 == 80 == J('حسيب'), "LE CYCLE (aller-retour) = 2×40 = 80 = حسيب — le double passage porte le comptable")
A(J('حسيبا') == 81 == 80+1, "حسيبا = 81 = 80 + 1 (le cycle + le +1)")
A(2*indeg[1] == 114, "2 × deg_in(S1) = 2×57 = 114 — le volume se plie en deux sur l'attracteur")

print("— II. Le مثاني : le redoublement redoublé —")
r_math = refs(r'مثاني')
A(len(r_math) == 2 and set(r_math) == {(15,87),(39,23)},
  "مثاني attesté EXACTEMENT 2 fois : 15:87 (les sept-مثاني) et 39:23")
A(J('مثاني') == 601 and isprime(601), "J(مثاني) = 601, premier")
A(J('المثاني') == 632 == 8*79 and J('عددا') == 79, "المثاني = 632 = 8 × 79 = 8 × عددا")
A(J('مثنى') == 600 and J('مثاني') == J('مثنى')+1,
  "مثاني = مثنى + 1 (601 = 600+1) — l'écho de باسم = بسم + 1")
A(J('باسم') == J('بسم')+1, "باسم = بسم + 1 (le +1 du lecteur)")
v = {}
with open(f'{FP}/01_DATA_jummal_114_par_verset.csv', encoding='utf-8') as fh:
    for row in csv.DictReader(fh):
        v[(int(row['sourate']), int(row['verset']))] = int(row['jummal'])
A(v[(1,7)] == 6010 == 10*601, "J(1:7) = 6010 = 10 × مثاني — la sourate des sept-مثاني clôt sur dix fois le mot")

print("— III. La série doublée {228, 300, 306, 308, 310} au rasm —")
mots = Counter()
for l in txt:
    m = re.match(r'\d+\|\d+\|(.*)', l)
    if m:
        for w in nu(m.group(1)).split():
            w = ''.join(c for c in w if c in ABJAD)
            if w: mots[w] += 1
parJ = defaultdict(Counter)
for w, n in mots.items(): parJ[J(w)][w] = n
vd = defaultdict(list)
for k, j in v.items(): vd[j].append(k)
A(J('صراط') == 300 and parJ[300]['صراط'] == 32, "300 = 2×150 : mot dominant صراط ×32 (le chemin)")
A(len(vd[228]) == 0 and len(vd[300]) == 0 and len(vd[306]) == 0,
  "aucun verset ne pèse 228, 300 ou 306 — les doubles de structure sans incarnation-verset")
A(vd[308] == [(53,34)], "UN SEUL verset J=308 = 2×154 dans tout le Coran : 53:34")
A(vd[310] == [(53,62)], "UN SEUL verset J=310 = 2×155 : 53:62 — le dernier d'an-Najm (sajda)")
A(parJ[310]['شاهد'] >= 1 and parJ[310]['اشهد'] >= 1 and parJ[310]['قرئ'] >= 1,
  "310 porte شاهد, اشهد, قرئ — le témoin, atteste, est-lu")
ph = defaultdict(list)
with open(f'{FP}/PHRASES_114_waqf.csv', encoding='utf-8') as fh:
    for row in csv.DictReader(fh):
        ph[int(row['jummal'])].append((int(row['sourate']), int(row['phrase']), row['rasm']))
A(len(ph[154]) == 0, "AUCUNE phrase (0/10642) ne pèse 154 — le nombre-registre est la somme, pas une pièce")
A(len(ph[155]) == 1 and ph[155][0][0] == 11, "UNE SEULE phrase pèse 155 : dans S11 (هود)")
A(len(ph[306]) == 1 and ph[306][0][0] == 8 and 'واصبروا' in nu(ph[306][0][2]).replace(' ',''),
  "UNE SEULE phrase pèse 306 = 2×153 : S8, « واصبروا »")
A(len(ph[601]) == 3 and any(s == 53 for s,_,_ in ph[601]),
  "3 phrases pèsent 601 = مثاني, dont une dans S53 (صحف موسى)")
A(sorted(s for s,_,_ in ph[228]) == [8, 39],
  "les 2 phrases à 228 = 2×114 : S8 et S39 — la sourate du verset مثاني")

print("— IV. L'ancrage natif du « compter deux fois » —")
A(J('شهيدين') == 379 and isprime(379) and refs(r'\bشهيدين\b') == [(2,282)],
  "شهيدين = 379 (premier), attesté UNE fois : 2:282 — la contre-signature double de la créance")
A(len(refs(r'\bمرتين\b')) == 5 and set(refs(r'\bمرتين\b')) == {(9,101),(9,126),(17,4),(28,54),(33,31)},
  "مرتين (« deux fois ») ×5, dont 2 dans S9 la singularité")
A(len(refs(r'\bضعفين\b')) == 3 and J('ضعفين') == 1010, "ضعفين (le double) ×3 ; J = 1010")
A(refs(r'\bكفلين\b') == [(57,28)] and J('كفلين') == 190 == 10*19, "كفلين (deux parts) ×1 : 57:28 ; 190 = 10×19")
A(len(refs(r'\bمثنى\b')) == 3, "مثنى (deux par deux) ×3")

print(f"\nATTESTATION COMPLÈTE — {N} assertions — 0 ÉCART — [bi]")
