from fastapi import APIRouter, HTTPException
from models.request_model import VideoLink
from services.youtube_service import extract_comments, extract_video_id
from services.textBlob_analyser_service import analyze_sentiment

router = APIRouter()

@router.post("/analyse")
async def fetch_comments(data: VideoLink):
    video_id = extract_video_id(data.url)
    if not video_id:
        raise HTTPException(status_code=400, detail="Invalid YouTube URL")

    try:
        comments = extract_comments(video_id, data.comment_count)
        sentiment_data, sentiment_percent = analyze_sentiment(comments)
        return {
            "video_id": video_id,
            "total_comments": len(comments),
            "sentiment_breakdown": {
                "positive": len(sentiment_data["positive"]),
                "neutral": len(sentiment_data["neutral"]),
                "negative": len(sentiment_data["negative"])
            },
            "sentiment_percentage": sentiment_percent,
            "comments_by_sentiment": sentiment_data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
