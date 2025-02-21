# 🎥 MirrorVideoProxy - Proxy para Burlar Detección en Xuione Panel  

MirrorVideoProxy es una aplicación en Flask diseñada para **engañar por completo a Xuione Panel**, haciendo que los streams parezcan reproducciones legítimas en reproductores IPTV en lugar de restreams.  

## 🚀 Características  

✅ **Oculta el origen del stream**, simulando ser un reproductor IPTV real.  
✅ **User-Agent aleatorio** de reproductores como VLC, Kodi, IPTVnator, GSE, etc.  
✅ **Redirección transparente** del tráfico sin que Xuione pueda detectar restream.  
✅ **Gestión sencilla** de proxys a través de una API REST.  
✅ **Persistencia en `proxys.json`** para mantener la configuración entre reinicios.  

## 🔧 Uso  

### 1️⃣ Inicia la app:  
```bash
python app.py
