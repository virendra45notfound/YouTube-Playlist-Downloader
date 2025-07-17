# YouTube & Playlist Downloader

A sleek, modern Flask app for downloading YouTube videos, playlists, or MP3 audio using **yt-dlp** and **FFmpeg**.

---

## Features

* Download single videos (up to 1080p) in MP4 format.
* Download entire playlists of videos.
* Extract MP3 audio from single videos or playlists.
* Interactive, responsive UI with real-time status updates.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/virendra45notfound/YouTube-Playlist-Downloader.git
   cd YouTube-Playlist-Downloader
   
   ```
2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Ensure **FFmpeg** is installed and available in your PATH.

## Project Structure

```
yt-downloader/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css    # Updated modern dark theme stylesheet
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

## Styling Notes

* The **style.css** now lives in `static/style.css` and contains a modern dark mode theme using CSS variables.
* Key improvements:

  * **Dark background** with vibrant accent (`#ff005b`).
  * **Responsive layout** for mobile screens.
  * **Button alignment fixed** via `display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem;`.
  * Browser caching issues can be resolved by doing a **hard reload** (Ctrl+Shift+R).

> If you make further CSS changes, ensure the file path in `index.html` matches exactly:
>
> ```html
> <link rel="stylesheet" href="{{ url_for('sta
> ```
