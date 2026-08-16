# Collapsi: colección de reglas no oficial

[English](README.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md)

Este repositorio contiene una colección multilingüe **no oficial** de reglas de [Collapsi](https://riffleshuffleandroll.itch.io/collapsi), el juego de estrategia abstracta inventado por **Mark S. Ball**, de Riffle Shuffle & Roll.

La publicación actual, **Collapsi Revival Edition**, documenta tanto la configuración actualizada de Mark S. Ball con Jotas para la partida estándar de 2 jugadores como la configuración anterior con Jokers. También incluye **variantes de Renacimiento** opcionales creadas por **Johann Duscher (a.k.a. Jonny Dee)**; estas siguen usando la configuración con Jokers y permiten que las cartas colapsadas vuelvan al juego de varias formas controladas. Este proyecto es independiente y no es una publicación oficial de Mark S. Ball.

## Referencia original y publicación actual

El reglamento original descargable se identifica como **Collapsi v1.3.1**, actualizado por última vez el 9 de julio de 2025. Usa dos Jotas como cartas iniciales y cada Jota permite un movimiento inicial de una casilla. Esta publicación no oficial documenta esa configuración actualizada junto con la configuración anterior con Jokers, en la que se elige un movimiento de 1, 2, 3 o 4 casillas. Las variantes de Renacimiento siguen basándose en la configuración con Jokers. Otras explicaciones en el [canal de YouTube de Riffle Shuffle & Roll](https://www.youtube.com/@riffleshuffleandroll) pueden reflejar fases distintas del desarrollo del juego original; este repositorio no deduce de ellas ningún número de versión oficial.

## Reglas

| Idioma | Markdown | PDF |
| --- | --- | --- |
| English | [Read online](docs/en/rules.md) | [Download PDF](output/pdf/collapsi-rules-en.pdf) |
| Deutsch | [Online lesen](docs/de/rules.md) | [PDF herunterladen](output/pdf/collapsi-rules-de.pdf) |
| Français | [Lire en ligne](docs/fr/rules.md) | [Télécharger le PDF](output/pdf/collapsi-rules-fr.pdf) |
| Español | [Leer en línea](docs/es/rules.md) | [Descargar PDF](output/pdf/collapsi-rules-es.pdf) |

El README raíz está en inglés porque GitHub muestra `README.md` automáticamente. Cada README y reglamento comienza con un selector de idioma compacto, para que los lectores puedan llegar a su idioma con un clic.

## Versionado

Esta colección de reglas usa su **propia versión semántica** y un nombre de edición. La publicación actual es **Collapsi Revival Edition**, versión **1.0.1**. Las publicaciones de parche compatibles conservan el nombre de edición; las que añaden variantes reciben un nombre nuevo. Las publicaciones y etiquetas Git usan `edition-vMAJOR.MINOR.PATCH`, por ejemplo `edition-v1.0.1`. Consulta la [lista de publicación](RELEASE.md), disponible en inglés, antes de publicar.

Este número identifica únicamente esta colección de reglas no oficial. Es deliberadamente independiente de versiones desconocidas o cambiantes de las reglas originales de Collapsi y no debe presentarse como una versión oficial de Collapsi. La compatibilidad con una versión concreta de las reglas originales debe documentarse en las notas de publicación, no codificarse en el número de versión.

## Estructura del repositorio

```text
docs/<idioma>/rules.md      Fuentes Markdown traducidas
output/pdf/                 PDF generados
assets/fonts/               Fuentes incluidas para una maquetación estable
scripts/build_pdfs.py       Una generación para cada idioma
.github/workflows/          Verificación automatizada de PDF
```

Los directorios de idioma usan etiquetas cortas, en minúsculas y compatibles con BCP 47, como `en`, `de`, `fr` o `pt-br`. Solo la prosa traducida pertenece a `docs/<idioma>/`. Las fuentes, la lógica de generación, las licencias, las indicaciones a contribuyentes y los flujos de trabajo se mantienen independientes del idioma en la raíz del repositorio.

## Generar los PDF

La canalización de PDF usa [ReportLab](https://www.reportlab.com/opensource/). Evita una instalación de LaTeX y dependencias nativas de renderizado HTML, a la vez que admite fuentes incrustadas, saltos de página controlados, números de página, enlaces y metadatos PDF.

```sh
uv sync --locked
uv run python scripts/build_pdfs.py
```

Las dependencias fijadas, un único renderizador compartido, fuentes Noto Sans incluidas, metadatos de publicación fijos y nombres de archivo estables hacen que las generaciones sean reproducibles. El flujo de trabajo de GitHub Actions vuelve a generar todos los idiomas y rechaza los PDF confirmados que estén obsoletos; también publica los PDF como artefacto del flujo de trabajo.

## Licencia y atribución

Los textos originales y las contribuciones de Renacimiento de Johann Duscher se ofrecen bajo [CC BY-NC-SA 4.0](LICENSE.md). Esto permite la reutilización y adaptación, pero no el uso comercial, y exige que las adaptaciones empleen la misma licencia. Mantén disponible de forma gratuita toda edición distribuida de las reglas. Collapsi en sí y el material atribuible a Mark S. Ball permanecen sujetos a sus derechos y este repositorio no los vuelve a licenciar.

Si creas una variante derivada de estas reglas de Renacimiento, conserva los créditos de Mark S. Ball y Johann Duscher. Una variante que no use ni derive de las reglas de Renacimiento no necesita atribuir a Johann Duscher. Consulta [LICENSE.md](LICENSE.md) para conocer el alcance preciso y [CONTRIBUTORS.md](CONTRIBUTORS.md) para los roles.

## Contribuir traducciones

Las nuevas traducciones son bienvenidas. La lista de comprobación de [CONTRIBUTING.md](CONTRIBUTING.md) explica cómo añadir un idioma sin duplicar la configuración de generación.
