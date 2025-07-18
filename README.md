# YouTube & Playlist Downloader (CLI Version)

A simple command-line Python script for downloading YouTube single videos, playlists, or MP3 audio files using **yt-dlp** and **FFmpeg**.

---

## Features

* Download a single video (up to 1080p) with audio merged into MP4 format.
* Download an entire playlist of videos.
* Extract MP3 audio from a single video or an entire playlist.
* Customizable output directory structure.

---

## Dependencies

* Python 3.6 or higher
* [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* [FFmpeg](https://www.ffmpeg.org/) (must be installed and in your system PATH)

### Install Python Package Dependencies

```bash
pip install yt-dlp
```

> Note: No additional Python wrapper for FFmpeg is required; yt-dlp handles audio extraction via FFmpeg internally.

### Install FFmpeg

* **macOS (Homebrew):**

  ```bash
  brew install ffmpeg
  ```
* **Ubuntu/Debian:**

  ```bash
  sudo apt update && sudo apt install ffmpeg
  ```
* **Windows:**

  1. Download a static build from [ffmpeg.org/download.html](https://www.gyan.dev/ffmpeg/builds/#git-master-builds), ffmpeg-git-full.7z.
  2. Extract it in a simpler folder path like C:\ and add the `bin/` folder to your system’s PATH environment variable.

---

## Usage

1. Clone or download the `main` branch of this repository:

   ```bash
   git clone -b main https://github.com/virendra45notfound/YouTube-Playlist-Downloader.git
   cd YouTube-Playlist-Downloader
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. Follow the prompts:

   ```text
   What do you want to download?
   1. Single video (video+audio)
   2. Playlist (videos+audio)
   3. MP3 audio (single song or playlist)
   Enter 1, 2, or 3:
   ```

4. Based on your selection, input the URL and the output directory when asked.

### Examples

* **Single Video**

  ```text
  Choice: 1
  Video URL: https://www.youtube.com/watch?v=ABC123
  Output Directory: downloads/video
  ```

* **Playlist**

  ```text
  Choice: 2
  Playlist URL: https://www.youtube.com/playlist?list=XYZ789
  Output Directory: downloads/playlist
  ```

* **MP3 Audio (Single)**

  ```text
  Choice: 3
  Sub-choice: a  # single song
  Video URL: https://www.youtube.com/watch?v=ABC123
  Output Directory: downloads/audio
  ```

* **MP3 Audio (Playlist)**

  ```text
  Choice: 3
  Sub-choice: b  # playlist
  Playlist URL: https://www.youtube.com/playlist?list=XYZ789
  Output Directory: downloads/audio_playlist
  ```

---

## Configuration

* **output\_path**: Directory where downloads are saved (created automatically).
* **Video Quality**: Best available video up to 1080p plus best audio.
* **Audio Quality**: MP3 at 192 kbps.

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.
