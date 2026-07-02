# FICHE OBJET — 𝒞 (l'objet algébrique central)
*The Basmala Formula — 18ᵉ objet. Recompté sur les FP, arithmétique entière exacte [bi]. **Fiche v2** : cofacteurs de e₃, e₄ entièrement résolus (Miller-Rabin déterministe + Pollard rho) — plus aucun facteur indéterminé.*

## 0 · Définition
𝒞 = **RAPPORT (les 4 témoins) + S96**. S96 (apex / source, hors-sphère, 0/154) soudé au noyau récurrent du renvoi *f* {S1, S4, S98, S13}.
- trace 𝒞 = Σ ΣJ(5) = **1418472 = 2^3·3^4·11·199**, charge **+0**
- RAPPORT (4 témoins) = **1397122 = 2·47·89·167**, charge **+1**
- contrôle : RAPPORT + ΣJ(S96) = 1397122 + 21350 = 1418472 ✓

## 1 · Les 5 sommets
| sommet | nom | ΣJ | charge (corps) | J(nom) | charge (nom) | rôle dans *f* |
|---|---|--:|:--:|--:|:--:|---|
| S96 | العلق al-ʿAlaq | 21350 | -1 | 231 | +0 | apex / source (deg_in 0) |
| S1 | الفاتحة al-Fātiḥa | 10147 | +1 | 525 | +0 | attracteur (deg_in 57=3·19) |
| S98 | البينة al-Bayyina | 28891 | +1 | 98 | -1 | œil (cycle) |
| S13 | الرعد ar-Raʿd | 239874 | +0 | 305 | -1 | ermite (point fixe f(13)=13) |
| S4 | النساء an-Nisāʾ | 1118210 | -1 | 143 | -1 | œil (cycle) |

Σ charges (corps) = **0**. Σ(4 témoins) = +1, refermé par S96 (−1) = **0** ; triplet Z₃ {−1,0,+1} présent, S13 neutre au centre.

## 2 · La relation d'arête = le renvoi *f* (établie)
Une connexion **est** une pointe de *f* (FP `pointe_sourate` ; « la pointe EST la connexion », `PROTOCOLE_GENERAL_AUDIT`). f(96)=2, f(1)=4, f(4)=98, f(98)=1, f(13)=13 ; point fixe **{13}** ; **36 connexions** (cibles non-fixes) ; 77 sources ; deg_in(S1)=57=3·19, deg_in(S96)=0.

**Éternel retour à S1 + holonomie** (Σ des charges `ΣJ mod 3` des nœuds, extrémités incluses) :
| sommet | chemin *f* → S1 | pas | holonomie |
|---|---|--:|:--:|
| S96 | 96→2→70→3→33→20→88→1 | 7 | +0 |
| S1 | 1 | 0 | +1 |
| S98 | 98→1 | 1 | -1 |
| S13 | point fixe — bassin propre (ermite) | — | hors-retour |
| S4 | 4→98→1 | 2 | +1 |

Cycle de l'œil : 1→4→98→1, holonomie +1. Les holonomies réalisent les trois classes : S96 → 0, S4 → +1, S98 → −1.

## 3 · La structure 4D — le 4-simplexe (pentachore)
5 sommets → **10 arêtes · 10 faces · 5 cellules · 1 cellule 4D**. χ(∂Δ⁴) = 5−10+10−5 = **0** = χ(S³) : la frontière de 𝒞 est l'hypersphère **S³** (∂Δⁿ≅Sⁿ⁻¹). Apex = **S96** ; facette opposée = {S1,S4,S98,S13}. 𝒞 = cône de sommet S96 sur la base des 4 témoins.

