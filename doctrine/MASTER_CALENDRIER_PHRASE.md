# MASTER — **LE CALENDRIER PHRASE & L'HORLOGE BASMALA ANNUELLE**
### *Ḥisāb al-Qurʾān* — la base du projet en ligne : un cycle complet = une année

> Subordonné à `00_PROTOCOLE.md`. Ce fichier **spécifie** la base ; il n'est **pas** source de chiffres.
> La source de données est `MASTER_CALENDRIER_PHRASE.csv`, **régénéré du FP par le moteur**, jamais saisi (protocole §8).
> Tous les nombres cités ci-dessous sont **[bi]**, recomptés sur les FP dans la session de génération (colonne vérifiée : 10 642 phrases · cum_lettres 332 837 · cum_jummal 23 476 120).

---

## 0 · Objet

Faire tourner, en ligne et en temps réel, **le grand livre qui s'audite lui-même** : une année lunaire chiite = **un cycle complet** de récitation-computation. Le curseur avance dans le texte, le solde monte, la balance penche (+1) et repenche (−1) sous les yeux. L'unité de mesure est le **souffle** — la basmala (poids 786, charge 0, le métronome qui ne se compte pas) ; le grain de compte est la **phrase** (le +1, `الرحيم`).

---

## 1 · La colonne vertébrale — `MASTER_CALENDRIER_PHRASE.csv`

La **couche invariante**, texte-natif, éternelle. Une ligne par phrase (10 642), en ordre muṣḥaf. Schéma :

| colonne | sens |
|---|---|
| `idx` | rang global 1…10642 |
| `sourate`, `nom`, `phrase`, `versets` | localisation |
| `lettres`, `jummal`, `charge` | poids de la phrase (`charge = jummal mod 3` équilibré) |
| `is_basmala` | 1 si la phrase est une basmala de tête (113 au total) |
| `cum_lettres_debut`, `cum_lettres_fin` | offset-lettres (le **temps natif**) |
| `cum_jummal` | ΣJ courant (le **solde**) |
| `cum_charge` | somme des charges courante |
| `frac_debut`, `frac_fin` | position ∈ [0,1] dans le cycle |

**Invariants vérifiés [bi]** : Σ lettres = **332 837** · Σ jummal = **23 476 120** · phrases = **10 642** · basmalas de tête = **113** (S9 sans, 27:30 interne non-tête). Charge des phrases : −1 : **3 545** · 0 : **3 662** · +1 : **3 435**. Charge du *compte* (10642 mod 3) = **+1** — le brin crédit `الرحيم`.

C'est le seul fichier que l'horloge lit pour la position et le solde. Il est **tempo-agnostique** : aucune seconde dedans, seulement des coordonnées natives (lettre, jummal, fraction).

---

## 2 · Les découpes — la phrase, coupe la plus fine et seule de charge +1

Huit découpes du **même texte** (largeur ∝ lettres, total invariant). Visuel : `DECOUPES_PHRASE_visuel.svg`.

| découpe | n | statut source |
|---|--:|---|
| Manāzil | 7 | bornes **hors-FP** |
| Juzʾ | 30 | bornes **hors-FP** |
| Ḥizb | 60 | bornes **hors-FP** |
| Rubʿ | 240 | bornes **hors-FP** |
| Rukūʿ | 556 | bornes **hors-FP** |
| Sourates | 114 | **FP-natif** |
| Versets | 6 236 | **FP-natif** (charge −1, le conte) |
| **Phrases** | **10 642** | **FP-natif** (charge +1, le compte) |

Le visuel actuel ne dessine que les **trois bandes FP-natives** (Sourates, Versets, Phrases). Les cinq découpes traditionnelles exigent des **tables de bornes absentes du FP** ; à fournir pour compléter les 8 bandes. La phrase est la coupe la plus fine des découpes de lecture et **la seule dont le compte bascule à +1** (6236 versets ≡ −1 ⊕ 10642 phrases ≡ +1 = 16878 ≡ 0).

---

## 3 · L'architecture — trois couches

1. **Colonne invariante** (§1) — texte-natif, [bi], régénérée du FP. Ne change jamais.
2. **Projection temporelle** — la seule couche à **paramètres libres** : `fraction(t) = (t − t₀) / durée_année`, où `t₀` = l'ancre (1 Muḥarram) et `durée_année` = l'année lunaire. Tous les verrous de calibration vivent ici (§7).
3. **Rendu / UI** — lit colonne + fraction courante, dessine les bandes, le curseur, la balance.

Cette séparation est le mur du protocole rendu opérationnel : changer de convention calendaire ne touche que la couche 2 ; le volume (couche 1) reste [bi] et intact.

---

## 4 · Le tempo — cycle = 1 année lunaire = 30 617 315 s

