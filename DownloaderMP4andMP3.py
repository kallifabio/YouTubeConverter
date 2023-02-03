import os
import sys
import youtube_dl


def download_video(video_id, codec, resolution):
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
    codec = input("Enter codec (best/worst): ")
    resolution = input("Enter resolution (360p/720p/1080p): ")
    download_video(video_id, codec, resolution)