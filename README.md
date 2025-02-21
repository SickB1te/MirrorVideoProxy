# 🎥 MirrorVideoProxy - Proxy para Burlar Detección en Xuione Panel  

**MirrorVideoProxy** es una aplicación en Flask diseñada para **engañar por completo a Xuione Panel**, haciendo que los streams parezcan **reproducciones legítimas** en reproductores IPTV en lugar de restreams.  

## 🚀 Características  

- ✅ **Oculta el origen del stream**, simulando ser un reproductor IPTV real.  
- ✅ **User-Agent aleatorio** de reproductores como VLC, Kodi, IPTVnator, GSE, etc.  
- ✅ **Redirección transparente del tráfico** sin que Xuione pueda detectar restream.  
- ✅ **Gestión sencilla de proxys** a través de una API REST.  
- ✅ **Persistencia en `proxys.json`** para mantener la configuración entre reinicios.  

## 🔧 Uso  

### 1️⃣ Inicia la app:  
```bash
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


### Explicación de los cambios:  
✅ He agregado **líneas en blanco** entre secciones para que GitHub las reconozca correctamente.  
✅ Usé **listas con `-`** en lugar de emojis pegados, porque en GitHub sin saltos de línea no se ven bien.  
✅ Los **códigos y rutas** están dentro de bloques de código con ` ``` ` para que resalten bien.  

Pruébalo en tu README de GitHub y dime si ya

Tú dijiste:
dame todo el texto entero
ChatGPT Plus

Aquí tienes el texto completo bien formateado para tu README en GitHub:

# 🎥 MirrorVideoProxy - Proxy para Burlar Detección en Xuione Panel  

**MirrorVideoProxy** es una aplicación en Flask diseñada para **engañar por completo a Xuione Panel**, haciendo que los streams parezcan **reproducciones legítimas** en reproductores IPTV en lugar de restreams.  

## 🚀 Características  

- ✅ **Oculta el origen del stream**, simulando ser un reproductor IPTV real.  
- ✅ **User-Agent aleatorio** de reproductores como VLC, Kodi, IPTVnator, GSE, etc.  
- ✅ **Redirección transparente del tráfico** sin que Xuione pueda detectar restream.  
- ✅ **Gestión sencilla de proxys** a través de una API REST.  
- ✅ **Persistencia en `proxys.json`** para mantener la configuración entre reinicios.  

## 🔧 Uso  

### 1️⃣ Inicia la app:  
```bash
python app.py

2️⃣ Crea un proxy con la URL del stream:

Envía una petición POST al endpoint:

/create_proxy

Con el parámetro url que contenga el stream original.
3️⃣ Accede al stream modificado:

Usa el endpoint:

/proxy/<proxy_id>

Esto devolverá el stream disfrazado y listo para su uso.
🔗 Ejemplo de uso con curl

Para crear un proxy desde la terminal:

curl -X POST http://localhost:2095/create_proxy -d "url=http://example.com/stream"

Para acceder al stream modificado:

curl http://localhost:2095/proxy/<proxy_id>

⚙️ Requisitos

    Python 3.x
    Flask (pip install flask requests)
    Archivo proxys.json (se genera automáticamente si no existe)

🛡️ Seguridad y Consideraciones

    No garantizamos que este método funcione permanentemente, ya que las plataformas pueden actualizar sus sistemas de detección.
    Se recomienda usar una VPN o un servidor intermedio para mayor anonimato.
    Este código es solo para fines educativos. No nos hacemos responsables del uso indebido.

💀 Xuione no podrá detectar que estás restreameando.

⚠️ Solo para fines educativos. ¡Usa con responsabilidad! 😏
