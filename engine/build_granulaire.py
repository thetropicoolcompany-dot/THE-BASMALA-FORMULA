import csv, itertools, unicodedata
from math import comb, gcd
from functools import reduce
ab={'ا':1,'أ':1,'إ':1,'آ':1,'ٱ':1,'ء':1,'ب':2,'ج':3,'د':4,'ه':5,'ة':5,'و':6,'ؤ':6,'ز':7,'ح':8,'ط':9,'ي':10,'ى':10,'ئ':10,'ك':20,'ل':30,'م':40,'ن':50,'س':60,'ع':70,'ف':80,'ص':90,'ق':100,'ر':200,'ش':300,'ت':400,'ث':500,'خ':600,'ذ':700,'ض':800,'ظ':900,'غ':1000}
NOM={'S96':'al-ʿAlaq','S1':'al-Fātiḥa','S4':'an-Nisāʾ','S98':'al-Bayyina','S13':'ar-Raʿd'}
CRIT={'S96':'règle A (ponctuation FR)','S1':'règle A (ponctuation FR)','S98':'règle A (ponctuation FR)','S13':'mixte (forcé/aligné/sélection)','S4':'pauses du rasm (waqf)'}
SMALL=(2,3,5,7,11,13,17,19)
def uname(c):
    try: return unicodedata.name(c)
    except: return f"U+{ord(c):04X}"
HUGE_THRESH=10**25
HUGE_B=10**4
def factor(x, B=10**6):
    n=x; f={}
    b = B if x < HUGE_THRESH else HUGE_B
    d=2
    while d<=b and d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1:
        if n < b*b: f[n]=f.get(n,0)+1   # aucun facteur <= b et n < b^2 => n premier
        else: f['_C']=n                  # grand cofacteur, factorisation non terminee
    return f
def facstr(x):
    if isinstance(x,dict): d=dict(x)
    else: d=factor(x) if x>1 else {}
    co=d.pop('_C',None)
    parts=[f"{p}^{e}" if e>1 else str(p) for p,e in sorted(d.items())]
    if co is not None: parts.append(f"[cofacteur {co} non factorise au-dela de 10^6]")
    return '·'.join(parts) if parts else '1'
def charge(x): r=x%3; return 1 if r==1 else (-1 if r==2 else 0)
def poly(roots):
    c=[1]
    for r in roots:
        new=[0]*(len(c)+1)
        for i,a in enumerate(c): new[i]+=a; new[i+1]+=a*(-r)
        c=new
    return c
def poly_str(c):
    n=len(c)-1; t=[]
    for i,a in enumerate(c):
        d=n-i
        if a==0: continue
        s='+' if a>0 else '−'; av=abs(a); mono='X' if d==1 else (f'X^{d}' if d>1 else ''); coef='' if (av==1 and d>0) else str(av); sep='·' if (coef and mono) else ''
        t.append(f"{s} {coef}{sep}{mono}".strip())
    s=' '.join(t); return (s[2:] if s.startswith('+ ') else s).replace('− ','−')
