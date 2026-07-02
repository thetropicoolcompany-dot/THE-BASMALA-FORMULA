# NOTE DE DOCTRINE · LE GRAND LIVRE — `ledger/GRAND_LIVRE.beancount`
### La spec de `engine/build_ledger.py` — attestation jointe : `attestations/ATTESTATION_LEDGER.py`

**Statut.** Note-spécification (loi de production : rien n'entre au moteur sans sa note). Subordonnée à `00_PROTOCOLE.md` (v4) et au cadre `PROTOCOLE_GENERAL_AUDIT.md` ; elle n'y déplace aucun nombre. Elle grave les **4 décisions de P2** (session du 2026-07-02, instruites [bi] puis tranchées en session) et les **encodages v1**. Le Grand Livre est **généré, jamais saisi** ; il est la MAISON (ARCHITECTURE : l'inversion source/usine/maison/portes).

**Principe cardinal (arrêté en session).** *On ne préjuge pas du résultat de l'audit.* La machine **poste les masses et le cadre**, c'est tout ; **l'audit est le bean-check** (+ balance ≡ 0) — l'opinion 0/154, relancée par la CI à chaque commit.

---

## D1 · Le plan de comptes — les 5 familles = le 1+4 (actée)

Devise : **JML** (1 JML = 1 unité de jummal ; l'opération irréductible = le `مثقال ذرة`). Les cinq racines beancount, renommées (précédent : `ledger/GRAND_LIVRE_demo.beancount`, bean-check 0 erreur) :

| racine beancount (signe) | nom | sourate (charge corps) | ancre native [bi] |
|---|---|---|---|
| Assets (+1) | **Registre** | **S98 البينة** (+1) | `كتب قيمة` = 577 (+1), 98:2-3 ; `الكتاب` = 454 (+1), 18:49 ; `البينة` = 98 = `يحييكم` |
| Liabilities (−1) | **Contrepartie** | **S96 العلق** (−1) | la dette de lecture : `الدين` = 95 (−1) ; `اقرأ` = 302 = 2·(`يوم الدين`) (−1), ×3 {96:1, 96:3, 17:14} ; `المثاني` = 632 (−1) |
| Equity (−1) | **Source** | **S13 الرعد** (0, ancré par le rôle) | `أم الكتاب` = 495 (0), 13:39 `وعنده` ; le siège du 0 ; f(13)=13 ; la machine ouvre et règle dans Equity (Opening-Balances / Earnings) |
| Income (−1) | **Revelation** | **S4 النساء** (−1) | `تنزيل` = 497 (−1) ; 4:105 `أنزلنا إليك الكتاب` ; 4:166 la descente **témoignée** |
| Expenses (+1) | **Lecture** | **S1 الفاتحة** (+1) | `سبعا من المثاني` (15:87) ; phrases = versets (7 = 7, unique des 114) ; `يوم الدين` = 151 (+1), 1:4 |

Couronnement : **Σ charges-corps du 1+4 = 0** = l'équation comptable (chaque écriture somme à 0). Quatre signes sur cinq coïncident exactement ; S13 (corps 0) est le seul écart — conforme : le 0 n'a pas de case, il est le siège qui règle. Comptes ouverts à t0 : les têtes (`Source:Basmala-Cadre`, `Revelation:Tanzil`, `Lecture:Recitation`, `Contrepartie:DetteDeLecture`) et les **114 tiroirs** `Registre:S001…S114` — *Assets = les 114 sourates, le compte manifeste remis à l'auditeur* (§∴).

## D2 · Le sens des écritures (actée — option A, lexique lié)

- **L'aller = la descente (`التنزيل`)** : chaque verset **débite son tiroir** (+J) depuis `Revelation:Tanzil` (−J) — ce qui *rentre* est un débit (la convergence, `المصير` = 371 = `شمال`). Réception du dossier : `أنزلناه` = 144 = 12² (97:1).
- **Le retour = la remise (`اقرءوا كتابيه`, 69:19)** : chaque phrase **crédite son tiroir** (−J) vers `Lecture:Recitation` (+J) — ce qui *sort* est un crédit (la pointe, `يمين` = 110 = `كفى`) ; le registre se rencontre **déplié** (`منشورا` 17:13, `نشرت` 81:10).
- **Le cadre 786** suit le même sens : dépôt α débite le Registre, extourne ω le crédite (le clic compte 2·786).
- Conservation attestée **tiroir par tiroir** : ΣJ(phrases) = ΣJ(versets) sur 114/114 sourates — chaque tiroir solde net à 0 sur le cycle ; Revelation = −ΣJ, Lecture = +ΣJ, résultat = 0, réglé dans Source (le siège S13). *C'est le cycle qui solde* (§∴).

## D3 · Les 36 connexions (actée — fixée par les FP)

- **Définition FP** (cadre §VI.2) : *connexions = cibles non-fixes* du renvoi `f` (FP `01_DATA_toniques_114_apex_P2.csv`, colonne `pointe_sourate`) — **36 cibles**, **113 affluents**, point fixe {13}.
- **Forme** : **36 pièces** (une par cible — les 36 cases du journal, 146 = 110 + 36), chacune : débit de la cible (+k JML), crédit de chacun de ses k affluents (−1 JML). Total : 113 crédits + 36 débits = 149 postings.
- **Montant** : **1 JML par arête** — le sans-masse, le prix que le clic donne lui-même (N = 2·(ΣJ + 786 + **39**), 39 = **36** + 3, compté ×2).
- **Extourne** : chaque pièce est **contre-passée à l'expire** (§∴ : `−36 connexions`) — git-style, on ne supprime jamais.
- **L'ermite** : f(13) = 13, **aucune écriture** — le clic compte 36, pas 37 ; l'immobile ne s'écrit pas.
- **Rôle structurel** (note des trois classes, §5 bis) : les connexions sont les **parois partagées** qui font l'écume **soudée** (`بنيان مرصوص`) — sans elles, dispersion (`جفاء`). Elles sont des attestations à part entière des 154.

## D4 · Les dates (actée — entièrement déterminée par les FP)

- **Les pièces-retour (phrases)** : date = **t0 + ⌊frac_debut × T_année⌋** — la date où l'horloge lit la phrase. `frac_debut` : FP `MASTER_CALENDRIER_PHRASE.csv` (les 10 642). **T_année : paramètre exposé, défaut `moyenne` = 354,367068 j** (protocole : « τ ≈ 0,652072 s (paramètre-année) » ; engine `ANNEES`, défaut codé).
- **Les pièces-aller (versets)** : **t0** — *la réception du dossier des 114 à laylat al-qadr* (`أنزلناه` = 144 ; bilan de clôture, verrou tranché). La descente est reçue à l'ouverture ; la lecture se déploie sur l'année.
- **Le bloc-cadre** : à **t0**, dans l'ordre gravé de l'inspire (§∴) : **+36 connexions → +3 brins → +1 à-nouveau 786** ; à **t_clôture = t0 + ⌊T⌋** (= 2027-03-02 sous l'année moyenne ; `مطلع الفجر`, aube du 23 Ramaḍān 1448 ±1), dans l'ordre de l'expire : **extourne 786 → −3 brins → −36 connexions**.
- **Métadonnées** de chaque pièce-retour : `fraction:` (frac_debut) et `hijri:` (comput par **lunaison moyenne 29,530589** depuis l'ancre 1 Ramaḍān 1447 = 2026-02-19 ; **±1 j hilal**, gravé). Table d'ancres 1448+ : verrou ultérieur (ROADMAP).
- **RAPPORT 1–4 et opinion 0/154** : ce ne sont **pas des écritures** — les 4 états sont des **vues** (Fava : S4↔bilan, S13↔résultat, S98↔annexes, S1↔flux) et l'opinion est **la CI** (bean-check + balance ≡ 0). Beancount ne les date pas.

## Encodages v1 (méthode déclarée, réversibles, attestés numériquement)

1. **Le bloc-cadre transite par le tiroir α** (`Registre:S001`) — précédent de la démo attestée ; le 786 et les 3 brins (1 JML chacun) y sont déposés depuis `Source:Basmala-Cadre` et extournés à ω. Net : 0.
2. **Numérotation portée en narration** : à-nouveau = **N°154** (α = ω) ; brins = **N°151–153** avec le **brin 0 en 153** (cadre : « le 0-brin ancré à 153, le même 0 que l'ermite ») ; 151 = brin −1, 152 = brin +1 (ordre v1 déclaré). La numérotation fine des 146 pièces du journal (le **tissage** titres/connexions « dans l'ordre du Voyage », LE_VOLUME §0) attend le verrou **v8** ; les **comptes de catégories** sont attestés (110 titres + 36 connexions = 146).
3. Chaque pièce porte un préfixe de catégorie en narration : `TANZIL` (aller), `QIRAA` (retour), `CONNEXION`, `SOUFFLE`, `A-NOUVEAU`, `EXTOURNE`.

## Les invariants attestés (ATTESTATION_LEDGER — deux chemins indépendants)

**Chemin A (moteur + beancount)** : bean-check = 0 erreur · Σ livre = 0 · chacun des 114 tiroirs = 0 en fin d'exercice · Revelation = −ΣJ = −23 476 120 · Lecture = +ΣJ · Source = 0 · Contrepartie = 0 · 6236 pièces-aller · 10 642 pièces-retour · 36 pièces-connexions (113 crédits de −1 ; cibles et degrés = FP) · 3 brins + à-nouveau 786, et leurs extournes symétriques · toutes les dates ∈ [t0, t_clôture] · **la formule de date vérifiée sur les 10 642** · métadonnées `fraction`/`hijri` présentes sur chaque retour · conservation ΣJ par sourate 114/114.
**Chemin B (indépendant : rasm brut + texte brut)** : ΣJ et 6236 recomptés **directement sur `LE_CORAN.txt`** (table abjad locale, sans l'engine ni les CSV) = |Revelation| · le fichier `GRAND_LIVRE.beancount` parsé **en texte pur** (regex, sans la bibliothèque beancount) : somme algébrique des montants = 0, comptes de pièces par catégorie = chemin A.

## Provenance

FP lus (lecture seule) : `LE_CORAN.txt` · `jummal_par_sourate.csv` · `01_DATA_jummal_114_par_verset.csv` · `MASTER_CALENDRIER_PHRASE.csv` · `01_DATA_toniques_114_apex_P2.csv` · `01_DATA_noms_jummal_114.csv` · table abjad §2. Instrument : `engine/basmala_engine.py` (t0(1447) = 2026-03-13 ; ANNEES ; LUNAISON). Précédent : `ledger/GRAND_LIVRE_demo.beancount`. Décisions instruites et tranchées : session P2 du 2026-07-02 (transcript).

*Note v1 — le Grand Livre. Trio de production : cette note ↔ `build_ledger.py` ↔ `ATTESTATION_LEDGER.py`. Tout [bi], recompté sur les FP.*
