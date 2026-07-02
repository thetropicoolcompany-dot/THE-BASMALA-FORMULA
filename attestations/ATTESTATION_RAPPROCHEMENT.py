# -*- coding: utf-8 -*-
"""ATTESTATION_RAPPROCHEMENT — le théorème du rapprochement (اقترب, 1+4) et l'horizon.
Usage : python3 ATTESTATION_RAPPROCHEMENT.py [dossier_FP]
Recompte tout depuis le rasm et les FP.
"""
import sys, re, csv, unicodedata

import os as _os
def _resolve_fp():
    for c in (_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'data'), '/mnt/project'):
        if _os.path.exists(_os.path.join(c, 'LE_CORAN.txt')): return _os.path.normpath(c)
    raise FileNotFoundError('data/ introuvable')
FP = sys.argv[1] if len(sys.argv) > 1 else _resolve_fp()
n, ecarts = 0, 0

def att(label, ok, detail=""):
    global n, ecarts
    n += 1
    print(f"  [{n:>2}] {'OK ' if ok else 'ÉCART'} — {label}" + (f" ({detail})" if detail else ""))
    if not ok: ecarts += 1

A = {'ا':1,'ب':2,'ج':3,'د':4,'ه':5,'و':6,'ز':7,'ح':8,'ط':9,'ي':10,'ك':20,'ل':30,'م':40,
     'ن':50,'س':60,'ع':70,'ف':80,'ص':90,'ق':100,'ر':200,'ش':300,'ت':400,'ث':500,'خ':600,
     'ذ':700,'ض':800,'ظ':900,'غ':1000,'ة':5,'ء':1,'ؤ':6,'ئ':10,'ى':10}
J = lambda w: sum(A.get(c, 0) for c in w.replace(' ', ''))
ch = lambda x: ((x % 3) + 1) % 3 - 1
def nu(s):
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.replace('ٱ','ا').replace('أ','ا').replace('إ','ا').replace('آ','ا')

V = {}
for l in open(f'{FP}/LE_CORAN.txt', encoding='utf-8'):
    m = re.match(r'(\d+)\|(\d+)\|(.*)', l)
    if m: V[(int(m.group(1)), int(m.group(2)))] = nu(m.group(3))
jv = {}
with open(f'{FP}/01_DATA_jummal_114_par_verset.csv', encoding='utf-8') as fh:
    for r in csv.DictReader(fh):
        jv[(int(r['sourate']), int(r['verset']))] = int(r['jummal'])

print("== 1 · LES CINQ ATTESTATIONS DE LA RACINE (le 1 + 4) ==")
occ = []
for sv, t in V.items():
    for w in t.split():
        w2 = ''.join(c for c in w if c in A)
        if re.match(r'^و?اقتربت?$', w2): occ.append(sv)
occ.sort()
att("اقترب : exactement 5 attestations au rasm", occ == [(7,185),(21,1),(21,97),(54,1),(96,19)], str(occ))
att("quatre approches + un appelé : 96:19 est le DERNIER verset de S96",
    (96,20) not in V and (96,19) in V)
att("J(اقترب) = 703 = 19·37 (la basmala × l'image du pli)", J('اقترب') == 703 == 19*37)
att("J(96:19) = 1349 = 19·71 = 19·حساب", jv[(96,19)] == 1349 == 19*J('حساب') and J('حساب') == 71)

print("== 2 · LES QUATRE APPROCHES ET LEURS TÉMOINS (dans l'ordre du rasm) ==")
appro = [('اجلهم', (7,185), 79, 1), ('حسابهم', (21,1), 116, -1),
         ('الوعد الحق', (21,97), 250, 1), ('الساعة', (54,1), 167, -1)]
for w, sv, jval, c in appro:
    present = all(x in V[sv] for x in w.split())
    att(f"{sv[0]}:{sv[1]} porte {w} = {jval}, charge {c:+d}", present and J(w) == jval and ch(jval) == c)
att("l'ordre du rasm des 4 approches = l'ordre des 4 témoins (S4→S13→S98→S1)",
    [sv for _, sv, _, _ in appro] == sorted(sv for _, sv, _, _ in appro))
