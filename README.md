# YouTube & Playlist Downloader

A sleek, modern Flask app for downloading YouTube videos, playlists, or MP3 audio using **yt-dlp** and **FFmpeg**.

> **Note:** Active development is currently happening on the [`app`](https://github.com/virendra45notfound/YouTube-Playlist-Downloader/tree/app) branch.

---

## Features

* Download single videos (up to 1080p) in MP4 format.
* Download entire playlists of videos.
* Extract MP3 audio from single videos or playlists.
* Interactive, responsive UI with real-time status updates.

## Installation

1. Clone the `app` branch of this repository:

   ```bash
   git clone -b app https://github.com/virendra45notfound/YouTube-Playlist-Downloader.git
   cd YouTube-Playlist-Downloader
   ```
2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies (Flask, yt-dlp, FFmpeg wrapper):

   ```bash
   pip install -r requirements.txt
   ```
4. Ensure **FFmpeg** is installed and available in your PATH.

   * macOS (Homebrew):

     ```bash
     brew install ffmpeg
     ```
   * Ubuntu/Debian:

     ```bash
     sudo apt install ffmpeg
     ```
   * Windows:
     Download from [https://ffmpeg.org/download.html](https://www.gyan.dev/ffmpeg/builds/#git-master-builds) ffmpeg-git-full.7z, extract it to a simpler directory like in C:\ and add the bin folder inside of the extracted folder to your system PATH.
     
     Check if ffmpeg is installed correctly or not by running the following command in command prompt

     ```bash
     ffmpeg -version
     ```

## Project Structure

```
YouTube-Playlist-Downloader/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── styles.css   
└── downloads/       # Where downloaded files are saved
```

## Usage

1. Run the Flask app:

   ```bash
   python app.py
   ```
2. Open your browser and go to `http://127.0.0.1:5000`.
3. Select a download type (Video, Playlist, or MP3).
4. Paste your YouTube URL.
5. Click **Start Download**.


## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.
