from yt_dlp import YoutubeDL


class YouTubeService:

    @staticmethod
    def get_video_info(url: str):

        options = {
            "quiet": True,
            "skip_download": True
        }

        with YoutubeDL(options) as ydl:

            info = ydl.extract_info(
                url,
                download=False
            )

        return info