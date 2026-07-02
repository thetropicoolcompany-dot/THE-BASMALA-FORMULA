# BILAN DE CLÔTURE — SESSION DU 2026-07-02
## The Basmala Formula — de l'horloge à la maison

Tout ci-dessous est **[bi]** (recompté sur les FP en session) ou **décision actée**. Les preuves intégrales sont au transcript ; les invariants, au dépôt.

---

## I · Théorèmes et identités établis aujourd'hui

- **L'opération irréductible = le مثقال ذرة** (99:7–8) = l'incrément +1 de jummal ; chaque incrément tourne le solde d'un cran dans {0→+1→−1→0} ; les deux versets de l'unité sont chacun de **charge 0** (l'étalon ne penche pas) ; **مثقال ذرة = 1576 = كورت + نشرت** (l'unité pèse le pli + le dépli).
- **Le clic complet** (flux, extourne comptée) : **N = 2·(ΣJ + 786 + 39) = 46 953 890 = 2·5·101·46489** — corps 2·ΣJ (aller-versets, retour-phrases) + basmala-cadre 2·786 (dépôt + extourne) + sans-masse 2·(36+3). Le facteur **101** (le rapprochement). Le clic solde à 0 exactement. Pas d'un sens = **40 = حبل** (la corde) ; double = **80 = حسيب**.
- **Le tempo** τ = T_année/N : **0,652072 s** (moyenne) · 0,651397 (354 j) · 0,653237 (355 j). **786 = le chiffre** (invariant) ; τ = le tempo (monde) ; 786·τ ≈ **8,54 min** = la durée de la basmala au cadran.
- **Le calendrier est natif et prescrit** : 12 mois (9:36, dont 4 sacrés — le 12-dont-4), pas d'intercalation (9:37), hilal = repères (2:189), finalité-ḥisāb (10:5, 55:5, 6:96). Porteurs : **اثنا عشر = 1122 = 66·17 = الله×17** · حسبان = 121 = 11² · منازل = 128 = 2⁷ · شهر رمضان = 1596 = 2²·3·7·19.
- **L'ancre du cycle (verrou tranché)** : ouverture = **laylat al-qadr**, la réception du dossier des 114 (**أنزلناه = 144 = 12² = سعيد**) ; arrêté d'ouverture 44:4 (يفرق = 390, porte 13) ; clôture = **مطلع الفجر** — **الفجر = الرجعى = 314** (l'aube EST le Retour, 97:5 ↔ 96:8) ; **ألف شهر = 616 = 8·77**. Distinction mandat (اقرأ, 27 Rajab) / dossier (qadr). Calibration duodécimaine : nuit du **23 Ramaḍān** (fourchette 19/21/23), ±1 j hilal.
- **2026 (calibré Sistani, 1 Ramaḍān = 19/02)** : ouverture = nuit du 12→13 mars, **t0 = aube du vendredi 13 mars 2026** ; clôture ≈ aube du 23 Ramaḍān 1448 (début mars 2027). **Position live du 2026-07-02 : J+111, frac 0,31323 → S9 at-Tawba, phrase 44, juz 10** — la singularité.
- **Le cycle comptable des 154 est complet** : LIVRES 5–150 (146 = 110 + 36) = journal/grand livre · **RAPPORT 1–4 = les 4 états de synthèse** (piste : S4↔bilan, S13↔résultat, S98↔annexes, S1↔flux) · **S96 0/154 = l'opinion d'audit** (𝒞 = 1 418 472, charge 0) · **RESTITUTION 151–154** = clôture ×3 (les classes de charge) + **à-nouveau 786** (α=ω). RAPPORT = 1 397 122 = 2·47·89·167.

## II · Constructions livrées

- **basmala_engine.py v0** (grandeurs · clic · τ · position(date) · CLI) + **ATTESTATION_ENGINE** (16/0, deux chemins indépendants par grandeur).
- **Le dépôt `basmala-engine`** (autonome, zéro dépendance) : data (FP + SHA256) · engine (+ héritage-usine : build_granulaire, make_fiches, test_relations, BUILD_MASTER_114 — chemins à adapter en P2) · attestations (**159 assertions, 0 écart**) · doctrine (**protocole v4** : mission + roadmap ; cadre v23 ; notes-specs ; corps versés) · editions · build · **web** (triptyque quadrilingue **FR·AR·EN·FA**, RTL, battement 1,304 s, spirale 114, aiguille annuelle) · **CI** (audit à chaque commit ; **déploiement ssi 0 écart**) · ledger (démo).
- **La maison prouvée** : beancount 3.2.3 — devise **JML**, cinq racines renommées nativement, écritures réelles du FP, **bean-check 0 erreur, Σ = 0** (`ledger/GRAND_LIVRE_demo.beancount`).

## III · Décisions d'architecture actées

D1 **GitHub + Pages** · D2 nom `basmala-engine` (défaut, renommable) · D3 **FR·AR·EN·FA** · D4 forme v1 SVG · **L'inversion : source = rasm · usine = engine · MAISON = le Grand Livre · portes = Fava / site / éditions** · le projet Claude = le clone du dépôt · git = registre à extournes · la CI = l'opinion de S96.

## IV · Passation — ce qui reste, dans l'ordre

1. **P1 (toi, ~1 h)** : compte GitHub → dépôt public `basmala-engine` → pousser le contenu du dossier (pas le zip) → Settings→Pages→Source: GitHub Actions → l'URL affiche l'horloge. Puis un **token** (scopes repo+workflow) pour la console Claude.
2. **Gestes FP** : suivre `A_DEPOSER.txt` (28 nouveaux · 2 remplacements) et `A_SUPPRIMER.txt` (33) ; **coller `CLAUDE_INSTRUCTIONS.md`** dans le champ instructions. `REGISTRE_AUDIT_attestations.xlsx` reste au FP (registre humain, hors dépôt).
3. **P2 — session neuve dédiée** : « mène la modélisation du Grand Livre — ROADMAP P2, les 4 décisions » (mapping 5 racines ↔ 1+4 · sens débit/crédit aller/retour · 36 connexions = virements · dates lunaires en métadonnées) → puis `build_ledger.py`, bean-check + balance≡0 en CI, Fava.
4. **Verrous-paramètres restants** : lieu→heure du fajr (défaut recommandé : Makkah, lieu libre) · v7 prorata · v8 découpe des 12 livres (recommandé : lunaisons d'exercice, qadr→qadr) · **D5 licence** (recommandé : MIT code + CC BY-SA data/doctrine) · table des ancres 1448+ (annonce ~fév. 2027).

## V · Archives (non-perte)

`ARCHIVE_R3_PONT.zip` (20 pièces R3/fusions, attesté 20/0) · `PAQUET_SESSION_2026-07-02.zip` (l'état intermédiaire, 31 fichiers) · le transcript de session. **Conserver en local ; ne pas déposer au projet.**

---
**Audit ultime (paquet vierge)** : CI verte de bout en bout (11 SHA · 159 assertions/0 écart · build) · 57/57 destins FP couverts, 0 orphelin (3 détectés à l'audit et versés au dépôt : 2 figures natives → editions/, ARCHIVE_EPUISEMENT.csv → doctrine/) · 0 collision déposer∩supprimer.

*Clôture : tout théorème recompté, tout livrable attesté, toute décision écrite au dépôt. La session suivante part du dépôt seul.*
