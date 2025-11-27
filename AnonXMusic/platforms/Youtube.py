import asyncio
import os
import re
import yt_dlp

from youtube_search import YoutubeSearch
from typing import Union


YTDLP_OPTS_BASE = {
    "quiet": True,
    "nocheckcertificate": True,
    "geo_bypass": True,
    "no_warnings": True,
    "cookiefile": os.path.expanduser("~/.config/yt-dlp/cookies.txt"),
}


class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="

    async def search(self, query: str):
        results = YoutubeSearch(query, max_results=1).to_dict()
        if not results:
            return None

        r = results[0]
        return {
            "title": r["title"],
            "id": r["id"],
            "duration": r["duration"],
            "url": f"https://www.youtube.com{r['url_suffix']}",
            "thumb": r["thumbnails"][0],
        }

    async def get_formats(self, url: str):
        ytdlp_opts = {
            **YTDLP_OPTS_BASE,
            "skip_download": True,
        }

        with yt_dlp.YoutubeDL(ytdlp_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        formats = []
        for f in info.get("formats", []):
            if f.get("acodec") != "none":
                formats.append({
                    "format_id": f.get("format_id"),
                    "ext": f.get("ext"),
                    "filesize": f.get("filesize"),
                    "vcodec": f.get("vcodec"),
                    "acodec": f.get("acodec"),
                    "url": url,
                })
        return formats

    async def download_audio(self, url: str, title: str):
        os.makedirs("downloads", exist_ok=True)
        file_path = f"downloads/{title}.mp3"

        ytdlp_opts = {
            **YTDLP_OPTS_BASE,
            "format": "bestaudio",
            "outtmpl": file_path,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }

        def run():
            with yt_dlp.YoutubeDL(ytdlp_opts) as ydl:
                ydl.download([url])

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, run)

        return file_path
