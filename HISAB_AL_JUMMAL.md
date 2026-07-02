# Ḥisāb al-jummal — la méthode de calcul (le comput abjad mašriqī)

> **Provenance.** Contenu extrait de l'archive de référence *Les Comptes du Coran — Édition fusionnée* (Partie B, « Méthode de calcul »), seul porteur du master `MASTER_2_HISAB_AL_JUMMAL` dont la source .tex est perdue. **Tous les nombres ci-dessous ont été recalculés sur les FP** (`01_DATA_noms_jummal_114.csv`, `01_DATA_jummal_114_par_verset.csv`, table abjad du protocole §2) — [bi] — et non repris de l'archive, dont l'arabe est par endroits corrompu. Premier composant traité du protocole d'épuisement (`ARCHIVE_EPUISEMENT.csv`).

## 1 · Origine et histoire

Le procédé est le **ḥisāb al-jummal** (comput abjad) : système de numération alphabétique où chacune des **28 lettres** de l'alphabet arabe reçoit une valeur entière fixe de **1 à 1000**. Son nom vient des quatre premières lettres de l'ordre sémitique ancien, **a-b-j-d** (alif = 1, bāʾ = 2, jīm = 3, dāl = 4). Cet ordre reproduit la séquence sémitique du phénicien, de l'araméen et de l'hébreu (22 lettres, jusqu'à tāw = 400) ; l'arabe la prolonge par ses **six lettres supplémentaires** (*rawādif*). Apparenté à la guématrie hébraïque et à l'isopséphie grecque, il a servi durant plus d'un millénaire à dater (chronogrammes), numéroter et chiffrer. La forme orientale (**mašriqī**), adoptée ici, s'est fixée au plus tard vers le IXᵉ siècle. *(Sur l'histoire du procédé : Encyclopaedia Iranica, art. « Abjad ».)*

## 2 · La table et la définition précise

La table des valeurs est celle **gravée au protocole §2** (table mašriqī, 28 lettres) ; on ne la redédouble pas ici. Conventions de lecture : la hamza vaut 1 ; la tāʾ marbūṭa (ة) vaut 5 ; les variantes de l'alif (أ إ آ ٱ) valent 1 ; le yāʾ (ي) et l'alif maqṣūra (ى) valent 10 ; toute marque hors-table (vocalisation, espaces) vaut 0.

La fonction **J** est un **morphisme additif** pour la concaténation : `J(t₁t₂) = J(t₁) + J(t₂)`. Pour un titre, on somme les valeurs de ses lettres ; le nom est pris **dans sa forme du muṣḥaf** (article *al-* inclus le cas échéant).

## 3 · Un exemple entièrement déroulé (recalculé [bi])

Le nom de la sourate-source, **العلق** (al-ʿAlaq, « le caillot »), lettre à lettre :

| lettre | nom | valeur | cumul |
|:---:|---|---:|---:|
| ا | alif | 1 | 1 |
| ل | lām | 30 | 31 |
| ع | ʿayn | 70 | 101 |
| ل | lām | 30 | 131 |
| ق | qāf | 100 | 231 |

soit **J(العلق) = 231 = 3·7·11**.

Repères vérifiés sur les FP (les J(nom) des 114 titres) :

- plus petite **valeur** jummal : **طه** (Ṭā-Hā, S20) = 14 = 2·7 ;
- plus grande **valeur** jummal : **التغابن** (S64) = 1484 = 2^2·7·53 ;
- titre du **moins de lettres** : **ص** (S38, 1 lettre) = 90 = 2·3^2·5 ;
- titre du **plus de lettres** : **المنافقون** (S63, 9 lettres) = 358 = 2·179 ;
- al-Fātiḥa (S1) = 525 = 3·5^2·7.

> **Correction portée.** L'archive (B.3) désignait طه comme « le titre le plus court » et al-Fātiḥa comme « le plus long » : imprécis. En nombre de lettres, le plus court est **ص** (1 lettre) et le plus long **المنافقون** (9 lettres) ; طه n'a que la plus petite *valeur*. Corrigé ici, recompté sur les FP.

En cumulant les 114 titres on obtient la **primitive discrète F(s)** ; sa valeur terminale est **ΣJ(titres) = 40238 = 2·11·31·59**. *(À ne pas confondre avec le jummal du corpus entier — somme sur les 6236 versets — qui vaut **23476120 = 2^3·5·586903**.)*

---

*Composant « ḥisāb al-jummal » (ex-`MASTER_2`, source perdue) : extrait, reformulé, nombres recalculés [bi]. Il sécurise le contenu le plus à risque de l'archive de référence.*
