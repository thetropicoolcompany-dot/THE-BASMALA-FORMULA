# -*- coding: utf-8 -*-
"""BUILD_LEDGER — génère ledger/GRAND_LIVRE.beancount depuis les FP (jamais saisi).
Spec : doctrine/NOTE_GRAND_LIVRE.md (les 4 décisions de P2, encodages v1).
Attestation jointe : attestations/ATTESTATION_LEDGER.py (deux chemins indépendants).

Usage : python3 build_ledger.py [--fp DIR] [--annee moyenne|354|355] [--ancre 1447] [--out FICHIER]
La machine ne préjuge pas : elle poste les masses et le cadre ; l'audit est le bean-check.
"""
import sys, csv, os
from datetime import timedelta
from collections import defaultdict

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from basmala_engine import Engine, ANCRES, ANNEES, LUNAISON, _resolve_fp

def hijri(d, ram1):
    """Comput duodécimain par lunaison moyenne depuis 1 Ramadan de l'ancre (±1 j hilal)."""
    dh = (d - ram1).days
    m = int(dh / LUNAISON)
    jour = dh - int(m * LUNAISON)
    mois = ((9 - 1 + m) % 12) + 1
    an = 1447 + (9 - 1 + m) // 12
    return f"{jour}/{mois}/{an} (±1)"

