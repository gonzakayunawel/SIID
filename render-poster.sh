#!/usr/bin/env bash
# Renderiza el poster, asegurando que el logo de UNAB esté disponible para Typst.
#
# Typst resuelve rutas de imágenes relativas a su directorio de paquete
# (.quarto/typst/packages/local/typst-poster/0.1.1/), no al directorio del .qmd.
# Por eso hay que copiar el logo ahí antes de renderizar.

set -e

LOGO_SRC="poster/images/unab.png"
LOGO_DST="poster/.quarto/typst/packages/local/typst-poster/0.1.1/images/unab.png"

# Renderizar (esto regenera .quarto/ si no existe)
quarto render poster/poster.qmd 2>/dev/null || true

# Copiar logo al cache de Typst y re-renderizar
mkdir -p "$(dirname "$LOGO_DST")"
cp "$LOGO_SRC" "$LOGO_DST"
quarto render poster/poster.qmd

echo "✓ poster/poster.pdf generado"
