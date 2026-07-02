# -*- coding: utf-8 -*-
"""build_site.py — génère web/data/*.json depuis l'engine (jamais saisi).
Usage : python3 build/build_site.py
"""
import os, sys, json, csv

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))
from basmala_engine import Engine, ANNEES, ANCRES, LUNAISON

e = Engine()
g = e.grandeurs()

# phrases.json — le cadran complet (compact)
phrases = [{
    's': int(r['sourate']), 'n': r['nom'], 'p': int(r['phrase']),
    'v': r['versets'], 'j': int(r['jummal']), 'c': int(r['charge']),
    'b': int(r['is_basmala']), 'juz': int(r['juz']),
    'f0': float(r['frac_debut']), 'f1': float(r['frac_fin']),
    'r': r.get('rasm', '')
} for r in e.phr]
# le rasm n'est pas dans MASTER : le joindre depuis PHRASES_114_waqf
rasm = {}
with open(os.path.join(e.fp, 'PHRASES_114_waqf.csv'), encoding='utf-8') as fh:
    for r in csv.DictReader(fh):
        rasm[(int(r['sourate']), int(r['phrase']))] = r['rasm']
for p in phrases:
    p['r'] = rasm.get((p['s'], p['p']), '')

meta = {
    'titre': 'The Basmala Formula — Ḥisāb al-Qurʾān',
    'grandeurs': g,
    'N_clic': e.N_clic(),
    'tau': {k: ANNEES[k] * 86400 / e.N_clic() for k in ANNEES},
    'annees_jours': ANNEES, 'lunaison': LUNAISON,
    'ancres': {str(k): str(v) for k, v in ANCRES.items()},
    'basmala': 786,
}

out = os.path.join(HERE, '..', 'web', 'data')
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, 'phrases.json'), 'w', encoding='utf-8') as fh:
    json.dump(phrases, fh, ensure_ascii=False, separators=(',', ':'))
with open(os.path.join(out, 'meta.json'), 'w', encoding='utf-8') as fh:
    json.dump(meta, fh, ensure_ascii=False, indent=1)
print(f"web/data/phrases.json : {len(phrases)} phrases, "
      f"{os.path.getsize(os.path.join(out,'phrases.json')):,} o")
print(f"web/data/meta.json : N_clic={meta['N_clic']:,}, τ(moyenne)={meta['tau']['moyenne']:.6f}")
