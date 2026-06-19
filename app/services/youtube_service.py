from youtube_transcript_api import YouTubeTranscriptApi


class YouTubeService:

    @staticmethod
    def get_farsi_subtitle(video_id: str):

        transcript = (
            YouTubeTranscriptApi
            .get_transcript(
                video_id,
                languages=["fa"]
            )
        )

        return transcript