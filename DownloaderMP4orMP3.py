import sys
import youtube_dl


def download_video(video_id, codec, resolution):
    ydl_opts = {}

    if codec == 'mp3':
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': codec,
                'preferredquality': '192',
            }],
            'verbose': 'None',  # True zum aktivieren und 'None' zum deaktivieren
            'fast_download': 'None',  # True zum aktivieren und 'None' zum deaktivieren
        }
    elif codec == 'mp4':
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'verbose': 'None',  # True zum aktivieren und 'None' zum deaktivieren
            'fast_download': 'None',  # True zum aktivieren und 'None' zum deaktivieren
        }
        if resolution:
            ydl_opts['format'] = f'{resolution}/bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
    else:
        print("Error: Unsupported codec")
        sys.exit()

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=' + video_id])


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python downloader.py <youtube_watch_id> <codec> <resolution>")
        sys.exit()
    video_id = sys.argv[1]
    codec = sys.argv[2]
    resolution = sys.argv[3] if sys.argv[3] != 'None' else None
    download_video(video_id, codec, resolution)