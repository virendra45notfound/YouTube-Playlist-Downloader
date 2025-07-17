YouTube & Playlist Downloader with yt-dlp
Easily download single videos, entire playlists, or extract MP3 audio (songs) from any video or playlist on YouTube and many other sites—all via a user-friendly Python script!

Features
Download individual YouTube (or supported site) videos in up to 1080p MP4 quality

Download complete playlists at the best available quality

Download MP3 audio from a single video or an entire playlist of songs

Automatic merging of video and audio using FFmpeg

Simple interactive CLI—no command-line flags needed

Error skipping for smooth batch downloads

Prerequisites
Python
You need Python 3.7+ (tested up to Python 3.13.1).
You can check your version with:

text
python --version
yt-dlp
Install via pip:

text
pip install -U yt-dlp
FFmpeg
Required for merging audio/video in 1080p+ and for audio extraction (MP3).
See Windows install instructions below.

Installation
Clone this repository or download the script

text
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
Or simply save the .py script from this repo.

Make sure yt-dlp is installed

text
pip install -U yt-dlp
Install FFmpeg (Windows instructions)

Go to: https://www.gyan.dev/ffmpeg/builds/

Under "git master builds", download ffmpeg-git-full.7z (or under "release builds", download ffmpeg-release-full.7z).

Extract the downloaded .7z file using 7-Zip.

Move the extracted folder (e.g., ffmpeg) to C:\ffmpeg for convenience.

Add the C:\ffmpeg\bin directory to your system PATH environment variable:

Press Windows Key, search "Edit environment variables for your account"

Click "Path" under "User variables" → Edit → New → Paste C:\ffmpeg\bin → OK all dialogs.

Open a new Command Prompt and check:

text
ffmpeg -version
If version info shows up, you're done.

<details> <summary>Linux/Mac</summary>
Linux (Debian/Ubuntu):

text
sudo apt update
sudo apt install ffmpeg
Mac (Homebrew):

text
brew install ffmpeg
</details>
Usage
Run the script from a terminal/command prompt:

text
python your_script.py
You will be prompted:
text
What do you want to download?
1. Single video (video+audio)
2. Playlist (videos+audio)
3. MP3 audio (single song or playlist)
Enter 1, 2, or 3:
Respond as follows:

1 → Enter a single video URL and output directory.

2 → Enter a playlist URL and output directory.

3 → Will further prompt:

a → Enter single video URL and output directory for one MP3 song

b → Enter playlist URL and output directory for all songs in MP3

All downloaded files will be saved in the provided directory, using the YouTube video/title as the filename.

Output
Videos: MP4 format with merged audio/video up to 1080p.

MP3 Audio: .mp3 files, 192kbps by default.

Troubleshooting
No audio in some files?
Update VLC or use another modern player; some recent codec regressions in VLC can cause MP4+Opus playback issues.

FFmpeg errors or audio extraction fails?
Double-check that FFmpeg is installed and ffmpeg -version works in your terminal/command prompt.

HTTP Error 403, fragment not found?
Occasionally, YouTube blocks some high-res streams. The script will automatically fall back to the next-best available quality.

License
MIT — see LICENSE file.

Credits
yt-dlp for all the download and conversion magic.

FFmpeg for audio/video processing.

Happy downloading!