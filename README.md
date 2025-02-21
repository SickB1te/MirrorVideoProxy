🎥 MirrorVideoProxy - Proxy para IPTV y Streaming

MirrorVideoProxy es una aplicación en Flask que permite crear y gestionar proxys para retransmisión de contenido IPTV.
🚀 Características

✅ Creación de proxys dinámicos para URLs de streaming.
✅ Simulación de User Agents de reproductores IPTV (VLC, Kodi, Perfect Player, etc.).
✅ Gestión de proxys a través de una API REST.
✅ Almacenamiento persistente en proxys.json.
✅ Redirección automática del tráfico al enlace original.
🔧 Uso

1️⃣ Ejecuta la app con:

python app.py

2️⃣ Crea un proxy enviando una URL al endpoint /create_proxy.
3️⃣ Accede al contenido a través de la ruta /proxy/<proxy_id>.

Ideal para retransmisión privada, evadir restricciones geográficas y optimizar el acceso a streams. 🎬
