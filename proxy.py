from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
from datetime import datetime
import os
import requests
import uuid
import json
import random
import re
from urllib.parse import urlparse

app = Flask(__name__)

# Lista de user agents de reproductores IPTV
iptv_user_agents = [
    "VLC/3.0.11.1 LibVLC/3.0.11.1",
    "Kodi/19.3 (Windows NT 10.0; Win64; x64) App_Sync/1.0",
    "IPTVnator/1.0 (Windows; x64) Lib/1.0",
    "Perfect Player/1.3.6 (Android; TV)",
    "GSE SMART IPTV/2.0 (Android; TV)"
]

# ---------------------------
# Funciones para manejo del JSON
# ---------------------------
def load_proxys():
    """Carga y sanea el JSON de proxys, eliminando entradas corruptas sin recrear el archivo."""
    try:
        with open('proxys.json', 'r', encoding="utf-8") as f:
            data = f.read().strip()
            if not data:
                return []
            try:
                proxys = json.loads(data)
            except json.JSONDecodeError as e:
                # Intentar quitar comas finales en objetos y arrays
                data_clean = re.sub(r',(\s*[}\]])', r'\1', data)
                proxys = json.loads(data_clean)
            saneados = []
            for proxy in proxys:
                # Solo consideramos entradas que sean diccionarios y tengan la clave 'original_url'
                if isinstance(proxy, dict) and 'original_url' in proxy:
                    if 'proxy_id' not in proxy or not isinstance(proxy['proxy_id'], str):
                        proxy['proxy_id'] = uuid.uuid4().hex[:6]
                    if 'proxy_url' not in proxy or not isinstance(proxy['proxy_url'], str):
                        proxy['proxy_url'] = f"/proxy/{proxy['proxy_id']}"
                    saneados.append(proxy)
            if len(saneados) < len(proxys):
                print("⚠️ Se eliminaron entradas corruptas del JSON.")
            return saneados
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("⚠️ Error al leer proxys.json, intentando sanear...", e)
        return []

def save_proxys(proxys):
    """Guarda los proxys en proxys.json de forma segura."""
    try:
        with open("proxys.json", "w", encoding="utf-8") as f:
            json.dump(proxys, f, indent=4)
    except Exception as e:
        print(f"⚠️ Error al guardar proxys.json: {e}")

def is_valid_url(url):
    """Verifica si una URL es válida."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# ---------------------------
# Rutas de la Aplicación
# ---------------------------
@app.route('/api/proxys', methods=['GET'])
def api_proxys():
    """Devuelve la lista de proxys en JSON."""
    proxys = load_proxys()
    return jsonify(proxys)

@app.route('/create_proxy', methods=['POST'])
def create_proxy():
    """Crea un nuevo proxy y lo guarda en proxys.json."""
    target_url = request.form.get('url')
    if target_url and is_valid_url(target_url):
        proxys = load_proxys()
        proxy_id = uuid.uuid4().hex[:6]
        proxy_info = {
            'original_url': target_url,
            'proxy_url': f"/proxy/{proxy_id}",
            'start_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'id': len(proxys),
            'proxy_id': proxy_id
        }
        proxys.append(proxy_info)
        save_proxys(proxys)
        return jsonify({"message": "Proxy creado", "proxy": proxy_info})
    return jsonify({"error": "URL no válida"}), 400

@app.route('/proxy/<proxy_id>', methods=['GET'])
def handle_proxy(proxy_id):
    """Redirige las peticiones a la URL original del proxy."""
    proxys = load_proxys()
    proxy = next((p for p in proxys if p['proxy_id'] == proxy_id), None)
    if not proxy:
        return "Error: Proxy no encontrado.", 404

    target_url = proxy['original_url']
    user_agent = random.choice(iptv_user_agents)
    headers = {"User-Agent": user_agent}

    try:
        resp = requests.get(target_url, stream=True, headers=headers, timeout=10)
        if resp.status_code != 200:
            return f"Error: No se pudo conectar a {target_url}", 500
        
        def generate():
            for chunk in resp.iter_content(chunk_size=4096):
                if chunk:
                    yield chunk
        
        return Response(generate(), content_type=resp.headers.get('Content-Type', 'application/octet-stream'))
    except Exception as e:
        print(f"Error al conectar con {target_url}: {e}")
        return "Error en la conexión con el stream.", 500

@app.route('/delete_proxy/<proxy_id>', methods=['DELETE'])
def delete_proxy(proxy_id):
    """Elimina un proxy por su ID."""
    proxys = load_proxys()
    new_proxys = [p for p in proxys if p['proxy_id'] != proxy_id]
    if len(new_proxys) == len(proxys):
        return jsonify({"error": "Proxy no encontrado"}), 404
    save_proxys(new_proxys)
    return jsonify({"message": f"Proxy {proxy_id} eliminado"})

@app.route('/')
def index():
    """Muestra la página principal con los proxys cargados."""
    proxys = load_proxys()
    return render_template('index.html', proxys=proxys)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2095)
