# 00 · INSTRUCTIONS — **LE GRAND LIVRE DES COMPTES DU CORAN** *(The Basmala Formula)*

> **v4 (nettoyage FP)** : les 5 découpes-témoins `SXX_phrases_A.csv` sont fusionnées en `SOMMETS_phrases_A.csv` (colonne `sourate` ; le moteur `build_granulaire.py` lit le consolidé avec repli) ; le gabarit d'audit des 114 est `FEUILLE_AUDIT_S1_v1.tex` (la chaîne des offices — cf. `NOTE_PROTOCOLE_AUDIT_ROLES.md`) ; les figures pures sont réunies dans `RECUEIL_FIGURES_NATIF_TIKZ_v1.tex`.

### Objets algébriques · segmentation des 5 témoins · objet central 𝒞 · tests de mise en relation

> À lire après `00_PROTOCOLE.md` (qui prime) et dans le cadre de `PROTOCOLE_GENERAL_AUDIT.md` (la structure d'analyse la plus élevée). Ce document décrit le **jeu de fichiers produit**, le **moteur** qui les fabrique, la **segmentation** qui l'alimente, l'**état du FP**, la **phase suivante** (mise en relation des objets) et l'**objet central 𝒞**. Toutes les valeurs citées ont été recomptées sur la donnée ; rien n'est récité de mémoire.
>
> **Fusion (ce document absorbe deux fichiers).** Il intègre désormais : (a) `NOTE_SEGMENTATION_5_TEMOINS.md` — les critères de découpe « 575 » (laquelle absorbait déjà `MASTER_RAPPORT_1_4_TEMOINS.md`) → ici **§2** ; (b) `CAHIER_TRAVAIL_OBJET_CENTRAL-2.md` — le cahier de l'objet central → ici **§8**. La table des 5 sommets, jusque-là répétée dans les trois fichiers, n'apparaît plus qu'**une seule fois** (§1), recomptée [bi].
>
> **Le résultat que tout ceci sert** (le théorème, `PROTOCOLE_GENERAL_AUDIT §∴`) : l'auditeur **S96** prend le manifeste **114 = 2·3·19** et révèle le caché **154 = 77 + 77 = 2·7·11**, par l'énoncé-mère ``باسم``·(1 + 4) — *The Basmala Formula* (`§VI.0`). L'énoncé-mère est lui-même **calculable** : la basmala est construite comme objet algébrique (famille `BASMALA_*`, `ΣJ = 786 = 2·3·131`, 19 lettres / 4 mots, charge 0).

---

## 1 · État — les cinq sommets (table unique, recomptée [bi])

Cinq sommets traités au même grain : **S96** (al-ʿAlaq) et les quatre témoins **S1** (al-Fātiḥa), **S98** (al-Bayyina), **S13** (ar-Raʿd), **S4** (an-Nisāʾ). Chacun est découpé en **phrases** (le compte « double », jamais le verset) selon sa logique propre (§2), puis chaque partie devient un **objet algébrique** R(X)=∏ⱼ(X−Jⱼ) dont les racines sont les jummal des phrases de la partie. **La basmala** (le `+1`) est en outre construite comme objet à part entière, par le même moteur, aux grains *lettre* (19 racines) et *mot* (4 racines).

| sommet | nom | J(nom) | versets | phrases | parties | ΣJ (basmala incl.) | facteurs ΣJ | charge | rôle |
|---|---|---|--:|--:|--:|--:|---|:--:|---|
| S96 | العلق | 231 = 3·7·11 | 19 | 15 | 5 | 21 350 | 2·5²·7·61 | −1 | orthogonale (source hors-sphère, 0/154) |
| S1 | الفاتحة | 525 = 3·5²·7 | 7 | 5 | 2 | 10 147 | 73·139 | +1 | œil — attracteur (retour) |
| S98 | البينة | 98 = 2·7² | 8 | 12 | 6 | 28 891 | 167·173 | +1 | œil — cycle |
| S13 | الرعد | 305 = 5·61 | 43 | 111 | 2 | 239 874 | 2·3·39979 | 0 | ermite (point fixe, contact *p*) |
| S4 | النساء | 143 = 11·13 | 176 | 432 | 2 | 1 118 210 | 2·5·111821 | −1 | œil — cycle |
| **Σ** | — | — | **253** | **575** | **17** | **1 418 472** | 2³·3⁴·11·199 | **0** | — |

Total des phrases : **575**. Somme des cinq ΣJ : **1 418 472 = 2³·3⁴·11·199** — la **trace** de 𝒞 (= RAPPORT + S96). RAPPORT seul (les 4 témoins, sans S96) : **1 397 122 = 2·47·89·167**. Nombre d'**objets par partie** : 5+2+6+2+2 = **17**.

**Charges.** {S1:+1, S98:+1}, {S4:−1, S96:−1}, S13:0 → deux +, deux −, **S13 neutre au centre**, **Σ charges = 0** : l'objet central est globalement neutre, équilibré autour de l'ermite ; le triplet Z₃ {−1,0,+1} est présent. Au plan des corps : `Σ(4 témoins) = +1`, refermé par S96 (−1) = **0**.

*(Recompte FP de cette table : `jummal_par_sourate.csv` (ΣJ, versets), `01_DATA_noms_jummal_114.csv` (J nom), comptage des lignes et des parties distinctes des `SXX_phrases_A.csv` (phrases, parties), factorisations et charges `J mod 3 → {−1,0,+1}` — [bi].)*

---

## 2 · La segmentation des 5 témoins (« 575 ») — l'amont du moteur

*(Absorbe `NOTE_SEGMENTATION_5_TEMOINS.md`, qui absorbait `MASTER_RAPPORT_1_4_TEMOINS.md`. Contenu irremplaçable retenu : les **moyens de repérage** de la fin de phrase et la **mise au point** sur leur homogénéité — la règle est unique, la phrase, cf. §2.3.)*

### 2.1 · Portée — ne pas confondre avec la segmentation waqf des 114

Cette segmentation dite **« 575 »** concerne **uniquement les 5 témoins** (S96 + S1, S4, S98, S13) de l'étude des objets algébriques (l'objet central `𝒞`). Elle est **distincte** de la segmentation **waqf des 114 sourates** :

