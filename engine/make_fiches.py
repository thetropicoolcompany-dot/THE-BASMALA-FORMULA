import sys, csv, itertools
from math import comb, gcd
from functools import reduce
exec(open('/home/claude/build_granulaire.py').read())
code=sys.argv[1]; MAXLIST=20
rows,groups,seen,Jp,Pa,iP,iQ,cP,cQ,lr = build(code)
ABJAD="ا1 ب2 ج3 د4 ه5 و6 ز7 ح8 ط9 ي10 ك20 ل30 م40 ن50 س60 ع70 ف80 ص90 ق100 ر200 ش300 ت400 ث500 خ600 ذ700 ض800 ظ900 غ1000"
DIAC=any(ord(c) in range(0x064B,0x0653) or ord(c)==0x0670 or ord(c)==0x0640 or ord(c) in range(0x06D6,0x06DD) for r in rows for c in r['rasm'])
ekP=[((-1)**k)*cP[k] for k in range(len(cP))]
def coeffs_lines(c):
    n=len(c)-1
    if n<=25: return '\n'.join(f"  X^{n-i:>3} : {a}" for i,a in enumerate(c))
    head='\n'.join(f"  X^{n-i:>3} : {c[i]}" for i in range(4))
    tail='\n'.join(f"  X^{n-i:>3} : {c[i]}" for i in range(n-3,n+1))
    return head+f"\n  …  ({n-7} coefficients intermédiaires — tous dans {code}_obj_coeffs.csv)\n"+tail
# --- non granulaire ---
md=f"""# FICHE OBJET ALGÉBRIQUE — {code} · {NOM[code]}

> Niveau phrases (degré {iP['n']}) et niveau parties (degré {iQ['n']}). Critère de découpage : {CRIT[code]}. ΣJ basmala-incluse. Tout se redérive de la table abjad, du rasm, et de la définition de J.

## A · Socle
Table abjad : {ABJAD}. Règles : ة=5 ; ء=أ=إ=آ=ٱ=1 ; ؤ=6 ; ئ=ى=10 ; harakat, tatweel (U+0640), alif suscrit (U+0670), waqf = 0. Source `LE_CORAN.txt`. J(phrase)=Σ valeurs des lettres du rasm.

## B · Vecteur des racines J=(J₁…J{iP['n']})
| i | partie | versets | rasm | Jᵢ | facteurs | charge |
|--:|:--|:--|:--|--:|:--|:--:|
""" + '\n'.join(f"| {i+1} | {r['partie']} | {r['versets']} | {r['rasm']} | {r['jummal']} | {r['facteurs']} | {charge(int(r['jummal'])):+d} |" for i,r in enumerate(rows)) + f"""

## C · Polynôme P(X)=∏(X−Jᵢ)
P(X)=Σ(−1)ᵏeₖX^(n−k). Viète itératif. Coefficients (X^{iP['n']}→X^0) :
{coeffs_lines(cP)}

Sommes de Newton : p₁={iP['p1']}, p₂={iP['p2']}, p₃={iP['p3']}.

## D · Invariants
- trace e₁=ΣJ={iP['e1']}={iP['e1f']} ; produit eₙ=∏J={iP['prod']}.
- pgcd={iP['pgcd']} → {'primitif' if iP['prim'] else 'NON primitif'}.
- distinct {iP['distinct']} ; min/max {iP['vmin']}/{iP['vmax']}.
- spectre : {iP['nprimes']} premiers ; petits présents {{{iP['present']}}} ; absents {{{iP['absent']}}} → {'saturé' if iP['absent']=='∅' else 'lacunaire'}.
- charges (n₊,n₀,n₋)=({iP['cpos']},{iP['czero']},{iP['cneg']}) ; somme {iP['scharge']:+d} ; charge globale {iP['cglob']:+d}.

## E · Étage parties
Vecteur des sommes de parties : ({', '.join(map(str,Pa))}).
| partie | Σ | facteurs | charge |
|:--|--:|:--|:--:|
""" + '\n'.join(f"| {nm} | {v} | {facstr(v)} | {charge(v):+d} |" for nm,v in seen) + f"""

Q(X)=∏(X−Pⱼ) deg {iQ['n']} ; e₁(Q)={iQ['e1']}={iQ['e1f']} ; charges ({iQ['cpos']},{iQ['czero']},{iQ['cneg']}) somme {iQ['scharge']:+d}.

## F · Contrôles
Σ(parties)={sum(Pa)} = Σ(phrases)={sum(Jp)} = ΣJ({code}). ✔ e₁(P)={ekP[1]}=trace. ✔
"""
open(f'/home/claude/FICHE_OBJET_{code}.md','w',encoding='utf-8').write(md)
# --- granulaire ---
g=[f"# FICHE OBJET ALGÉBRIQUE — {code} · {NOM[code]} — VERSION GRANULAIRE\n",
   f"> Granularité maximale : chaque nombre dérivé de la lettre au coefficient. Compagnons : `{code}_decomposition_lettres.csv` (chaque caractère), `{code}_fonctions_symetriques.csv` (chaque eₖ ; termes explicites quand C(m,k)≤60).\n",
   "## A · Socle\n",
   f"Table abjad : {ABJAD}. Mise à zéro : harakat (U+064B–0652), tatweel (U+0640), alif suscrit (U+0670), waqf (U+06D6–06DC), espace. J=Σ valeurs.\n",
   "## B · De la lettre au jummal\n"]
