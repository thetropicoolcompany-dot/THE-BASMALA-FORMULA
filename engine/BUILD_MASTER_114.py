#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ATTESTATION + BUILD — « Compter par phrases ce que le souffle a CONTÉ par versets »
La décision centrale de S96 : la lecture à rebours (ω→α) qui libère le double.

Le Coran est un CONTE manifeste (sourate / ligne-verset / jummal) recélant un
COMPTE caché (sourate / phrase / jummal). L'homologie conte/compte est native
(racine ق-ص-ص : قصص le récit / قصاص le règlement exact) — testée en T8.

Deux fonctions :
  (1) PROUVER — T0..T8, 39 assertions, J recalculé depuis le RASM brut. [bi]
  (2) CONSTRUIRE — la table maîtresse par sourate, qui FUSIONNE le compte (objet
      algébrique : OBJETS_114_phrase.csv) et le conte (la ventilation versets↔phrases).
      -> MASTER_114_CONTE_COMPTE.csv  (supersède ces deux fichiers).

Aucun nombre récité de mémoire : tout est recompté sur les FP.

FP requis (lecture seule) :
  - LE_CORAN.txt                          (rasm, segmenté sourate|verset|rasm)
  - 01_DATA_jummal_114_par_verset.csv     (J par verset)
  - PHRASES_114_waqf.csv                  (J par phrase, découpe waqf)
  - jummal_par_sourate.csv                (ΣJ, versets, lettres par sourate)
  - 01_DATA_noms_jummal_114.csv           (nom + jummal du nom)
  - 01_DATA_toniques_114_apex_P2.csv      (renvoi f = pointe_sourate)