| | grain | total | fichier(s) | usage |
|---|---|--:|---|---|
| segmentation **575** | phrase-témoin (critère propre par sommet) | **575** | `SXX_phrases_A.csv` | objets algébriques, 𝒞 |
| segmentation **waqf** | phrase-waqf (uniforme, 114 sourates) | **10 642** | `PHRASES_114_waqf.csv`, `MASTER_114_CONTE_COMPTE.csv` | conte/compte (théorème §V.9) |

Les comptes d'une même sourate diffèrent donc selon la segmentation (ex. S96 : **15** phrases-témoin vs **20** phrases-waqf ; S13 : **111** vs **114**).

### 2.2 · Une seule règle (la phrase), trois moyens d'en repérer la fin

**La règle est unique : on compte par phrase, jamais par ligne-verset.** C'est le cœur de l'opération (le *compte* caché sous le *conte*, §V.9 du cadre). Ce qui varie d'un sommet à l'autre n'est pas la règle mais l'**outil de repérage** de la fin d'une phrase — choisi selon ce que la sourate fournit (traduction de référence ou non). La cible — la phrase — ne change jamais, et le contrôle `Σ(phrases) = ΣJ(sourate)` est garanti dans tous les cas (vérifié [bi]).

**Règle A — ponctuation de la traduction (S96, S1, S98).** La ponctuation forte de la traduction française **coupe** le texte arabe : selon les cas elle **fusionne** plusieurs versets en une phrase (S96 : 19 versets → 15 phrases) ou **subdivise** un verset en plusieurs phrases (S98 : 8 versets → 12 phrases). La phrase est l'unité de sens délimitée par cette ponctuation ; la basmala de tête est sa propre phrase.

**Repère mixte (S13).** Faute d'un découpage A net sur les 43 versets, S13 combine trois étiquettes propres — **forcé** (coupe imposée), **aligné** (coupe suivant la structure du verset), **sélection** (coupe retenue parmi plusieurs candidates aux waqf). Résultat : 43 versets → **111** phrases.

