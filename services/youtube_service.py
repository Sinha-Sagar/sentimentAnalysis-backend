from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def extract_video_id(url: str) -> str:
    parsed_url = urlparse(url)
    if parsed_url.hostname == 'youtu.be':
        return parsed_url.path[1:]
    elif parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
        query = parse_qs(parsed_url.query)
        return query.get('v', [None])[0]
    return ""

def extract_comments(video_id: str, max_total: int = 20):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    comments = []
    next_page_token = None

    while len(comments) < max_total:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            textFormat="plainText",
            pageToken = next_page_token
        )

        response = request.execute()

        for item in response.get('items', []):
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)

        # Stop if there are no more pages
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return comments[:max_total]