#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_relations.py — première batterie de tests de mise en relation entre les 17 objets.
Entrée : OBJETS_ALGEBRIQUES_TABLE.csv (17 objets, 26 invariants).
Sortie : rapport texte. Tout est recalculé sur la donnée (factorisations refaites depuis trace_e1 entier).
Usage : python3 test_relations.py
"""
import csv, itertools
from math import gcd
from functools import reduce

def factor(n):
    f={}; d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=f.get(n,0)+1
    return f

O=[]
for r in csv.DictReader(open('OBJETS_ALGEBRIQUES_TABLE.csv',encoding='utf-8')):
    tr=int(r['trace_e1'])
    O.append(dict(
        key=f"{r['sourate']}·{r['partie']}", src=r['sourate'], part=r['partie'],
        deg=int(r['degre']), tr=tr, trf=factor(tr), ch=int(r['charge']),
        cp=int(r['charge_pos']), cz=int(r['charge_zero']), cn=int(r['charge_neg']),
        pgcd=int(r['pgcd']), vmin=int(r['vmin']), vmax=int(r['vmax']),
        e2=int(r['e2']), e3=int(r['e3']), p1=int(r['p1']), p2=int(r['p2']), p3=int(r['p3']),
        spec=set(int(x) for x in r['premiers_presents'].split()) if r['premiers_presents'] else set()))
N=len(O)
def pr(s=''): print(s)
pr(f"=== {N} objets ===")
for o in O: pr(f"  {o['key']:<26} deg {o['deg']:>3}  trace {o['tr']:>8} = {'·'.join(f'{p}^{e}' if e>1 else str(p) for p,e in sorted(o['trf'].items()))}  charge {o['ch']:+d}")

pr("\n========== 1. TRACES ÉGALES ==========")
seen={}
for o in O: seen.setdefault(o['tr'],[]).append(o['key'])
hit=[(t,k) for t,k in seen.items() if len(k)>1]
pr("aucune" if not hit else "\n".join(f"  trace {t} : {', '.join(k)}" for t,k in hit))

pr("\n========== 2. DIVISIBILITÉ DES TRACES (a | b) ==========")
found=False
for a,b in itertools.permutations(O,2):
    if a['tr']<b['tr'] and b['tr']%a['tr']==0:
        pr(f"  {a['tr']} ({a['key']})  |  {b['tr']} ({b['key']})   quotient {b['tr']//a['tr']}"); found=True
if not found: pr("  aucune")

pr("\n========== 3. FACTEURS PREMIERS COMMUNS ENTRE TRACES ==========")
found=False
for a,b in itertools.combinations(O,2):
    common=set(a['trf'])&set(b['trf'])
    if common:
        pr(f"  {a['key']} ∩ {b['key']} : {{{', '.join(map(str,sorted(common)))}}}"); found=True
if not found: pr("  aucun")

pr("\n========== 4. PGCD DES TRACES DEUX À DEUX (>1) ==========")
rows=[]
for a,b in itertools.combinations(O,2):
    g=gcd(a['tr'],b['tr'])
    if g>1: rows.append((g,a['key'],b['key']))
rows.sort(reverse=True)
pr("aucun >1" if not rows else "\n".join(f"  pgcd {g:>6} : {x} ∧ {y}" for g,x,y in rows[:25]))
if len(rows)>25: pr(f"  … (+{len(rows)-25} paires)")

pr("\n========== 5. SPECTRES (petits premiers présents) ==========")
for o in O: pr(f"  {o['key']:<26} {{{' '.join(map(str,sorted(o['spec'])))}}}")
pr("  — paires à spectre identique :")
f=False
for a,b in itertools.combinations(O,2):
    if a['spec']==b['spec'] and a['spec']: pr(f"    {a['key']} = {b['key']} : {{{' '.join(map(str,sorted(a['spec'])))}}}"); f=True
if not f: pr("    aucune")
pr("  — paires à spectres disjoints :")
f=False
for a,b in itertools.combinations(O,2):
    if a['spec'] and b['spec'] and not (a['spec']&b['spec']): pr(f"    {a['key']} ⟂ {b['key']}"); f=True
if not f: pr("    aucune")

pr("\n========== 6. CHARGES ==========")
pr("  par objet (charge globale ; n+,n0,n-) :")
for o in O: pr(f"    {o['key']:<26} {o['ch']:+d}   ({o['cp']},{o['cz']},{o['cn']})")
pos=[o['key'] for o in O if o['ch']>0]; neg=[o['key'] for o in O if o['ch']<0]; zer=[o['key'] for o in O if o['ch']==0]
pr(f"  bilan : +1 → {len(pos)} | 0 → {len(zer)} | −1 → {len(neg)}")
pr(f"    Σ charges des 17 = {sum(o['ch'] for o in O):+d}")

pr("\n========== 7. COÏNCIDENCES DE DEGRÉ ==========")
degs={}
for o in O: degs.setdefault(o['deg'],[]).append(o['key'])
for d,k in sorted(degs.items()):
    if len(k)>1: pr(f"  degré {d} : {', '.join(k)}")

pr("\n========== 8. COÏNCIDENCES D'INVARIANTS (e2,e3,p2,p3,vmin,vmax) ==========")
for inv in ('e2','e3','p2','p3','vmin','vmax'):
    m={}
    for o in O: m.setdefault(o[inv],[]).append(o['key'])
    h=[(v,k) for v,k in m.items() if len(k)>1]
    if h: pr(f"  {inv} partagé : "+" ; ".join(f"{v}→[{', '.join(k)}]" for v,k in h))

pr("\n[fin — batterie 1. Étendre ensuite aux objets niveau-sourate et aux relations e_k/Newton croisées.]")
