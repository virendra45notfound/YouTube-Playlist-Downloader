## YouTube & Playlist Downloader with yt-dlp

Easily download single videos, entire playlists, or extract MP3 audio (songs) from any video or playlist on YouTube and many other supported sites—all via a simple, interactive Python script.

---

### Features

* Download individual YouTube (or supported site) videos in up to **1080p MP4** quality
* Download complete playlists at the best available quality
* Download **MP3 audio** from a single video or an entire playlist of songs
* Automatic merging of video and audio using **FFmpeg**
* Simple interactive CLI—no command-line flags needed
* Error skipping for smooth batch downloads

---

### Prerequisites

1. **Python** 3.7+ (tested up to 3.13.1)

   ```bash
   python --version
   ```
2. **yt-dlp**

   ```bash
   pip install -U yt-dlp
   ```
3. **FFmpeg** (required for 1080p+ video merging and MP3 extraction)

   * **Windows:**

     1. Go to [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
     2. Under **git master builds**, download **ffmpeg-git-full.7z** (or under **release builds**, download **ffmpeg-release-full.7z**)
     3. Extract with 7-Zip and move the folder to `C:\ffmpeg`
     4. Add `C:\ffmpeg\bin` to your **User** `PATH` environment variable
     5. Restart your terminal and verify:

        ```bash
        ffmpeg -version
        ```
   * <details>
     <summary>Linux / Mac</summary>

     **Linux (Debian/Ubuntu):**

     ```bash
     sudo apt update
     sudo apt install ffmpeg
     ```

     **macOS (Homebrew):**

     ```bash
     brew install ffmpeg
     ```

     </details>

---

### Installation

1. Clone this repository or download the script:

   ```bash
   git clone https://github.com/virendra45notfound/YouTube-Playlist-Downloader.git
   cd YouTube-Playlist-Downloader
   ```

   Or simply download the `main.py` file.
2. Ensure **yt-dlp** is installed:

   ```bash
   pip install -U yt-dlp
   ```
3. Confirm **FFmpeg** is installed and working (see prerequisites).

---

### Usage

Run the script from your terminal or command prompt:

```bash
python main.py
```

You will be prompted:

```
What do you want to download?
1. Single video (video + audio)
2. Playlist (videos + audio)
3. MP3 audio (single song or playlist)
Enter 1, 2, or 3:
```

Respond as follows:

1️⃣ **Single video**

* Enter the **video URL**
* Enter the **output directory**

2️⃣ **Playlist**

* Enter the **playlist URL**
* Enter the **output directory**

3️⃣ **MP3 audio**

* Choose:

  * `a` → Single video MP3
  * `b` → Playlist MP3
* Enter the **URL** and **output directory**

All files will be saved in your chosen directory, named after the video titles.

---

### Output

* **Videos:** MP4 files with merged audio/video up to 1080p
* **MP3 Audio:** `.mp3` files at 192 kbps by default

---

### Troubleshooting

* **No audio in some videos?**

  * Update VLC or use another modern player—some codecs (e.g., Opus) have playback issues in older versions.

* **FFmpeg errors or audio extraction fails?**

  * Double-check that `ffmpeg -version` works.

* **HTTP Error 403 or fragment not found?**

  * YouTube sometimes blocks high-res streams. The script automatically falls back to the next-best quality.

---

### License

MIT — see [LICENSE](https://opensource.org/licenses/MIT) file

---

### Credits

* **yt-dlp** for all the download and conversion magic
* **FFmpeg** for audio/video processing

Happy downloading! 🎉
