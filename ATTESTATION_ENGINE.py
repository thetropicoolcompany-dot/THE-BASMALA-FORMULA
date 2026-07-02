# -*- coding: utf-8 -*-
"""ATTESTATION_ENGINE — la partie double computationnelle du basmala_engine.
Chaque grandeur de l'engine est recalculée ici par un CHEMIN INDÉPENDANT
(sources différentes ou algorithmes différents), puis comparée.
Usage : python3 ATTESTATION_ENGINE.py [dossier_FP]
"""
import sys, csv
from datetime import date

import os as _os
def _resolve_fp():
    for c in (_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'data'), '/mnt/project'):
        if _os.path.exists(_os.path.join(c, 'LE_CORAN.txt')): return _os.path.normpath(c)
    raise FileNotFoundError('data/ introuvable')
FP = sys.argv[1] if len(sys.argv) > 1 else _resolve_fp()
sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'engine'))
from basmala_engine import Engine, J, charge, ANNEES, ANCRES

n, ecarts = 0, 0
def att(label, ok, detail=""):
    global n, ecarts
    n += 1
    print(f"  [{n:>2}] {'OK ' if ok else 'ÉCART'} — {label}" + (f" ({detail})" if detail else ""))
    if not ok: ecarts += 1

e = Engine(FP)
g = e.grandeurs()

print("== 1 · Les grandeurs : engine (rasm) vs chemin indépendant (CSV sources) ==")
tot_l = tot_j = tot_v = 0
with open(f'{FP}/jummal_par_sourate.csv', encoding='utf-8') as fh:
    for r in csv.DictReader(fh):
        tot_l += int(r['lettres']); tot_j += int(r['jummal']); tot_v += int(r['versets'])
att("lettres : rasm recompté == CSV source", g['lettres'] == tot_l == 332837, f"{g['lettres']:,}")
att("jummal : rasm recompté == CSV source", g['jummal'] == tot_j == 23476120, f"{g['jummal']:,}")
att("versets : rasm == CSV", g['versets'] == tot_v == 6236)
att("phrases : MASTER == PHRASES_114_waqf",
    g['phrases'] == sum(1 for _ in open(f'{FP}/PHRASES_114_waqf.csv', encoding='utf-8')) - 1 == 10642)
att("mots porteurs : 78 248 (recompte rasm)", g['mots'] == 78248, f"{g['mots']:,}")

print("== 2 · L'horloge : le clic, le tempo, la basmala ==")
att("N_clic = 2·(ΣJ+786+39) = 46 953 890 = 2·5·101·46489",
    e.N_clic() == 46953890 == 2*5*101*46489)
att("τ(moyenne) ∈ [0,652071 ; 0,652073] s", 0.652071 < e.tau('moyenne') < 0.652073,
    f"{e.tau('moyenne'):.6f}")
att("τ(354) < τ(moyenne) < τ(355)", e.tau('354') < e.tau('moyenne') < e.tau('355'))
att("la première écriture du registre = la basmala (786, charge 0)",
    int(e.phr[0]['jummal']) == 786 and int(e.phr[0]['is_basmala']) == 1
    and charge(786) == 0)
att("le cadran est complet : frac 0 → 1, cumul lettres = total",
    float(e.phr[0]['frac_debut']) == 0.0
    and abs(float(e.phr[-1]['frac_fin']) - 1.0) < 1e-9
    and int(e.phr[-1]['cum_lettres_fin']) == g['lettres'])

print("== 3 · La position : engine (bisect) vs chemin indépendant (scan linéaire) ==")
def position_independante(d, t0, an):
    f = ((d - t0).days % an) / an
    with open(f'{FP}/MASTER_CALENDRIER_PHRASE.csv', encoding='utf-8') as fh:
        for r in csv.DictReader(fh):
            if float(r['frac_debut']) <= f < float(r['frac_fin']):
                return int(r['sourate']), int(r['phrase'])
    return None
for d, attendu in [(date(2026, 7, 2), (9, 44)),      # la démonstration live (S9, la singularité)
                   (date(2026, 3, 13), (1, 1)),       # l'aube d'ouverture → la basmala de 1:1
                   (date(2026, 12, 25), None)]:       # un jour quelconque : concordance seule
    p = e.position(d)
    indep = position_independante(d, ANCRES[1447], ANNEES['moyenne'])
    ok = (p['sourate'], p['phrase']) == indep and (attendu is None or indep == attendu)
    att(f"position({d}) : deux chemins concordent" + (f" et = S{attendu[0]} phr.{attendu[1]}" if attendu else ""),
        ok, f"S{p['sourate']} phr.{p['phrase']}")
att("l'ouverture (t0) lit la basmala même : J(phrase) = 786",
    e.position(date(2026, 3, 13))['jummal_phrase'] == 786)

print("== 4 · Les conventions : abjad et charge ==")
att("J(بسم الله الرحمن الرحيم rasm 1:1) = 786", J(e.versets[(1, 1)]) == 786)
att("charge : 786→0, 103→+1, 305→−1", charge(786) == 0 and charge(103) == 1 and charge(305) == -1)

print()
print(f"ATTESTATION ENGINE — {n} assertions — {ecarts} ÉCART{'S' if ecarts != 1 else ''}"
      + (" — partie double computationnelle ÉTABLIE [bi]" if ecarts == 0 else " — À CORRIGER"))