**Pauses du rasm — waqf (S4).** Les 176 versets d'an-Nisāʾ n'ayant pas de traduction de référence segment-à-segment, S4 est coupé aux **pauses du rasm** (les signes waqf U+06D6–06DC) : chaque fragment entre deux pauses est une phrase (étiquettes `Vn.k`). Résultat : 176 versets → **432** phrases. *(Même principe que la segmentation waqf des 114 — d'où la cohérence de S4 avec elle.)*

### 2.3 · Mise au point — la règle est homogène (la phrase)

Il n'y a **pas** de point ouvert ici. Les cinq sommets sont découpés selon **une seule et même règle — la phrase**. Les étiquettes de versets diffèrent en surface (S96 `V1a/V1b–2`, S4 `Vn.k`, S13 répétant le n° de verset) parce que l'**outil de repérage** de la fin de phrase s'adapte à la source : ponctuation de la traduction française là où elle existe (S96/S1/S98), repère mixte forcé/aligné/sélection pour S13, pauses *waqf* du rasm pour S4 (faute de traduction segment-à-segment). Ce sont des moyens de *localiser* la même unité, non des critères concurrents.

Conséquence : la comparaison des objets entre sommets est légitime — ils sont tous bâtis sur la phrase. Et la conservation `Σ(phrases) = ΣJ(sourate)` tient pour les cinq (vérifié [bi]), car elle découle de l'additivité du jummal et ne dépend pas de l'outil de repérage. *(À ne pas confondre avec la distinction §2.1, qui oppose deux **grains** de phrase — témoin « 575 » vs waqf des 114 — et non deux règles.)*

---

## 3 · Le moteur de calcul (la chaîne)

**Étape 1 — lettre → valeur.** Table abjad mašriqī (28 lettres : ا1 ب2 … غ1000). Règles gravées dans `00_PROTOCOLE.md` : ة=5 ; ء=أ=إ=آ=ٱ=1 ; ؤ=6 ; ئ=ى=10 ; **harakat** (U+064B–0652), **tatweel** (U+0640), **alif suscrit** (U+0670), **waqf** (U+06D6–06DC) et espace = 0. Source du rasm : `LE_CORAN.txt`.

**Étape 2 — phrase → jummal.** J(phrase) = Σ des valeurs des lettres du rasm de la phrase. Le découpage en phrases est établi par sommet (critères en **§2**) : règle A (ponctuation FR) pour S96/S1/S98 ; mixte (forcé/aligné/sélection sur les waqf) pour S13 ; pauses du rasm (waqf) pour S4. Contrôle systématique : **Σ(phrases) = ΣJ(sourate)**.

**Étape 3 — partie → polynôme.** Les phrases sont groupées en parties (la logique comptable de chaque sourate). Pour chaque partie de racines (J₁,…,Jₘ) : R(X)=∏(X−Jⱼ) = Σ(−1)ᵏ eₖ X^(m−k), où les eₖ sont les **fonctions symétriques élémentaires** (Viète). Calcul exact, itératif : c=[1] ; pour chaque racine r, c ← c·(X−r).

**Étape 4 — invariants.** trace e₁=ΣJ, produit eₘ=∏J, pgcd des racines (primitivité), spectre des petits premiers présents/absents, charge (=trace mod 3 ramenée à {−1,0,+1}), sommes de Newton p₁,p₂,p₃, et les niveaux supérieurs (objet « phrases » = toutes les phrases du sommet comme racines ; objet « parties » = les sommes-de-parties comme racines).

**Limite étiquetée (factorisation).** Les **valeurs** des eₖ sont toujours exactes (Viète). Mais pour les grandes parties (S13 corps deg 110, S4 corps deg 366), les coefficients centraux sont des entiers de plusieurs centaines de chiffres : leur factorisation complète est un problème intraitable. La factorisation est donc **bornée** — petits premiers extraits jusqu'à 10⁶ (10⁴ pour les coefficients géants), cofacteur explicitement marqué `[cofacteur N non factorisé…]`. Les **termes explicites** d'un eₖ ne sont énumérés que lorsque C(m,k) ≤ 60 ; au-delà, seule la valeur (factorisée bornée) est donnée. Aucune primalité n'est affirmée sur un cofacteur non calculé.

---

## 4 · Le jeu canonique versé dans les FP

Familles de fichiers de données/fiches + scripts + ce README + le script de test.

**(a) Fichiers-phrases homogènes — `S96/S1/S98/S13/S4_phrases_A.csv`.** Une ligne = une phrase. 12 colonnes : `phrase · partie · versets · rasm · lettres · jummal · facteurs · charge · partie_jummal · partie_facteurs · partie_charge · francais`. Jummal **et** nombre de lettres recomptés sur le rasm. `francais` vide pour S4. *C'est l'entrée de tout le reste.*

**(b) Décomposition lettre→jummal — `SXX_decomposition_lettres.csv`.** Une ligne = un **caractère** : `phrase · partie · rang_lettre · caractere · nom_unicode · valeur_abjad · cumul`. Montre la mise à zéro des harakat caractère par caractère. Σ des valeurs d'une phrase = son jummal (vérifié par assertion). Tailles : S1 16 ko … S4 1,37 Mo (33 573 lignes).

**(c) Fonctions symétriques — `SXX_fonctions_symetriques.csv`.** Une ligne = un eₖ d'une partie : `partie · degre · k · nb_termes_C(m,k) · e_k · e_k_facteurs · termes_explicites`. Le passage jummal→coefficient rendu visible (termes énumérés si C(m,k)≤60).

**(d) Objets, forme compacte — `SXX_obj_invariants.csv` et `SXX_obj_coeffs.csv`.** invariants = 21 champs aux niveaux *phrases* et *parties* ; coeffs = la liste complète des coefficients (eₖ et coeff X^(n−k)) des deux polynômes.

**(e) Fiches lisibles — `FICHE_OBJET_SXX.md` (non granulaire, A→F) et `FICHE_OBJET_SXX_GRANULAIRE.md` (lettre→coefficient, dérivation complète par partie).**

**(f) Fichiers transverses (les 17 objets ensemble) :**
- `OBJETS_ALGEBRIQUES_TABLE.csv` — **la table de comparaison**, 17 objets × 26 invariants. **Socle des tests de relation.**
- `CATALOGUE_OBJETS_PAR_PARTIE.csv` — vue courte des 17 objets (9 colonnes).
- `OBJETS_ALGEBRIQUES_REFERENCE.md` — catalogue lisible, par sourate, chaque objet titré + profil.
- `GRAND_LIVRE_OBJETS_S96_4temoins.csv` — fichier unique large, 575 lignes (toutes les phrases empilées), 48 colonnes : texte → comptes phrase → agrégats partie → objet sourate (`ph_*`) → objet parties-sommes (`pa_*`) → `formule_finale`.

**(g) La basmala comme objet — famille `BASMALA_*` (l'énoncé-mère calculable, le nom du projet) :** `BASMALA_decomposition_lettres.csv`, `BASMALA_segments_facteurs.csv`, `BASMALA_fonctions_symetriques.csv`, `BASMALA_obj_coeffs.csv`, `BASMALA_obj_invariants.csv`, `BASMALA_grains.csv` ; documentée par `README_BASMALA.md` et `LEXIQUE_BASMALA.md`. Pipeline identique, validé sur S1·A avant application. Invariant central : `ΣJ = 786 = 2·3·131`, 19 lettres porteuses, charge 0 ; trace e₁ = 786 aux niveaux *lettres* (deg 19) et *mots* (deg 4).

**(h) Moteur reproductible :**
- `build_granulaire.py` — module : table abjad, factorisation bornée, charge, `poly`/`poly_str` (Viète), `euclid`, `invset`, et `build(code)` qui lit `{code}_phrases_A.csv` et produit (b),(c),(d).
- `make_fiches.py` — lit le module, appelle `build(code)`, écrit les deux fiches (e). Usage : `python3 make_fiches.py S96`.
- `test_relations.py` — la batterie 1 des tests (cf. §7).

---

## 5 · Régénérer & vérifier

Tout est reproductible depuis `LE_CORAN.txt` + les `SXX_phrases_A.csv` :

```
python3 make_fiches.py S96   # (et S1, S98, S13, S4) → 6 fichiers/ sourate
python3 test_relations.py    # → rapport des relations entre les 17 objets
```

Contrôles intégrés (assertions) : Σ lettres = jummal pour chaque phrase ; Σ parties = Σ phrases = ΣJ(sourate). Si une assertion casse, la donnée d'entrée a changé.

---

## 6 · État du FP

Les actions sur le FP se font dans l'interface (lecture seule du côté moteur). Le classement de la session du 28/06 a été **appliqué** : les cibles « archiver » ne sont plus dans le FP actif.

**GARDER — sources d'entrée (irremplaçables) :** `LE_CORAN.txt`, `jummal_sourates.py`, `00_PROTOCOLE.md`, `01_DATA_jummal_114_par_verset.csv`, `jummal_par_sourate.csv`, `01_DATA_noms_jummal_114.csv`, `01_DATA_toniques_114_apex_P2.csv`, `quran-simple_xz_b64.txt`. **+ le cadre :** `PROTOCOLE_GENERAL_AUDIT.md`.

**ABSORBÉ DANS CE DOCUMENT (lignage) :** `MASTER_RAPPORT_1_4_TEMOINS.md` → `NOTE_SEGMENTATION_5_TEMOINS.md` (§2 ci-dessus) ; `CAHIER_TRAVAIL_OBJET_CENTRAL-2.md` (§8 ci-dessous). Ces fichiers cessent d'être des sources séparées ; leur contenu irremplaçable (critères de segmentation, objet central) vit ici.

**VERSÉ — le jeu produit (§4) :** les fichiers (a)–(f), la famille `BASMALA_*` (g), et les scripts (h).

**ARCHIVÉ — superseded (absents du FP) :** `MASTER_RAPPORT.md`, `BILAN_INTEGRAL_SESSION_GRAND_LIVRE_S96.md`, `AUDIT_COMPLETUDE_FUSION_v3.md`, `OBJETS_ALGEBRIQUES_S96/S1/S98/S4.md`, `objets_algebriques_S96.py`, `compute_S96.py`, `MASTER_S96.md`, `MASTER_S13_phrases.md`, `MASTER_SOMMAIRE_153_154`. *(La justification prose de la segmentation S13 par waqf demeure dans les `S13_phrases_A.csv` et en §2.2.)*

**PISTE SÉPARÉE — interprétation & production du livre (hors dossier d'analyse) :** `NOTE_OBSERVATEURS_QUANTIQUES_QAT_v3_complet.md` (couche [R3], SU(3)/observateurs), `FEUILLET_S96_v3.tex`, toutes les `FIGURES_*.tex` (dont `FIGURES_BASMALA_*`), `FRONTISPICE_TIKZ_v2.tex`, `SCEAU_AN-NUR_TIKZ_v1.tex`, `LCDC_LIVRE_FUSION_COMPLET_v3_SANS_CORAN.pdf`. **Garde absolue : ne pas supprimer `LCDC_…v3.pdf`** avant épuisement vérifié.

---

## 7 · Phase suivante — tests de mise en relation

Objectif : chercher les **relations structurelles** entre les 17 objets, sur la donnée seule (aucune coïncidence pêchée ; on teste des familles définies à l'avance), puis tenter de **synthétiser** ce qui relie ces 17 objets — en route vers 𝒞.

`test_relations.py` exécute déjà la **batterie 1** sur `OBJETS_ALGEBRIQUES_TABLE.csv` :
1. traces égales ; 2. divisibilité des traces ; 3. facteurs premiers communs entre traces ; 4. pgcd des traces deux à deux ; 5. spectres partagés / disjoints ; 6. charges (bilan global, paires) ; 7. coïncidences de degré ; 8. invariants partagés (e₂, e₃, p₂, p₃, vmin, vmax).

Quelques sorties de la batterie 1 (à titre d'amorce, sans interprétation) : les **17 charges se somment à 0** (4×+1, 9×0, 4×−1) ; **spectre complet {2,3,5,7,11,13,17,19}** partagé par S96·P2, S4·corps, S4·clausule, S13·corps ; **degré 7** commun à S96·P2 et S98·corps ; **pgcd(16698,238227)=33** entre les corps de S98 et S13 ; la valeur **860** est racine à la fois dans S1·A (énoncé) et S98·pôle− (« les pires »).

**Extensions à coder (batterie 2 et +) :**
- objets **niveau-sourate** (les 5 polynômes des sommets entiers) ajoutés à la table, puis relations inter-niveaux.
- relations **eₖ / Newton croisées** (coefficients ou sommes de puissances coïncidant entre objets), au-delà des seuls invariants déjà tabulés.
- relations **spectrales fines** (racines communes entre polynômes ; resultant / pgcd polynomial de deux R(X)).
- appariements de **charges** par grandeur homogène (les pôles ± de S98 ; les trois `كلا` de S96) ; l'objet **basmala** mis en relation avec S96·basmala et les racines-786 partagées.

---

## 8 · 𝒞 — l'objet algébrique central

*(Absorbe `CAHIER_TRAVAIL_OBJET_CENTRAL-2.md`. La table des 5 sommets est en §1 ; on n'y renvoie ici sans la redupliquer.)*

### 8.0 · But et thèse
Définir et construire l'**objet algébrique central** du projet : **S96** (l'orthogonale / le Lecteur, source hors-sphère, 0/154) soudée aux **4 témoins** {S1, S4, S98, S13} (le noyau récurrent de *f*). Les 4 témoins portent la **structure 4D** ; **l'éternel retour à S1** (l'attracteur) établit **toutes les connexions**. Trace **1 418 472 = 2³·3⁴·11·199**, charge **0** — cohérent avec `PROTOCOLE_GENERAL_AUDIT §IV.5` (𝒞 = RAPPORT + S96 ; RAPPORT = 1 397 122 = 2·47·89·167).

### 8.1 · Les cinq sommets
Voir la table **§1** (J(nom), ΣJ, factorisations, charges, rôles — recomptés [bi]). Lecture des charges : deux +, deux −, S13 neutre au centre, Σ = 0 ; le triplet Z₃ {−1,0,+1} est présent ; l'objet central est globalement neutre, équilibré autour de l'ermite.

### 8.2 · Ce qui est ÉTABLI (et sa source)
- **Le pont S96↔S13** : ΣJ(S96) = 21350 = **305 × 70**, où 305 = J(الرعد) = nom de S13. C'est l'**unique** arête remplie par « nom divise total » sur les 10 (scan §8.4). [vérifié FP]
- **Le 61 noue** S96↔S13 : 61∣305 et 61∣21350 ; et le témoin V43.2 = 1647 = 3³·**61** porte ce 61 au cœur des phrases de S13. [vérifié FP]
- **Le 17 traverse** : كلا(S96)=51=3·**17** ; الحساب(S13)=102=2·3·**17**=2×51. [vérifié FP]
- **Décompositions en phrases** de S96 (15 ph., Σ=21350) et S13 (111 ph., Σ=239874, témoin-centre 1647) — fichiers `SXX_phrases_A.csv`. [vérifié FP]
- **Noyau récurrent de *f*** : Fix f = {13}, cycle {1→4→98→1}, S1 attracteur (degré entrant 57 = 3·19). [SOURCE : CSV toniques — **de nouveau re-dérivable**, voir §8.3]

### 8.3 · Prérequis *f* — **LEVÉ** (le fichier est présent)
**`01_DATA_toniques_114_apex_P2.csv`** (l'endofonction f(s) = `pointe_sourate`) **est présent dans les FP** (vérifié : fichier listé, en-tête portant la colonne `pointe_sourate`). La version antérieure de ce cahier le donnait pour manquant ; **c'est corrigé**. Toute la mécanique du flux est donc de nouveau re-calculable : *f*, le noyau {13}∪{1,4,98}, le degré entrant 57 de S1, les chemins de retour, l'éternel retour à S1. *(Re-dérivation effective à faire en session ; le verrou matériel est tombé.)*

### 8.4 · La structure 4D — le 4-simplexe (pentachore)
5 sommets → **4-simplexe** : 10 arêtes, 10 faces, 5 cellules (tétraèdres). Décomposition : {S1,S4,S98} = l'œil (3-cycle) · S13 = ermite · S96 = apex orthogonal.

**La relation d'arête est ÉTABLIE : c'est le renvoi *f*** (la pointe — voir §8.5 et `PROTOCOLE_GENERAL_AUDIT.md`, « la pointe EST la connexion »). Le scan ci-dessous ne sert qu'à montrer *pourquoi un critère statique ne convient pas* : la divisibilité nom∣total ne remplit qu'**1 arête sur 10** (le pont S13–S96), et pgcd ou premier partagé n'en garnissent que 3. Un critère bâti sur les totaux/noms laisse la figure creuse — d'où le recours à la relation **dynamique** *f* (qui, par les chemins de retour à S1, relie tous les sommets). Scan des 10 arêtes (FP, recompté [bi]) :

| arête | pgcd(ΣJ) | premiers ΣJ communs | nom∣total ? |
|---|:--:|---|:--:|
| S1–S4 | 1 | — | non |
| S1–S13 | 1 | — | non |
| S1–S96 | 1 | — | non |
| S1–S98 | 1 | — | non |
| S4–S13 | 2 | [2] | non |
| S4–S96 | 10 | [2, 5] | non |
| S4–S98 | 1 | — | non |
| S13–S96 | 2 | [2] | **oui** |
| S13–S98 | 1 | — | non |
| S96–S98 | 1 | — | non |

**La connexion est tranchée — ce n'est pas une décision ouverte.** Une connexion *est* une **pointe du renvoi *f*** : chaque sourate pointe vers la sourate dont le numéro égale celui de son verset-pointe (FP `pointe_sourate`), vérifié **114/114**. Recompté [bi] : f(96)=2, f(1)=4, f(4)=98, f(98)=1, f(13)=13 (point fixe) ; f²(96)=70 ; **image = 37** cibles distinctes, dont **1 point fixe** {S13}, soit **36 connexions** (les cibles non-fixes) et **77 sources** (deg_in 0) ; deg_in(S1)=57=3·19, deg_in(S96)=0. C'est le même *f* qui fonde la bascule `114 →(+36)→ 150` du cadre. Les critères (a)–(g) du scan ne sont donc **pas** des candidats concurrents à départager : ils ont servi à constater l'insuffisance des relations statiques, ce que *f* (dynamique) résout. *(Source : `PROTOCOLE_GENERAL_AUDIT.md`, renvoi f ; `00_PROTOCOLE.md` §3.)*

### 8.5 · L'éternel retour à S1 — les connexions
S1 = attracteur, degré entrant **57 = 3·19** ; tout le flux y revient. Les connexions **sont** les **chemins de retour** de chaque sommet vers S1 par *f* — établi et recompté [bi] : chemin `96→2→70→3→33→20→88→1` (7 pas) ; cycle de l'œil `1→4→98→1` ; point fixe `f(13)=13` ; **36 connexions** au total (cibles non-fixes du renvoi *f*, §8.4). Ce qui reste à **dérouler** (calcul mécanique, non décision) : pour chaque sommet, la longueur de son chemin vers S1 et l'**holonomie** (la charge `{0,+1,−1}` accumulée le long du retour).

### 8.6 · Le polynôme central (l'« équation propre » de 𝒞)
Former le polynôme unitaire dont les sommets sont racines (méthode du projet, P(X)=∏(X−racines)).
- **Sur les noms** (degré 5, racines [525, 143, 305, 231, 98]) : Σ noms = **1302** = 2·3·7·31 ; coefficients e₁…e₅ = [1302, 621570, 136654784, 13845214845, 518362094250].
- **Sur les totaux** : Σ ΣJ = **1 418 472** = 2³·3⁴·11·199 (la trace) ; polynôme de degré 5 à coefficients géants (à dérouler en session).
À faire : facteurs, fonctions symétriques, et tester si ce polynôme central a une structure (racines de l'unité, irréductibilité, lien au 153/150).

### 8.7 · Étapes de construction — ordre précis
1. Re-dériver *f* depuis le CSV toniques (désormais présent) : noyau, degré entrant de S1, chemins des 5 sommets vers S1.
2. Charger l'objet-sommets (table §1, déjà vérifiée — réutiliser).
3. **Instancier la relation d'arête = le renvoi *f*** (établi, §8.4–§8.5) : tracer les arêtes/chemins par *f*, marquer le point fixe S13 et les 36 connexions. *(Plus de « définir/trancher » : la relation est arrêtée.)*
4. Construire le **4-simplexe** avec la relation retenue ; marquer arêtes/faces/cellules « remplies ».
5. Construire **l'éternel retour** : chemins vers S1, holonomie, structure des connexions.
6. Dérouler le **polynôme central** (§8.6) : coefficients, facteurs, structure.
7. **Synthèse** : 𝒞 = (5 sommets, relation d'arête = renvoi *f*, 4-simplexe, retour-à-S1, polynôme central) — un seul objet, qui entre dans `OBJETS_ALGEBRIQUES_TABLE.csv` comme **18ᵉ objet** et fédère les tests de relation (§7).

### 8.8 · Décisions ouvertes (à trancher en début de session)
- **Valeur de sommet** : ΣJ (total), J(nom), ou vecteur des phrases ? *(et, pour les racines de 𝒞 : 5 traces-sommet {21350, 10147, 28891, 239874, 1118210}, ou 575 jummal-phrases, ou 17 traces-objet ?)*
- **Objet 4D** : 4-simplexe, ou autre (les charges Z₃ × autre chose) ?
- **Rôle de S1** : 5ᵉ sommet *et* attracteur — apex du retour, ou sommet parmi 5 ?

*Décisions désormais TRANCHÉES (retirées de cette liste) :*
- ~~Relation de connexion (l'arête)~~ → **arrêtée : la pointe du renvoi *f*** (§8.4–§8.5 ; 36 connexions ; vérifié 114/114 ; cadre `PROTOCOLE_GENERAL_AUDIT.md`).
- ~~Homogénéité du critère de segmentation~~ → **non-problème : la règle est unique (la phrase)** ; seuls les outils de repérage varient (§2.2–§2.3). La comparaison des objets entre sommets est légitime.

### 8.9 · Topologie de l'objet central (Régime 3) — deux apports réels, un écueil

**8.9.1 · Apport RÉEL — la frontière de 𝒞 EST l'hypersphère.** Fait standard, non numérologique : **∂Δⁿ ≅ Sⁿ⁻¹**. La frontière du **4-simplexe** (S96 + 4 témoins) est exactement **S³**. Le modèle géométrique (la sphère = le corps compté) se referme sur la combinatoire :
- **f-vecteur** : 5 sommets · **10 arêtes** · 10 triangles · **5 tétraèdres** · 1 cellule ; χ(∂Δ⁴) = 5−10+10−5 = **0** = χ(S³) (vérifié).
- **Structure apex / base** : S96 = **apex** ; la facette **opposée à S96** est le tétraèdre **{S1,S4,S98,S13}** (les 4 témoins). Le 4-simplexe = **cône de sommet S96 sur la base des 4 témoins** ; S13 (le contact *p*) est un sommet de cette base, sur S³.
- Conséquence pour §8.4 : les **10 arêtes** à remplir = les arêtes de S³ ; les **5 tétraèdres** = les 5 cellules-témoins (une par sommet omis). La « relation d'arête » à définir est la donnée qui transforme ce squelette S³ en objet *valué*.

**8.9.2 · Apport d'IMAGE (Régime 3) — le retournement de la sphère.** Le **retournement de la sphère** de Smale (immersions S²→ℝ³ ; surfaces de Morin/Boy = étapes) est l'archétype mathématique de « tourner à l'envers ». C'est l'**image** topologique du **retournement** déjà présent dans le projet (l'inversion du souffle §150→§1 ; S96 = 1ʳᵉ révélée / 96ᵉ écrite ; descente S96→S13 puis retour à S1). **Homologie déclarée, imagerie seule — aucune arithmétique ajoutée.** (Distinguer : Smale concerne S² ; l'hypersphère §8.9.1 est S³.)

**8.9.3 · Écueil à ÉVITER — les groupes d'homotopie des sphères.** **Ne pas les inscrire comme structure.** Deux raisons rigoureuses :
1. **Non-pertinence d'encodage.** Les π_k(Sⁿ) sont **intrinsèques à la sphère** : identiques pour *toute* S³, ils ne dépendent **d'aucune** donnée du projet (ni jummal, ni *f*). Même via la frontière S³ (§8.9.1), ils ne portent **aucune** information sur les sourates.
2. **Coïncidences non informatives.** Les premiers 13, 17, 19 apparaissent dans les stems stables — mais c'est **garanti** : tout premier *p* apparaît, sa **première** torsion tombe au stem **2p−3** (image de J). D'où 13→23, 17→31, 19→35, 61→119, 71→139 — des indices **sans aucun sens projet**. Y lire une structure serait exactement la numérologie que le **Régime 3 / modèle nul** interdit.

**Si une couche topologique est voulue**, les bons outils sont **combinatoires/discrets** — l'homologie simpliciale du 4-simplexe et de sa frontière S³ (§8.9.1), et la dynamique de l'endofonction *f* (basin, retour à S1, §8.5) — **pas** l'homotopie des sphères.

---

*Document de fusion. Absorbe `NOTE_SEGMENTATION_5_TEMOINS.md` (→ §2, qui absorbait `MASTER_RAPPORT_1_4_TEMOINS.md`) et `CAHIER_TRAVAIL_OBJET_CENTRAL-2.md` (→ §8). Table des 5 sommets dédupliquée (§1, occurrence unique). Correction portée : prérequis *f* (`01_DATA_toniques_114_apex_P2.csv`) **présent** dans les FP, donc levé (§8.3). Tous les nombres de §1 recomptés sur les FP — [bi]. Renvois externes (`§∴`, `§VI.0`, `§IV.5`, `§V.9`) vers `PROTOCOLE_GENERAL_AUDIT.md`.*

*Révision v2 (corrections d'incohérences internes héritées du cahier de travail absorbé, alignées sur le cadre supérieur `PROTOCOLE_GENERAL_AUDIT.md`) : (1) **§2.2–§2.3** — supprimé le faux « point ouvert » sur l'homogénéité de la segmentation : la règle de découpe est **unique (la phrase)**, seuls les outils de repérage de fin de phrase varient ; la comparaison inter-sommets est légitime ; conservation `Σ(phrases)=ΣJ` garantie [bi]. (2) **§8.4, §8.5, §8.7, §8.8** — supprimé la fausse « Décision centrale : quelle relation EST une connexion ? » : la relation d'arête **est arrêtée — la pointe du renvoi *f***, conformément à `PROTOCOLE_GENERAL_AUDIT.md` (« la pointe EST la connexion ») ; recompté [bi] sur le FP `pointe_sourate` : f(96)=2, f(1)=4, f(4)=98, f(98)=1, f(13)=13, f²(96)=70 ; image 37, point fixe {13}, **36 connexions**, 77 sources, deg_in(S1)=57=3·19. Le scan nom∣total / pgcd de §8.4 est conservé à titre d'illustration (un critère statique ne garnit que 1 à 3 arêtes sur 10 — d'où *f*, dynamique).*
