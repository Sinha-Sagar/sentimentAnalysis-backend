from pydantic import BaseModel

class VideoLink(BaseModel):
    url: str
    comment_count: int