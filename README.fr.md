# Collapsi : collection de règles non officielle

[English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md)

Ce dépôt contient une collection multilingue **non officielle** de règles de [Collapsi](https://riffleshuffleandroll.itch.io/collapsi), le jeu de stratégie abstrait inventé par **Mark S. Ball** de Riffle Shuffle & Roll.

La publication actuelle, **Collapsi Revival Edition**, présente à la fois la mise en place actualisée de Mark S. Ball avec des Valets pour la partie standard à 2 joueurs et l'ancienne mise en place avec des Jokers. Elle inclut également des **variantes de Renaissance** facultatives créées par **Johann Duscher (a.k.a. Jonny Dee)** ; celles-ci continuent d'utiliser la mise en place avec les Jokers et permettent aux cartes effondrées de revenir en jeu de plusieurs manières contrôlées. Ce projet est indépendant et n'est pas une publication officielle de Mark S. Ball.

## Référence originale et publication actuelle

Le livret de règles original téléchargeable s'identifie comme **Collapsi v1.3.1**, dernière mise à jour le 9 juillet 2025. Il utilise deux Valets comme cartes de départ, chaque Valet permettant un déplacement initial d'une case. Cette publication non officielle présente cette mise en place actualisée aux côtés de l'ancienne mise en place avec des Jokers, qui permet de choisir un déplacement de 1, 2, 3 ou 4 cases. Les variantes de Renaissance restent fondées sur la mise en place avec les Jokers. D'autres explications sur la [chaîne YouTube Riffle Shuffle & Roll](https://www.youtube.com/@riffleshuffleandroll) peuvent refléter différents stades du développement du jeu original ; ce dépôt n'en déduit aucun numéro de version officiel.

## Règles

| Langue | Markdown | PDF |
| --- | --- | --- |
| English | [Read online](docs/en/rules.md) | [Download PDF](output/pdf/collapsi-rules-en.pdf) |
| Deutsch | [Online lesen](docs/de/rules.md) | [PDF herunterladen](output/pdf/collapsi-rules-de.pdf) |
| Français | [Lire en ligne](docs/fr/rules.md) | [Télécharger le PDF](output/pdf/collapsi-rules-fr.pdf) |
| Español | [Leer en línea](docs/es/rules.md) | [Descargar PDF](output/pdf/collapsi-rules-es.pdf) |

Le README racine est en anglais parce que GitHub affiche automatiquement `README.md`. Chaque README et livret de règles commence par un sélecteur de langue compact afin que les lecteurs puissent atteindre leur langue en un clic.

## Versionnement

Cette collection de règles utilise sa **propre version sémantique** et un nom d'édition. La publication actuelle est **Collapsi Revival Edition**, version **1.0.1**. Les correctifs compatibles conservent le nom de l'édition ; les publications qui ajoutent des variantes reçoivent un nouveau nom. Les publications et balises Git emploient `edition-vMAJOR.MINOR.PATCH`, par exemple `edition-v1.0.1`. Consultez la [liste de publication](RELEASE.md), disponible en anglais, avant de publier.

Ce numéro identifie uniquement cette collection de règles non officielle. Il est volontairement indépendant des versions inconnues ou évolutives des règles originales de Collapsi et ne doit pas être présenté comme une version officielle de Collapsi. La compatibilité avec une version précise des règles originales doit être documentée dans les notes de publication plutôt que codée dans le numéro de version.

## Structure du dépôt

```text
docs/<langue>/rules.md      Sources Markdown traduites
output/pdf/                 PDF générés
assets/fonts/               Polices embarquées pour une mise en page stable
scripts/build_pdfs.py       Une génération pour toutes les langues
.github/workflows/          Vérification automatisée des PDF
```

Les répertoires de langue utilisent des étiquettes courtes, minuscules et compatibles BCP 47, comme `en`, `de`, `fr` ou `pt-br`. Seule la prose traduite se trouve sous `docs/<langue>/`. Les polices, la logique de génération, la licence, les indications aux contributeurs et les workflows restent indépendants de la langue à la racine du dépôt.

## Générer les PDF

La chaîne PDF utilise [ReportLab](https://www.reportlab.com/opensource/). Elle évite une installation LaTeX et les dépendances de rendu HTML natives, tout en prenant en charge les polices embarquées, des sauts de page maîtrisés, les numéros de page, les liens et les métadonnées PDF.

```sh
uv sync --locked
uv run python scripts/build_pdfs.py
```

Des dépendances figées, un moteur commun, des polices Noto Sans embarquées, des métadonnées de publication fixes et des noms de fichiers stables rendent les générations reproductibles. Le workflow GitHub Actions régénère toutes les langues et refuse les PDF obsolètes enregistrés ; il publie également les PDF comme artefact de workflow.

## Licence et attribution

Les textes originaux et contributions de Renaissance de Johann Duscher sont proposés sous [CC BY-NC-SA 4.0](LICENSE.md). Cette licence permet la réutilisation et l'adaptation, mais pas l'usage commercial, et impose la même licence aux adaptations. Veuillez maintenir gratuitement accessible toute édition de règles distribuée. Collapsi lui-même et les éléments attribuables à Mark S. Ball restent soumis à ses droits et ne sont pas remis sous licence par ce dépôt.

Si vous dérivez une variante de ces règles de Renaissance, conservez le crédit de Mark S. Ball et de Johann Duscher. Une variante qui n'utilise pas les règles de Renaissance ou n'en dérive pas n'a pas à attribuer Johann Duscher. Consultez [LICENSE.md](LICENSE.md) pour le périmètre exact et [CONTRIBUTORS.md](CONTRIBUTORS.md) pour les rôles.

## Contribuer aux traductions

Les nouvelles traductions sont bienvenues. La liste de contrôle dans [CONTRIBUTING.md](CONTRIBUTING.md) explique comment ajouter une langue sans dupliquer de configuration de génération.
