# API client library
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import random


def get_youtube_client():
    # API information
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = ""

    # API client
    youtube = build(api_service_name, api_version, developerKey=DEVELOPER_KEY)
    return youtube


def get_latest_videos(query="song", type="video", maxResults=10, order="date"):
    try:
        part = "snippet"
        publishedAfter = "2022-06-24T15:30:00Z"
        youtube = get_youtube_client()

        request = youtube.search().list(
            part=part,
            publishedAfter=publishedAfter,
            q=query,
            type=type,
            maxResults=maxResults,
        )

        response = request.execute()
        response = random.choice(response["items"])
        response = f'https://www.youtube.com/watch?v={response["id"]["videoId"]}'
        return response
    except HttpError as e:
        return "https://www.youtube.com/watch?v=bxnYFOixIoc"
