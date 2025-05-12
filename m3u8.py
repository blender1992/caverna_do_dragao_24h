from flask import Flask, Response
import os

app = Flask(__name__)

PLAYLIST_FILE = "playlist.m3u8"

@app.route('/channel')
def channel():
    def generate():
        with open(PLAYLIST_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                yield line

    return Response(generate(), mimetype='application/vnd.apple.mpegurl')

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))  # Usa PORT do Render, se não tiver usa 8080
    app.run(host='0.0.0.0', port=port)
