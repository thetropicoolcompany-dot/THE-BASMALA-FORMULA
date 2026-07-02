# The Basmala Formula — Ḥisāb al-Qurʾān
**FR** · L'ordinateur basmala : le registre coranique qui se recompte, s'atteste (159 assertions, 0 écart) et s'affiche — l'horloge comptable annuelle (ouverture : aube du 23 Ramaḍān, calibration duodécimaine).
**AR** · حاسوب البسملة: سجلّ القرآن يعيد حسابه ويثبته ويعرضه — ساعة محاسبية سنوية (الافتتاح: مطلع فجر ٢٣ رمضان).
**EN** · The basmala computer: the Qur'anic ledger that recomputes, attests (159 assertions, 0 discrepancy) and displays itself — the annual accounting clock (opening: dawn of 23 Ramaḍān, Twelver calibration).
**FA** · رایانهٔ بسم‌الله: دفترِ قرآن که خود را بازشماری، گواهی و نمایش می‌دهد — ساعت حسابداری سالانه (گشایش: سپیده‌دم ۲۳ رمضان).

## Quickstart
```bash
python3 engine/basmala_engine.py position            # la position du registre aujourd'hui
python3 engine/basmala_engine.py grandeurs           # 332 837 lettres · 23 476 120 jummal…
for a in attestations/ATTESTATION_*.py; do python3 $a; done   # l'audit complet
python3 -m http.server -d web 8000   # tester localement, puis http://localhost:8000
python3 build/build_site.py                          # régénère web/data/*.json
```
Site : `web/index.html` (statique, quadrilingue FR·AR·EN·FA, calcul côté client). CI : chaque commit relance l'audit ; **déploiement seulement si 0 écart**.

## Couches
`data/` FP sources (SHA256) · `engine/` le moteur · `attestations/` la partie double computationnelle · `doctrine/` protocole + cadre + notes-specs · `editions/` productions LaTeX · `build/` génération · `web/` le triptyque conte·balance·forme.

Doctrine complète : `doctrine/00_PROTOCOLE.md` (v4). Licence : à décider (D5).