def build(fp=None, annee='moyenne', ancre=1447, out=None):
    fp = fp or _resolve_fp()
    e = Engine(fp)
    T = ANNEES[str(annee)]
    t0 = ANCRES[ancre]
    ram1 = t0 - timedelta(days=22)                    # 1 Ramadan de l'ancre (calibration 23)
    tclot = t0 + timedelta(days=int(T))               # مطلع الفجر suivant (±1 hilal)
    out = out or os.path.normpath(os.path.join(_HERE, '..', 'ledger', 'GRAND_LIVRE.beancount'))

    # ── FP ──
    versets = [(int(r['sourate']), int(r['verset']), int(r['jummal']))
               for r in csv.DictReader(open(os.path.join(fp, '01_DATA_jummal_114_par_verset.csv'), encoding='utf-8'))]
    f = {int(r['sourate']): int(r['pointe_sourate'])
         for r in csv.DictReader(open(os.path.join(fp, '01_DATA_toniques_114_apex_P2.csv'), encoding='utf-8'))}
    aff = defaultdict(list)
    for s, t in sorted(f.items()):
        if t != s:
            aff[t].append(s)
    cibles = sorted(aff)                              # les 36 cibles non-fixes (l'ermite exclu)

    L = []
    A = L.append
    A(';; ================================================================')
    A(';; الكتاب — LE GRAND LIVRE DES COMPTES DU CORAN (The Basmala Formula)')
    A(';; GÉNÉRÉ par engine/build_ledger.py — JAMAIS SAISI. Spec : doctrine/NOTE_GRAND_LIVRE.md')
    A(f';; Exercice {ancre}->{ancre+1} — t0 = aube du 23 Ramadan = {t0} ; clôture = {tclot} (±1 hilal) ; année = {T} j')
    A(';; D1 — les 5 familles = S96 + les 4 témoins :')
    A(';;   Assets      = Registre     <-> S98 البينة   (+1=+1)  كتب قيمة (98:3)')
    A(';;   Liabilities = Contrepartie <-> S96 العلق    (-1=-1)  اقرأ = 2·(يوم الدين), la dette de lecture')
    A(';;   Equity      = Source       <-> S13 الرعد    (0, rôle) أم الكتاب (13:39), le siège du 0, α=ω')
    A(';;   Income      = Revelation   <-> S4  النساء   (-1=-1)  تنزيل témoigné (4:105, 4:166)')
    A(';;   Expenses    = Lecture      <-> S1  الفاتحة  (+1=+1)  يوم الدين (1:4)')
    A(';; La machine poste ; l’audit est le bean-check (opinion 0/154 = la CI).')
    A(';; ================================================================')
    A('option "title" "الكتاب — Le Grand Livre des Comptes du Coran"')
    A('option "operating_currency" "JML"')
    A('option "name_assets" "Registre"')
    A('option "name_liabilities" "Contrepartie"')
    A('option "name_equity" "Source"')
    A('option "name_income" "Revelation"')
    A('option "name_expenses" "Lecture"')
    A('')
    A(f'{t0} open Source:Basmala-Cadre JML')
    A(f'{t0} open Revelation:Tanzil JML')
    A(f'{t0} open Lecture:Recitation JML')
    A(f'{t0} open Contrepartie:DetteDeLecture JML')
    for s in range(1, 115):
        A(f'{t0} open Registre:S{s:03d} JML')
    A('')

    # ── t0 · l’inspire, ordre §∴ : +36 connexions → +3 brins → +1 à-nouveau 786 ──
    A(';; ── INSPIRE (t0) : +36 connexions → +3 brins (souffle) → +1 à-nouveau 786 (§∴) ──')
    for t in cibles:
        k = len(aff[t])
        A(f'{t0} * "CONNEXION — cible S{t:03d}, {k} affluent{"s" if k > 1 else ""} (1 JML/arête, sans-masse du clic)"')
        A(f'  Registre:S{t:03d}  {k} JML')
        for s in aff[t]:
            A(f'  Registre:S{s:03d}  -1 JML')
        A('')
    for num, brin in ((151, '-1'), (152, '+1'), (153, '0')):
        A(f'{t0} * "SOUFFLE — brin {brin} [N°{num}] (1 JML, sans-masse du clic)"')
        A('  Registre:S001  1 JML')
        A('  Source:Basmala-Cadre  -1 JML')
        A('')
    A(f'{t0} * "A-NOUVEAU 786 — la basmala-cadre (α) [N°154] ; أنزلناه = 144 = 12²"')
    A('  Registre:S001  786 JML')
    A('  Source:Basmala-Cadre  -786 JML')
    A('')

    # ── t0 · l’aller : la réception du dossier des 114 (6236 versets) ──
    A(';; ── ALLER (t0) : TANZIL — la réception du dossier des 114 (laylat al-qadr) ──')
    for s, v, j in versets:
        A(f'{t0} * "TANZIL S{s:03d}:{v}"')
        A(f'  Registre:S{s:03d}  {j} JML')
        A(f'  Revelation:Tanzil  {-j} JML')
    A('')

    # ── l’année · le retour : la lecture, phrase par phrase, datée par l’horloge ──
    A(';; ── RETOUR (l’année) : QIRAA — la remise du registre, phrase par phrase ──')
    for r in e.phr:
        s, p, j = int(r['sourate']), int(r['phrase']), int(r['jummal'])
        fr = float(r['frac_debut'])
        d = t0 + timedelta(days=int(fr * T))
        bas = ' — basmala' if r['is_basmala'] == '1' else ''
        A(f'{d} * "QIRAA S{s:03d} phrase {p}{bas}"')
        A(f'  fraction: "{fr:.5f}"')
        A(f'  hijri: "{hijri(d, ram1)}"')
        A(f'  Lecture:Recitation  {j} JML')
        A(f'  Registre:S{s:03d}  {-j} JML')
    A('')

    # ── t_clôture · l’expire, ordre §∴ : extourne 786 → −3 brins → −36 connexions ──
    A(';; ── EXPIRE (clôture) : extourne 786 → −3 brins → −36 connexions (§∴) ──')
    A(f'{tclot} * "EXTOURNE A-NOUVEAU 786 — la basmala-cadre (ω) [N°154] ; مطلع الفجر"')
    A('  Registre:S001  -786 JML')
    A('  Source:Basmala-Cadre  786 JML')
    A('')
    for num, brin in ((153, '0'), (152, '+1'), (151, '-1')):
        A(f'{tclot} * "EXTOURNE SOUFFLE — brin {brin} [N°{num}]"')
        A('  Registre:S001  -1 JML')
        A('  Source:Basmala-Cadre  1 JML')
        A('')
    for t in reversed(cibles):
        k = len(aff[t])
        A(f'{tclot} * "EXTOURNE CONNEXION — cible S{t:03d}, {k} affluent{"s" if k > 1 else ""}"')
        A(f'  Registre:S{t:03d}  {-k} JML')
        for s in aff[t]:
            A(f'  Registre:S{s:03d}  1 JML')
        A('')

    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    return out, dict(versets=len(versets), phrases=len(e.phr), cibles=len(cibles),
                     affluents=sum(len(v) for v in aff.values()), t0=str(t0), tclot=str(tclot), annee=str(annee))

if __name__ == '__main__':
    args = sys.argv[1:]
    def opt(name, default=None):
        return args[args.index(name) + 1] if name in args else default
    out, info = build(fp=opt('--fp'), annee=opt('--annee', 'moyenne'),
                      ancre=int(opt('--ancre', '1447')), out=opt('--out'))
    print(f"GRAND LIVRE généré : {out}")
    print(f"  {info['versets']} pièces-aller (TANZIL, t0={info['t0']}) · {info['phrases']} pièces-retour (QIRAA)"
          f" · {info['cibles']} connexions ({info['affluents']} arêtes) · brins 3+3 · 786 ×2 · clôture {info['tclot']} · année {info['annee']}")
