from flask import Flask, Response

app = Flask(__name__)

PLAYLIST_FILE = "playlist.m3u8"

@app.route('/channel')
def channel():
    def generate():
        while True:
            with open(PLAYLIST_FILE, 'r') as f:
                for line in f:
                    yield line
    return Response(generate(), mimetype='application/vnd.apple.mpegurl')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)