import os
import sys
import youtube_dl


def download_video(video_id, codec, resolution):
    if resolution not in ['480p', '720p', '1080p']:
        print("Invalid resolution, choose from: 480p, 720p, 1080p")
        return

    options = {
        'format': codec + '/' + resolution,
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'verbose': 'None',  # True zum aktivieren und 'None' zum deaktivieren
        'fast_download': 'None',  # True zum aktivieren und 'None' zum deaktivieren
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=' + video_id])


if __name__ == '__main__':
    video_id = input("Enter video id: ")
    codec = input("Enter codec (mp4): ")
    resolution = input("Enter resolution (480p/720p/1080p): ")
    download_video(video_id, codec, resolution)