Usage :  python3 ATTESTATION_VERSETS_PHRASES_S96.py
Sortie :  rapport PASS/FAIL + écrit MASTER_114_CONTE_COMPTE.csv
"""
import csv, re, sys
from collections import defaultdict
from math import gcd
from functools import reduce

# ----------------------------------------------------------------------
# Outils : table abjad, jummal, charge, factorisation, e2/e3 (Newton)
# ----------------------------------------------------------------------
ABJAD = {'ا':1,'أ':1,'إ':1,'آ':1,'ٱ':1,'ء':1,'ب':2,'ج':3,'د':4,'ه':5,'ة':5,
         'و':6,'ؤ':6,'ز':7,'ح':8,'ط':9,'ي':10,'ى':10,'ئ':10,'ك':20,'ل':30,
         'م':40,'ن':50,'س':60,'ع':70,'ف':80,'ص':90,'ق':100,'ر':200,'ش':300,
         'ت':400,'ث':500,'خ':600,'ذ':700,'ض':800,'ظ':900,'غ':1000}
def J(s):
    return sum(ABJAD.get(c, 0) for c in s)
def charge(n):
    r = n % 3
    return 0 if r == 0 else (1 if r == 1 else -1)
def norm_search(s):          # squelette consonantique (recherche de racine, T8)
    out = []
    for c in s:
        cp = ord(c)
        if 0x064B <= cp <= 0x0652 or cp in (0x0670, 0x0640) \
           or 0x06D6 <= cp <= 0x06DC or 0x0610 <= cp <= 0x061A:
            continue
        out.append(c)
    s = ''.join(out)
    for a in 'أإآٱ':
        s = s.replace(a, 'ا')
    return s
def factor_str(n):           # factorisation par division d'essai (ΣJ par sourate)
    if n <= 1:
        return str(n)
    fs = {}; m = n; d = 2
    while d * d <= m:
        while m % d == 0:
            fs[d] = fs.get(d, 0) + 1; m //= d
        d += 1 if d == 2 else 2
    if m > 1:
        fs[m] = fs.get(m, 0) + 1
    return '·'.join(f'{p}' if e == 1 else f'{p}^{e}' for p, e in sorted(fs.items()))
def e2_e3(vals):             # fonctions symétriques e2,e3 via sommes de Newton (exact, O(n))
    p1 = sum(vals); p2 = sum(x * x for x in vals); p3 = sum(x ** 3 for x in vals)
    return (p1 * p1 - p2) // 2, (p1 ** 3 - 3 * p1 * p2 + 2 * p3) // 6

PASS, FAIL = [], []
def check(label, cond, got=None):
    (PASS if cond else FAIL).append((label, got))
    print(("  OK  " if cond else " FAIL ") + label + ("" if got is None else f"   [{got}]"))

# ----------------------------------------------------------------------
# Lecture des FP
# ----------------------------------------------------------------------
Jverse_raw = {}; SJ_sourate_raw = defaultdict(int); verses_norm = []; nverse_raw = 0
with open('LE_CORAN.txt', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n').strip()
        if not line or '|' not in line:
            continue
        s, v, rasm = line.split('|', 2)
        s, v = int(s), int(v)
        j = J(rasm)
        Jverse_raw[(s, v)] = j
        SJ_sourate_raw[s] += j
        verses_norm.append(norm_search(rasm))
        nverse_raw += 1
def root_count(pat):
    return sum(1 for r in verses_norm if pat in r)

Jverse_csv = {}
with open('01_DATA_jummal_114_par_verset.csv', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        Jverse_csv[(int(row['sourate']), int(row['verset']))] = int(row['jummal'])

basmala = {}; frag = defaultdict(int); nphrase = 0
phrases_par_sourate = defaultdict(int); frags_par_sourate = defaultdict(int)
roots = defaultdict(list)          # jummal des phrases par sourate (racines de l'objet)
SJ_phrase_raw = 0
with open('PHRASES_114_waqf.csv', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        s = int(row['sourate']); tag = row['versets']
        jr = J(row['rasm']); jc = int(row['jummal'])
        if jr != jc:
            FAIL.append((f"rasm!=jummal phrase {s}.{row['phrase']}", (jr, jc)))
        nphrase += 1
        phrases_par_sourate[s] += 1
        roots[s].append(jr)
        SJ_phrase_raw += jr
        if 'basmala' in tag:
            basmala[s] = jr
        else:
            v = int(re.fullmatch(r'V(\d+)\.\d+', tag).group(1))
            frag[(s, v)] += jr
            frags_par_sourate[s] += 1

SJ_sourate_csv = {}; versets_csv = {}; lettres = {}
with open('jummal_par_sourate.csv', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        s = int(row['sourate'])
        SJ_sourate_csv[s] = int(row['jummal'])
        versets_csv[s] = int(row['versets'])
        lettres[s] = int(row['lettres'])

noms = {}; nom_jummal = {}
with open('01_DATA_noms_jummal_114.csv', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        s = int(row['sourate'])
        noms[s] = row['nom']; nom_jummal[s] = int(row['jummal_nom'])

f_pointe = {}
with open('01_DATA_toniques_114_apex_P2.csv', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        f_pointe[int(row['sourate'])] = int(row['pointe_sourate'])

versets_raw = defaultdict(int)
for (s, v) in Jverse_raw:
    versets_raw[s] += 1

V = nverse_raw; P = nphrase

print("=" * 68)
print("ATTESTATION + BUILD  versets ↔ phrases  —  l'acte central de S96")
print("Le souffle CONTE par versets · S96 COMPTE par phrases")
print("=" * 68)

# ----------------------------------------------------------------------
# T0..T8 — la preuve (39 assertions)
# ----------------------------------------------------------------------
print("\n[T0] Table abjad = table FP (ΣJ par sourate : rasm brut == jummal_par_sourate.csv)")
check("114/114 sourates concordent",
      all(SJ_sourate_raw[s] == SJ_sourate_csv[s] for s in range(1, 115)))

print("\n[T1] INVARIANT (le قصاص, équivalence exacte) : un seul grand livre")
SJ_verse_raw_tot = sum(Jverse_raw.values()); SJ_sourate_tot = sum(SJ_sourate_csv.values())
check("ΣJ(versets, rasm brut)  = 23 476 120", SJ_verse_raw_tot == 23476120, SJ_verse_raw_tot)
check("ΣJ(phrases, rasm brut)  = 23 476 120", SJ_phrase_raw == 23476120, SJ_phrase_raw)
check("ΣJ(sourates)            = 23 476 120", SJ_sourate_tot == 23476120, SJ_sourate_tot)
check("versets == phrases == sourates (mesure conservée)",
      SJ_verse_raw_tot == SJ_phrase_raw == SJ_sourate_tot)

print("\n[T2] COMPTES : 6236 versets (conte), 10642 phrases (compte), 114 sourates")
check("versets V = 6236", V == 6236, V)
check("phrases P = 10642", P == 10642, P)
check("sourates = 114", len(versets_raw) == 114, len(versets_raw))
check("Σ versets/sourate (CSV) = 6236", sum(versets_csv.values()) == 6236)

print("\n[T3] RAFFINEMENT STRICT : reconstruire J(verset) depuis les phrases")
mismatch = 0
for (s, v), jv in Jverse_csv.items():
    rec = frag.get((s, v), 0) + (basmala[s] if (v == 1 and s in basmala) else 0)
    if rec != jv:
        mismatch += 1
check("6236/6236 versets reconstruits exactement (0 écart)", mismatch == 0, f"écarts={mismatch}")
check("basmala de tête : valeur unique = 786", set(basmala.values()) == {786})
check("nombre de basmalas de tête = 113", len(basmala) == 113, len(basmala))
check("seule S9 est sans basmala de tête", sorted(set(range(1, 115)) - set(basmala)) == [9])

print("\n[T4] PARTIE DOUBLE : charge(conte) ⊕ charge(compte) = solde 0")
check("charge(V=6236) = -1 (débit, le conte / le souffle)", charge(V) == -1)
check("charge(P=10642) = +1 (crédit, le compte / le révélé)", charge(P) == 1)
check("charge(V+P=16878) = 0 (balance)", charge(V + P) == 0)

print("\n[T4-bis] LE CRÉDIT ÉMERGE : la basmala révélée flippe la charge")
Q = P - len(basmala); B = len(basmala)
check("fragments Q=10529 ≡ -1 (raffiner ne change pas le signe)", charge(Q) == -1, f"{Q}")
check("basmalas B=113 ≡ -1", charge(B) == -1, f"{B}")
check("Q ⊕ B = P : (-1)⊕(-1) ≡ +1 (mod3) — le crédit émerge",
      charge(Q + B) == 1 and Q + B == P)

print("\n[T5] DÉCOMPOSITION de P et parallèle des bascules")
check("P = 10529 (fragments) + 113 (basmalas)", Q == 10529 and B == 113)
offset = P - V; splits = Q - V
check("P - V = 4406", offset == 4406)
check("P - V = 113 (basmalas) + 4293 (raffinement waqf)", 113 + splits == offset)
check("raffinement waqf 4293 = 3^4 · 53 (la base-souffle 3)", splits == (3**4) * 53, splits)
check("comptes : 154 - 114 = 40 = 36 + 3 + 1", 154 - 114 == 36 + 3 + 1)

print("\n[T6] MASSE RÉVÉLÉE : la basmala déplacée (caché→explicite), 113 × 786")
check("113 × 786 = 88818 = 2·3·113·131", 113 * 786 == 88818 == 2 * 3 * 113 * 131)
check("ΣJ inchangé : la basmala est relocalisée, pas ajoutée",
      SJ_verse_raw_tot == SJ_phrase_raw)

print("\n[T7] POINTS FIXES : S1 (p=v), S96 (+1), S13 (→114)")
p = phrases_par_sourate; vv = versets_raw
fixes = [s for s in range(1, 115) if p[s] == vv[s]]
check("S1 est l'UNIQUE sourate où phrases = versets (=7)", fixes == [1] and p[1] == 7)
check("S96 (l'auditeur) : 19 versets → 20 phrases, delta = +1", vv[96] == 19 and p[96] == 20)
check("S13 (point fixe de f) : 43 versets → exactement 114 phrases", vv[13] == 43 and p[13] == 114)
check("0 phrases<versets ; 113 phrases>versets ; 1 égale",
      sum(1 for s in range(1,115) if p[s] < vv[s]) == 0
      and sum(1 for s in range(1,115) if p[s] > vv[s]) == 113 and len(fixes) == 1)

print("\n[T8] CONTE / COMPTE : l'homologie native (racine ق-ص-ص)")
check("قصص (le récit / le CONTE) attesté 10×", root_count('قصص') == 10, root_count('قصص'))
check("قصاص (le règlement exact / le COMPTE) attesté 4×", root_count('قصاص') == 4, root_count('قصاص'))
check("J(قصص) = 280", J('قصص') == 280)
check("J(قصاص) = 281 = قصص + 1 (l'alif, forme III réciproque)",
      J('قصاص') == 281 and J('قصاص') - J('قصص') == J('ا'))
check("القصص = شهداء = ورقة = 311 (le récit témoigné)",
      J('القصص') == J('شهداء') == J('ورقة') == 311)
check("الحساب = بسم = 102 (le compte = le Nom)", J('الحساب') == J('بسم') == 102)
check("axe-ligne س-ط-ر : أساطير 9× , مسطور 3×",
      root_count('ساطير') == 9 and root_count('مسطور') == 3)
check("chiasme : charge(قصص)=+1 , charge(قصاص)=-1",
      charge(J('قصص')) == 1 and charge(J('قصاص')) == -1)

# ----------------------------------------------------------------------
# T9 — CONSTRUCTION DE LA TABLE MAÎTRESSE (fusion conte ⊕ compte ⊕ objet)
# ----------------------------------------------------------------------
print("\n[T9] TABLE MAÎTRESSE : fusion par sourate (conte ⊕ compte ⊕ objet)")
# validation de la formule e2/e3 par combinaisons (S1)
from itertools import combinations as _comb
from math import prod as _prod
_v = roots[1]
check("e2/e3 (Newton) == combinaisons (contrôle S1)",
      e2_e3(_v) == (sum(_prod(c) for c in _comb(_v, 2)),
                    sum(_prod(c) for c in _comb(_v, 3))))
# cohérence f-renvoi
check("renvoi f : f(96)=2, f(13)=13 (point fixe), 77 sources",
      f_pointe[96] == 2 and f_pointe[13] == 13 and 114 - len(set(f_pointe.values())) == 77)

COLS = ['sourate', 'nom', 'nom_jummal', 'f_pointe', 'lettres',
        'versets', 'phrases', 'basmala_tete', 'fragments', 'delta_phr_vers',
        'SJ', 'SJ_facteurs', 'charge_versets', 'charge_phrases', 'charge_SJ',
        'pgcd', 'distinct', 'vmin', 'vmax',
        'charge_pos', 'charge_zero', 'charge_neg', 'charge_somme', 'e2', 'e3']
out = 'MASTER_114_CONTE_COMPTE.csv'
tot_phr = tot_ver = tot_sj = 0
with open(out, 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh); w.writerow(COLS)
    for s in range(1, 115):
        vals = roots[s]
        SJ = sum(vals)
        cp = sum(1 for x in vals if charge(x) == 1)
        cz = sum(1 for x in vals if charge(x) == 0)
        cn = sum(1 for x in vals if charge(x) == -1)
        e2, e3 = e2_e3(vals)
        w.writerow([s, noms[s], nom_jummal[s], f_pointe[s], lettres[s],
                    vv[s], p[s], 1 if s in basmala else 0, frags_par_sourate[s], p[s] - vv[s],
                    SJ, factor_str(SJ), charge(vv[s]), charge(p[s]), charge(SJ),
                    reduce(gcd, vals), len(set(vals)), min(vals), max(vals),
                    cp, cz, cn, cp - cn, e2, e3])
        tot_phr += p[s]; tot_ver += vv[s]; tot_sj += SJ
check("table : Σ phrases = 10642", tot_phr == 10642, tot_phr)
check("table : Σ versets = 6236", tot_ver == 6236, tot_ver)
check("table : Σ SJ = 23 476 120", tot_sj == 23476120, tot_sj)

# ----------------------------------------------------------------------
# Bilan
# ----------------------------------------------------------------------
print("\n" + "=" * 68)
print(f"BILAN : {len(PASS)} assertions vérifiées, {len(FAIL)} échec(s).")
if FAIL:
    print("ÉCHECS :")
    for lab, got in FAIL:
        print("   -", lab, got)
    sys.exit(1)
print("TOUT VÉRIFIÉ — [bi].")
print(f"Table maîtresse écrite : {out}  (25 colonnes × 114 sourates)")
print("  -> fusionne et supersède OBJETS_114_phrase.csv et VENTILATION_VERSETS_PHRASES_114.csv")
print("=" * 68)
