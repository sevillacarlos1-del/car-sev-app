import pathlib
import streamlit

def patch_streamlit_index():
    """
    Encuentra la ruta física del archivo index.html dentro del paquete instalado 
    de Streamlit e inyecta la etiqueta <link rel="manifest"> en el <head> raíz.
    """
    index_path = pathlib.Path(streamlit.__file__).parent / "static" / "index.html"

    if not index_path.exists():
        print("❌ No se encontró el archivo index.html de Streamlit.")
        return

    html_content = index_path.read_text(encoding="utf-8")

    manifest_tag = '<link rel="manifest" href="/app/static/manifest.json">'

    if manifest_tag not in html_content:
        pwa_head_tags = '''
    <!-- PWA Manifest & Meta Tags Inyectados -->
    <link rel="manifest" href="/app/static/manifest.json">
    <link rel="apple-touch-icon" href="/app/static/logo_192.png">
    <meta name="theme-color" content="#1E293B">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
</head>'''

        updated_content = html_content.replace("</head>", pwa_head_tags)
        index_path.write_text(updated_content, encoding="utf-8")
        print("✅ Streamlit index.html parcheado con éxito para PWA Manifest!")
    else:
        print("ℹ️ Streamlit index.html ya contiene la etiqueta rel=\"manifest\".")

if __name__ == "__main__":
    patch_streamlit_index()