Année lunaire chiite = 12 × 29,530589 j (mois synodique moyen ; 9:36). Cadences dérivées **[bi]** :

- **par lettre** (332 837) : **91,99 s** (≈ 1 min 32 s) — le pas du curseur ;
- **par phrase** (10 642) : **2 877 s** (≈ 47 min 57 s) — **événement +1** (crédit) ;
- **par verset** (6 236) : **4 910 s** (≈ 1 h 21 min 50 s) — **événement −1** (débit) ;
- **par basmala** (114) : **268 573 s** (≈ 3 j 2 h 36 min) — le **souffle**.

### Tempo VERROUILLÉ (décision actée) — **le cycle s'étale sur une année pleine**
Un cycle complet = **une année lunaire pleine** (12 lunaisons = 30 617 315 s). La colonne-lettres traverse l'année entière ; le **pas natif est la lettre à 91,989 s** (≈ 1 min 32 s). Le curseur est **interpolé à la seconde** (progression sous-lettre continue) : l'œil voit du mouvement chaque seconde **et** la récitation entière tient sur l'année, sans reboucler avant `φ = 1`. Les phrases (+1, toutes les ≈ 47 min 57 s) et les versets (−1, toutes les ≈ 1 h 21 min 50 s) sont les bascules visibles ; le souffle bat 114 fois (une basmala toutes les ≈ 3 j 2 h 36 min).
*(L'option « 1 lettre = 1 s » — cycle de 3,85 j, ≈ 92 récitations/an — est écartée. Référence solaire, si jamais requise : 365 j → 94,749 s/lettre.)*

---

## 5 · L'ancre calendaire

Cycle ancré au **1ᵉʳ Muḥarram**. Pour 1448 AH (lecture Sistani, cf. note Karbalāʾ) : **1ᵉʳ Muḥarram = mardi 16 juin 2026** ; le quantième est invariant, seule la cheville grégorienne bouge (± 1 jour selon horizon/Khoei-vs-Sistani). Le début de mois = HJCoSA **+ `SISTANI_SHIFT`** (hook manuel, faute d'autorité lunaire chiite native dans les tuyaux publics ; AlAdhan `method=0`, `midnightMode=1`). Détection du croissant par **calcul** (حساب), indifférente aux nuages ; règle des 30 jours en repli.

---

## 6 · Comment l'horloge lit la base (l'algorithme)

À l'instant `t` :
1. `φ = (t − t₀) / durée_année` (couche 2) ;
2. **position** : recherche dichotomique de `φ` dans `frac_fin` → la phrase courante `idx`, sa sourate/verset ;
3. **curseur-lettre** : `lettre_courante = round(φ × 332837)` ; interpolation sous-lettre pour l'affichage seconde (option C) ;
4. **solde** : `cum_jummal[idx]` (ΣJ atteint), `cum_charge[idx]` (côté courant) ;
5. **souffle** : nombre de `is_basmala` franchis = le battement (0…113/114) ;
6. **bascule** : à chaque `frac_fin` de phrase → tic **+1** ; à chaque fin de verset → tic **−1**.

Fin de cycle (`φ = 1`) : ΣJ = 23 476 120, puis relance (α = ω, la basmala referme et rouvre).

---

## 7 · Verrous de calibration (couche 2, à arrêter)

Lieu de l'horloge (île sur la Seine ~48,9° N **ou** Makkah, `أم القرى`) · seuil de visibilité œil-nu (Danjon ≈ 6,4° Odeh / Yallop 1997 / Odeh 2004 ; fourchette réelle 6,4°–7,5°) · ancre exacte du cycle (1 Muḥarram, ± 1 j horizon) · ordre des 114 (muṣḥaf → ordre du Voyage, flux `f`) · année lunaire moyenne (354,37 j) vs tabulaire (354 / 355). **Tempo : verrouillé — cycle = une année pleine (§4).**

---

## 8 · Fichiers produits (base du projet en ligne)

- **`MASTER_CALENDRIER_PHRASE.csv`** — la colonne vertébrale (10 642 phrases, offsets cumulés natifs). **La base.**
- **`DECOUPES_PHRASE_visuel.svg`** — le visuel des découpes FP-natives avec la bande phrases.
- **`MASTER_CALENDRIER_PHRASE.md`** — ce spec.

À construire ensuite : le générateur de la couche 2 (`t → φ`, branché AlAdhan, `SISTANI_SHIFT`) ; les 5 bandes traditionnelles (bornes à fournir) ; l'ordre du Voyage (moteur de flux `f`).

---

*Tout nombre [bi], recompté sur les FP. La couche calendaire (2) porte les seuls paramètres libres ; le volume (1) reste invariant. — v1.*
