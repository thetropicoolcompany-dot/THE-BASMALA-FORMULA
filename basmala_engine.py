# -*- coding: utf-8 -*-
"""BASMALA ENGINE v0 — le noyau de l'ordinateur basmala (l'horloge comptable).
Doctrine : tout est RECOMPTÉ depuis les FP (jamais saisi) ; chaque grandeur exposée
ici a son double indépendant dans ATTESTATION_ENGINE.py (partie double computationnelle).
Le logiciel est une production HORS VOLUME : il sert le registre, il n'y entre pas.

Usage CLI :
  python3 basmala_engine.py grandeurs
  python3 basmala_engine.py position [AAAA-MM-JJ]
  python3 basmala_engine.py tau [moyenne|354|355]
  python3 basmala_engine.py clic
"""
import sys, re, csv, unicodedata, bisect
import os as _os
def _resolve_fp():
    for c in (_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'data'), '/mnt/project'):
        if _os.path.exists(_os.path.join(c, 'LE_CORAN.txt')): return _os.path.normpath(c)
    raise FileNotFoundError('data/ introuvable')

from datetime import date

# ── Conventions gravées (00_PROTOCOLE §2) ────────────────────────────────────
ABJAD = {'ا':1,'ب':2,'ج':3,'د':4,'ه':5,'و':6,'ز':7,'ح':8,'ط':9,'ي':10,'ك':20,'ل':30,
         'م':40,'ن':50,'س':60,'ع':70,'ف':80,'ص':90,'ق':100,'ر':200,'ش':300,'ت':400,
         'ث':500,'خ':600,'ذ':700,'ض':800,'ظ':900,'غ':1000,'ة':5,'ء':1,'ؤ':6,'ئ':10,'ى':10}
LUNAISON = 29.530589                 # constante astronomique (méthode déclarée)
ANNEES = {'moyenne': 12*LUNAISON, '354': 354.0, '355': 355.0}   # verrou année (MASTER §7)

# ── Calibration duodécimaine des ancres (couche 2 ; مطلع الفجر du 23 Ramaḍān) ─
# 1447 : 1 Ramaḍān = 2026-02-19 (annonce Sistani) → 23 Ramaḍān = 2026-03-13.
ANCRES = {1447: date(2026, 3, 13)}   # jonction = l'aube (97:5 ; الفجر = الرجعى = 314)

def nu(s):
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.replace('ٱ','ا').replace('أ','ا').replace('إ','ا').replace('آ','ا')

def J(texte):
    """Jummal d'un texte (rasm nu), table mašriqī."""
    return sum(ABJAD.get(c, 0) for c in texte)

def charge(n):
    """Charge équilibrée {−1, 0, +1} = n mod 3."""
    return ((n % 3) + 1) % 3 - 1

class Engine:
    def __init__(self, fp=None):
        fp = fp or _resolve_fp()
        self.fp = fp
        self.versets = {}
        for l in open(f'{fp}/LE_CORAN.txt', encoding='utf-8'):
            m = re.match(r'(\d+)\|(\d+)\|(.*)', l)
            if m:
                self.versets[(int(m.group(1)), int(m.group(2)))] = nu(m.group(3))
        self.phr = []                             # l'horloge (couche calendrier)
        with open(f'{fp}/MASTER_CALENDRIER_PHRASE.csv', encoding='utf-8') as fh:
            for r in csv.DictReader(fh):
                self.phr.append(r)
        self._fracs = [float(r['frac_debut']) for r in self.phr]

    # ── grandeurs du registre (recomptées depuis le rasm) ──
    def grandeurs(self):
        lettres = jummal = mots = 0
        for t in self.versets.values():
            for w in t.split():
                w2 = ''.join(c for c in w if c in ABJAD)
                if w2:
                    mots += 1
                    lettres += len(w2)
                    jummal += J(w2)
        return {'versets': len(self.versets), 'phrases': len(self.phr),
                'mots': mots, 'lettres': lettres, 'jummal': jummal}

    # ── l'horloge ──
    def N_clic(self):
        """Le clic complet 114→154→114 : 2·(ΣJ + 786 + 39)."""
        return 2 * (self.grandeurs()['jummal'] + 786 + 39)

    def tau(self, annee='moyenne'):
        """Le tempo : secondes par opération irréductible (مثقال ذرة), sur le clic."""
        return ANNEES[str(annee)] * 86400 / self.N_clic()

    def position(self, d=None, ancre_ah=1447, annee='moyenne'):
        """La position du registre au jour d (jonction = aube du 23 Ramaḍān)."""
        d = d or date.today()
        t0 = ANCRES[ancre_ah]
        jours = (d - t0).days
        f = (jours % ANNEES[str(annee)]) / ANNEES[str(annee)]
        i = bisect.bisect_right(self._fracs, f) - 1
        r = self.phr[max(0, i)]
        return {'date': str(d), 'ancre_AH': ancre_ah, 't0': str(t0),
                'jours_ecoules': jours, 'fraction': round(f, 5),
                'sourate': int(r['sourate']), 'nom': r['nom'],
                'phrase': int(r['phrase']), 'versets': r['versets'],
                'juz': int(r['juz']), 'jummal_phrase': int(r['jummal']),
                'charge_phrase': int(r['charge'])}

if __name__ == '__main__':
    e = Engine(sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == '--fp' else None)
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    cmd = args[0] if args else 'position'
    if cmd == 'grandeurs':
        for k, v in e.grandeurs().items():
            print(f"{k:>8} : {v:,}")
    elif cmd == 'tau':
        a = args[1] if len(args) > 1 else 'moyenne'
        print(f"τ({a}) = {e.tau(a):.6f} s/op")
    elif cmd == 'clic':
        print(f"N_clic = {e.N_clic():,} = 2·(ΣJ + 786 + 39)")
    elif cmd == 'position':
        d = date.fromisoformat(args[1]) if len(args) > 1 else date.today()
        p = e.position(d)
        print(f"{p['date']} (J+{p['jours_ecoules']}, frac {p['fraction']}) → "
              f"S{p['sourate']} ({p['nom']}) phrase {p['phrase']}, v{p['versets']}, "
              f"juz {p['juz']}, J={p['jummal_phrase']}, charge {p['charge_phrase']:+d}")