## 4 · Le polynôme central — (a) sur les TOTAUX ΣJ  *(choix principal : trace 𝒞)*
- racines : `10147 21350 28891 239874 1118210` (degré 5)
- e1 = 1418472 = 2^3·3^4·11·199
- e2 = 351368100409 = 433·23623·34351
- e3 = 17734144538109738 = 2·3·3785687·780754129
- e4 = 310692377301013406380 = 2^2·5·11·37·23719·1609199237743
- e5 = 1678822043557743107583000 = 2^3·3·5^3·7·61·73·139·167·173·39979·111821
- trace e₁ = **1418472 = 2^3·3^4·11·199**, charge **+0** ; produit e₅ = 2^3·3·5^3·7·61·73·139·167·173·39979·111821
- Newton : p₁=1418472 · p₂=1309326613966 · p₃=1412039762256554118
- pgcd=1 · vmin=10147 · vmax=1118210 · distinct=5 · nprimes=11
- charges racines : +1×2 · 0×1 · −1×2 · spectre présent {2 3 5 7}, absent {11 13 17 19}
- **R[𝒞 · RAPPORT+S96 · totaux](X) = X^5 −1418472·X^4 +351368100409·X^3 −17734144538109738·X^2 +310692377301013406380·X −1678822043557743107583000**
> e₃ et e₄ : cofacteurs résolus — **e₃ : 2 955 690 756 351 623 = 3785687·780754129** (composé !) ; **e₄ : 1 609 199 237 743 premier**. Tous facteurs premiers confirmés (Miller-Rabin déterministe).

## 5 · Le polynôme central — (b) sur les NOMS J(nom)  *(variante ; concorde avec README §8.6)*
- racines : `98 143 231 305 525` (degré 5)
- e1 = 1302 = 2·3·7·31
- e2 = 621570 = 2·3·5·20719
- e3 = 136654784 = 2^6·7·305033
- e4 = 13845214845 = 3^3·5·7^2·11·149·1277
- e5 = 518362094250 = 2·3^2·5^3·7^4·11^2·13·61
- trace e₁ = **1302 = 2·3·7·31**, charge **+0** ; produit e₅ = 2·3^2·5^3·7^4·11^2·13·61
- Newton : p₁=1302 · p₂=452064 · p₃=189267540
- pgcd=1 · vmin=98 · vmax=525 · distinct=5 · nprimes=7
- charges racines : +1×0 · 0×2 · −1×3 · spectre présent {2 3 5 7 11 13}, absent {17 19}
- **R[𝒞 · RAPPORT+S96 · noms](X) = X^5 −1302·X^4 +621570·X^3 −136654784·X^2 +13845214845·X −518362094250**

## 6 · Conventions adoptées (décisions §8.8 tranchées pour cette construction)
- **Racines de 𝒞** : les **5 traces-sommet ΣJ** (→ trace 1 418 472, cohérent avec la définition). Variante sur les noms en §5.
- **Relation d'arête** : le **renvoi *f*** (établie). **Objet 4D** : le **4-simplexe** (frontière S³).
- **Holonomie** : Σ des charges des nœuds du chemin de retour, extrémités incluses (détail montré, modifiable).
- **Factorisation** : ici **complète** (cofacteurs résolus par primalité déterministe + Pollard rho), au-delà du défaut borné 10⁶ du moteur.

## 7 · Ligne pour `OBJETS_ALGEBRIQUES_TABLE.csv` (18ᵉ objet)
```csv
sourate,nom,partie,titre,degre,racines,trace_e1,trace_facteurs,produit_facteurs,pgcd,charge,charge_pos,charge_zero,charge_neg,vmin,vmax,distinct,nprimes,premiers_presents,premiers_absents,e2,e3,p1,p2,p3,formule_finale
𝒞,(objet central 𝒞),totaux ΣJ,𝒞 · RAPPORT+S96 · totaux,5,10147 21350 28891 239874 1118210,1418472,2^3·3^4·11·199,2^3·3·5^3·7·61·73·139·167·173·39979·111821,1,0,2,1,2,10147,1118210,5,11,2 3 5 7,11 13 17 19,351368100409,17734144538109738,1418472,1309326613966,1412039762256554118,R[𝒞 · RAPPORT+S96 · totaux](X) = X^5 −1418472·X^4 +351368100409·X^3 −17734144538109738·X^2 +310692377301013406380·X −1678822043557743107583000
𝒞,(objet central 𝒞),noms J(nom),𝒞 · RAPPORT+S96 · noms,5,98 143 231 305 525,1302,2·3·7·31,2·3^2·5^3·7^4·11^2·13·61,1,0,0,2,3,98,525,5,7,2 3 5 7 11 13,17 19,621570,136654784,1302,452064,189267540,R[𝒞 · RAPPORT+S96 · noms](X) = X^5 −1302·X^4 +621570·X^3 −136654784·X^2 +13845214845·X −518362094250
```