from flask import Flask, Response

app = Flask(__name__)

PLAYLIST_FILE = "playlist.m3u8"

@app.route('/channel')
def channel():
    def generate():
        with open(PLAYLIST_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                yield line

    return Response(generate(), mimetype='application/vnd.apple.mpegurl')