b=rows[0]; cum=0; chain=[]
for ch in b['rasm']:
    v=ab.get(ch,0)
    if v>0: cum+=v; chain.append(f"`{ch}`{v}")
note=" — rasm diacrité, la mise à zéro des harakat est visible caractère par caractère dans le compagnon" if DIAC else " — rasm nu"
g.append(f"Phrase 1 ({b['partie']}) « {b['rasm']} »{note}. Lettres porteuses :\n")
g.append(' + '.join(chain)+f" = **{cum}**.\n")
g.append(f"Les {iP['n']} phrases sont dérivées de même (Σ lettres = jummal, vérifié par assertion). Détail exhaustif : `{code}_decomposition_lettres.csv`.\n")
g.append("## C · Vecteur des racines\n")
g.append("| i | partie | versets | rasm | Jᵢ | facteurs | charge |\n|--:|:--|:--|:--|--:|:--|:--:|")
for i,r in enumerate(rows,1): g.append(f"| {i} | {r['partie']} | {r['versets']} | {r['rasm']} | {r['jummal']} | {r['facteurs']} | {charge(int(r['jummal'])):+d} |")
g.append("\n## D · Les objets par partie — dérivation complète jummal → polynôme\n")
for nm,J in groups.items():
    m=len(J); c=poly(J); tr=sum(J); pr=reduce(lambda a,b:a*b,J); gg=reduce(gcd,J) if m>1 else J[0]
    g.append(f"### Objet « {nm} » — degré {m}\nRacines (jummal des phrases) : {J}.\nFonctions symétriques élémentaires (valeur = factorisation ; nb de termes C({m},k)) :")
    ks=range(1,m+1) if m<=MAXLIST else list(range(1,4))+list(range(m-2,m+1))
    for k in ks:
        ek=((-1)**k)*c[k]; g.append(f"- e{k} ({comb(m,k)} terme{'s' if comb(m,k)>1 else ''}) = {ek} = {facstr(ek)}")
    if m>MAXLIST: g.append(f"- … (e₄…e₍{m-3}₎ : valeurs dans `{code}_fonctions_symetriques.csv`)")
    poly_disp = poly_str(c) if m<=MAXLIST else f"X^{m} − {tr}·X^{m-1} + … (deg {m}, {m+1} coefficients dans `{code}_obj_coeffs.csv`)"
    g.append(f"\n**Polynôme** : R(X) = {poly_disp}\nInvariants :")
    g.append(f"- trace e₁={tr}={facstr(tr)} ; produit eₘ={pr if m<=MAXLIST else '(voir CSV)'}{('='+facstr(pr)) if m<=MAXLIST else ''}")
    if m==2:
        st=euclid(J[0],J[1]); g.append(f"- pgcd={gg} (Euclide : "+', '.join(f'{a}={q}·{b}+{r}' for a,b,q,r in st)+")")
    else:
        g.append(f"- pgcd={gg}")
    g.append(f"- charge de la partie = {charge(tr):+d}")
    g.append(f"- Newton : p₁={sum(J)}, p₂={sum(j*j for j in J)}, p₃={sum(j**3 for j in J)}\n")
g.append(f"## E · Contrôle\nΣ des traces des parties = {sum(sum(J) for J in groups.values())} = ΣJ({code}) = {sum(Jp)}. ✔\n")
open(f'/home/claude/FICHE_OBJET_{code}_GRANULAIRE.md','w',encoding='utf-8').write('\n'.join(g))
print(f"=== {code} {NOM[code]} : 6 fichiers générés ===")
print(f"phrases={iP['n']}  parties={iQ['n']}  Σ={sum(Jp)}  diacrité={DIAC}  (jummal+lettres vérifiés)")
print(f"basmala/ph1 lettres = {' + '.join(chain)} = {cum}")
print("objets par partie :")
for nm,J in groups.items():
    c=poly(J); disp=poly_str(c) if len(J)<=MAXLIST else f"deg {len(J)} (coeffs en CSV)"
    print(f"  {nm:<26} deg {len(J):>3}  trace {sum(J):>7}={facstr(sum(J)):<18} charge {charge(sum(J)):+d}  R(X)={disp}")
print("contrôle Σparties=Σphrases :", sum(Pa),"=",sum(Jp))
