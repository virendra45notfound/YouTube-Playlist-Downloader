import os
import threading
from flask import Flask, render_template, request, jsonify

import yt_dlp

app = Flask(__name__)

DOWNLOAD_DIR = os.path.join(os.path.dirname(__file__), "downloads")

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def yt_download_job(url, otype, subchoice, status_dict):
    try:
        ensure_dir(DOWNLOAD_DIR)

        if otype == "video":
            ydl_opts = {
                'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
                'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]/best',
                'merge_output_format': 'mp4',
                'noplaylist': True,
                'ignoreerrors': True,
                'quiet': False
            }
        elif otype == "playlist":
            ydl_opts = {
                'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
                'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]/best',
                'merge_output_format': 'mp4',
                'noplaylist': False,
                'ignoreerrors': True,
                'quiet': False
            }
        elif otype == "mp3":
            is_playlist = (subchoice == "playlist")
            ydl_opts = {
                'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'noplaylist': not is_playlist,
                'ignoreerrors': True,
                'quiet': False
            }
        else:
            status_dict['result'] = 'Invalid type'
            return

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        status_dict['result'] = 'Download complete! Files saved in "downloads" folder.'
    except Exception as e:
        status_dict['result'] = f"Error: {str(e)}"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url", "")
    download_type = request.form.get("download_type", "")
    mp3_subchoice = request.form.get("mp3_subchoice", "")
    status = {}
    thread = threading.Thread(
        target=yt_download_job, args=(url, download_type, mp3_subchoice, status))
    thread.start()
    thread.join()  # Synchronous for demo; for async, remove this and return immediately
    return jsonify(status)

if __name__ == "__main__":
    app.run(debug=True)
