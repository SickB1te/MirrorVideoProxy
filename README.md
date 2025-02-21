🎥 MirrorVideoProxy - Proxy para Burlar Detección en Xuione Panel

MirrorVideoProxy es una aplicación en Flask diseñada para engañar por completo a Xuione Panel, haciendo que los streams parezcan reproducciones legítimas en reproductores IPTV en lugar de restreams.
🚀 Características

✅ Oculta el origen del stream, simulando ser un reproductor IPTV real.
✅ User-Agent aleatorio de reproductores como VLC, Kodi, IPTVnator, GSE, etc.
✅ Redirección transparente del tráfico sin que Xuione pueda detectar restream.
✅ Gestión sencilla de proxys a través de una API REST.
✅ Persistencia en proxys.json para mantener la configuración entre reinicios.
🔧 Uso
1️⃣ Inicia la app:

python app.py

2️⃣ Crea un proxy con la URL del stream:

Envía una petición POST al endpoint:

/create_proxy  

Con el parámetro url que contenga el stream original.
3️⃣ Accede al stream modificado:

Usa el endpoint:

/proxy/<proxy_id>

Esto devolverá el stream disfrazado y listo para su uso.
💀 Xuione no podrá detectar que estás restreameando.

⚠️ Solo para fines educativos. ¡Usa con responsabilidad! 😏