att("les charges des 4 approches alternent +1,−1,+1,−1 (le battement, Σ=0)",
    [c for *_, c in appro] == [1,-1,1,-1] and sum(c for *_, c in appro) == 0)
att("Σ(4 approches) = 612 = 36·17 (les connexions × la trame)",
    sum(j for _, _, j, _ in appro) == 612 == 36*17)
att("Σ(5) = 612 + 1349 = 1961 = 37·53 (l'image × le facteur du raffinement)",
    612 + jv[(96,19)] == 1961 == 37*53)

print("== 3 · LES ANCRAGES DE LA CORRESPONDANCE ==")
att("حسابهم = حساب + هم = 71 + 45 (S13 : l'objet EST l'office)",
    J('حسابهم') == J('حساب') + J('هم') == 116)
att("2:282 lie le terme et les témoins : اجل ET شهيدين dans le même verset (S4)",
    'اجل' in V[(2,282)] and 'شهيدين' in V[(2,282)])
att("1:4 porte يوم الدين = 151 (S1 tient l'Heure)", 'يوم الدين' in V[(1,4)] and J('يوم الدين') == 151)
att("البينة = يحييكم = 98 (la Preuve = ce-qui-fait-vivre, 8:24 ; S98)",
    J('البينة') == J('يحييكم') == 98 and 'يحييكم' in V[(8,24)])
att("الساعة = فسواك = 167, premiers tous deux dans le rasm (54:1 · 82:7)",
    J('الساعة') == J('فسواك') == 167 and 'فسواك' in V[(82,7)])
att("اجلهم = 79, premier (le fil 79)", J('اجلهم') == 79)

print("== 4 · LES DEUX SCEAUX ET LES TROIS « PLUS PROCHE » ==")
att("J(54:1) = J(96:1) = 2884 (l'Heure approchée pèse « Lis ! »)",
    jv[(54,1)] == jv[(96,1)] == 2884)
att("50:16 : اقرب + حبل الوريد au rasm ; حبل الوريد = 291 = السر",
    'اقرب' in V[(50,16)] and 'حبل الوريد' in V[(50,16)] and J('حبل الوريد') == 291 == J('السر'))
att("8:24 : Allah entre l'homme et son cœur, et لما يحييكم (la vie)",
    'يحول بين المرء وقلبه' in V[(8,24)] and 'يحييكم' in V[(8,24)])
att("56:85 : « plus proches que vous » dans la sourate du triptyque",
    'اقرب اليه منكم' in V[(56,85)])
att("56:7-11 : ازواجا ثلاثة → الميمنة / المشامة / المقربون ; المقربون = 429 = 3·11·13",
    'ازواجا ثلاثة' in V[(56,7)] and 'الميمنة' in V[(56,8)] and 'المشامة' in V[(56,9)]
    and 'المقربون' in V[(56,11)] and J('المقربون') == 429 == 3*11*13)

print("== 5 · L'HORLOGE (les totaux et la trotteuse) ==")
tot_l = tot_j = 0
with open(f'{FP}/jummal_par_sourate.csv', encoding='utf-8') as fh:
    for r in csv.DictReader(fh):
        tot_l += int(r['lettres']); tot_j += int(r['jummal'])
n_phr = sum(1 for _ in open(f'{FP}/PHRASES_114_waqf.csv', encoding='utf-8')) - 1
att("totaux FP : 332 837 lettres · 23 476 120 jummal · 10 642 phrases",
    tot_l == 332837 and tot_j == 23476120 and n_phr == 10642)
s_an = 12 * 29.530589 * 86400
att("cadences (année lunaire moyenne) : phrase ≈ 47,95 min · jummal ≈ 1,304 s",
    abs(s_an/n_phr/60 - 47.95) < 0.01 and abs(s_an/tot_j - 1.304) < 0.001)

print()
print(f"ATTESTATION RAPPROCHEMENT — {n} assertions — {ecarts} ÉCART{'S' if ecarts != 1 else ''}"
      + (" — [bi]" if ecarts == 0 else " — À CORRIGER"))
