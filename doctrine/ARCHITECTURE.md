# ARCHITECTURE — l'ordinateur basmala
**Décisions actées** : D1 GitHub (+Pages) · D2 nom par défaut `basmala-engine` (affichage : *The Basmala Formula*) · D3 langues FR·AR·EN·FA · D4 forme v1 en SVG (3D/son en P3) · D5 licence : ouverte, à trancher.

## L'inversion (actée) : source / usine / maison / portes
**Source** = le rasm (data/, inviolé) · **Usine** = l'engine (génère, jamais ne saisit) · **MAISON** = `ledger/GRAND_LIVRE.beancount` (la forme canonique de l'état — le nom du projet réalisé) · **Portes** = Fava (professionnelle), le site-horloge (publique, une VUE du Grand Livre), les éditions LaTeX (certifiée).

## Étage 1 · Le noyau (ce dépôt)
`data` (FP, lecture seule, checksums) → `engine` (grains, charges, horloge, ancres, τ, N_clic) → `attestations` (6 scripts, 175 assertions ; chaque grandeur a deux chemins indépendants) → `build` (JSON) → `web`.
**Loi de production** : rien n'entre au moteur sans sa note (doctrine/), rien ne s'affiche sans son attestation. **CI** : audit à chaque commit ; déploiement conditionné à 0 écart. Git = registre à extournes.

## Étage 2 · Le site (l'horloge permanente)
100 % statique : position(t) déterministe côté client (ancre + année lunaire moyenne + bisect sur le cadran des 10 642 phrases). Triptyque = 56:7 spatialisé : gauche conte (−1), milieu balance (0), droite forme (+1). Maintenance annuelle : une ligne d'ancre (annonce du Ramaḍān).

## Étage 3 · Le contrôle depuis Claude
v1 : le projet Claude = le clone du dépôt (console de dev : exécuter, attester, builder, pousser — token requis).
v2 (P4) : serveur MCP « basmala » exposant position/grandeurs/jummal/anses/attestations à toute session Claude.

## Paramètres (les verrous, exposés)
année (moyenne/354/355) · ancre par année AH (table) · lieu→heure du fajr · v7 prorata (lettres/jummal) · v8 découpe des 12 livres (exercice/calendaire) · ordre (muṣḥaf/flux).
