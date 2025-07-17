import yt_dlp
import os

def download_video(video_url, output_path):
    os.makedirs(output_path, exist_ok=True)
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]/best',
        'merge_output_format': 'mp4',
        'noplaylist': True,
        'ignoreerrors': True,
        'quiet': False
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def download_playlist(playlist_url, output_path):
    os.makedirs(output_path, exist_ok=True)
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]/best',
        'merge_output_format': 'mp4',
        'noplaylist': False,   # Download ENTIRE playlist
        'ignoreerrors': True,
        'quiet': False
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def download_mp3(url, output_path, is_playlist):
    os.makedirs(output_path, exist_ok=True)
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': not is_playlist,  # True for single song, False for playlist
        'ignoreerrors': True,
        'quiet': False
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    print("What do you want to download?")
    print("1. Single video (video+audio)")
    print("2. Playlist (videos+audio)")
    print("3. MP3 audio (single song or playlist)")
    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        video_url = input("Enter the video URL: ")
        output_path = input("Enter the output directory: ")
        download_video(video_url, output_path)
    elif choice == "2":
        playlist_url = input("Enter the playlist URL: ")
        output_path = input("Enter the output directory: ")
        download_playlist(playlist_url, output_path)
    elif choice == "3":
        print("MP3 audio download selected.")
        print("a. Single song (video URL)")
        print("b. Playlist of songs (playlist URL)")
        sub_choice = input("Enter 'a' or 'b': ").strip().lower()
        if sub_choice == "a":
            song_url = input("Enter the video URL: ")
            output_path = input("Enter the output directory: ")
            download_mp3(song_url, output_path, is_playlist=False)
        elif sub_choice == "b":
            playlist_url = input("Enter the playlist URL: ")
            output_path = input("Enter the output directory: ")
            download_mp3(playlist_url, output_path, is_playlist=True)
        else:
            print("Invalid choice for MP3 download. Exiting.")
    else:
        print("Invalid choice. Please run the script again and enter 1, 2, or 3.")