def euclid(a,b):
    a,b=max(a,b),min(a,b); s=[]
    while b: s.append((a,b,a//b,a%b)); a,b=b,a%b
    return s
def invset(J):
    n=len(J); S=sum(J); g=reduce(gcd,J) if n>1 else J[0]; prod=1
    for j in J: prod*=j
    p1=S; p2=sum(j*j for j in J); p3=sum(j**3 for j in J)
    e2=(S*p1-p2)//2; e3=(p3-S*p2+e2*p1)//3
    primes=set()
    for j in J: primes|=set(factor(j))
    ch=[charge(j) for j in J]
    return dict(n=n,e1=S,e1f=facstr(S),pgcd=g,prim=int(g==1),prod=prod,distinct=len(set(J)),vmin=min(J),vmax=max(J),
        nprimes=len(primes),present=' '.join(str(p) for p in SMALL if p in primes),absent=' '.join(str(p) for p in SMALL if p not in primes) or '∅',
        cpos=ch.count(1),czero=ch.count(0),cneg=ch.count(-1),scharge=ch.count(1)-ch.count(-1),cglob=charge(S),e2=e2,e3=e3,p1=p1,p2=p2,p3=p3)

def build(code, CAP=60):
    rows=list(csv.DictReader(open(f'/home/claude/{code}_phrases_A.csv',encoding='utf-8')))
    Jp=[int(r['jummal']) for r in rows]
    groups={}
    for r in rows: groups.setdefault(r['partie'],[]).append(int(r['jummal']))
    # vecteur parties (sommes, ordre d'apparition)
    seen=[]
    for r in rows:
        if r['partie'] not in [x[0] for x in seen]: seen.append((r['partie'],int(r['partie_jummal'])))
    Pa=[x[1] for x in seen]
    # 1) decomposition lettres
    lr=[]
    for r in rows:
        ph=int(r['phrase']); cum=0; pos=0
        for ch in r['rasm']:
            if ch==' ': lr.append([ph,r['partie'],'','(espace)','SPACE',0,cum]); continue
            v=ab.get(ch,0)
            if v>0: cum+=v; pos+=1
            lr.append([ph,r['partie'],pos if v>0 else '',ch,uname(ch),v,cum])
        assert cum==int(r['jummal']),(code,ph,cum,r['jummal'])
    with open(f'/home/claude/{code}_decomposition_lettres.csv','w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['phrase','partie','rang_lettre','caractere','nom_unicode','valeur_abjad','cumul'])
        for x in lr: w.writerow(x)
    # 2) fonctions symetriques (par partie ; termes explicites si C(m,k)<=CAP)
    sf=[]
    for nm,J in groups.items():
        m=len(J); c=poly(J)
        for k in range(1,m+1):
            ek=((-1)**k)*c[k]; nb=comb(m,k)
            if nb<=CAP:
                termes='  +  '.join('·'.join(map(str,cmb)) for cmb in itertools.combinations(J,k))
            else:
                termes=f"[{nb} termes — calcul par récurrence de Viète, voir polynôme]"
            sf.append([nm,m,k,nb,ek,facstr(ek),termes])
    with open(f'/home/claude/{code}_fonctions_symetriques.csv','w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['partie','degre','k','nb_termes_C(m,k)','e_k','e_k_facteurs','termes_explicites'])
        for x in sf: w.writerow(x)
    # 3) objets niveaux phrases & parties -> invariants + coeffs
    iP=invset(Jp); iQ=invset(Pa); cP=poly(Jp); cQ=poly(Pa)
    ekP=[((-1)**k)*cP[k] for k in range(len(cP))]; ekQ=[((-1)**k)*cQ[k] for k in range(len(cQ))]
    FIELDS=['objet','niveau','n','trace_e1','trace_e1_fac','pgcd','primitif','distinct','vmin','vmax','nprimes','petits_premiers_presents','petits_premiers_absents','charge_pos','charge_zero','charge_neg','somme_charges','charge_globale','p1','p2','p3']
    def row(niv,iv): return [code,niv,iv['n'],iv['e1'],iv['e1f'],iv['pgcd'],iv['prim'],iv['distinct'],iv['vmin'],iv['vmax'],iv['nprimes'],iv['present'],iv['absent'],iv['cpos'],iv['czero'],iv['cneg'],iv['scharge'],iv['cglob'],iv['p1'],iv['p2'],iv['p3']]
    with open(f'/home/claude/{code}_obj_invariants.csv','w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(FIELDS); w.writerow(row('phrases',iP)); w.writerow(row('parties',iQ))
    with open(f'/home/claude/{code}_obj_coeffs.csv','w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['objet','niveau','degre','k','e_k','coeff_X^(n-k)'])
        for k in range(len(cP)): w.writerow([code,'phrases',iP['n'],k,ekP[k],cP[k]])
        for k in range(len(cQ)): w.writerow([code,'parties',iQ['n'],k,ekQ[k],cQ[k]])
    return rows,groups,seen,Jp,Pa,iP,iQ,cP,cQ,lr
