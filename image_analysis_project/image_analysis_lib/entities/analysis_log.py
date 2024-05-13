from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class AnalysisLog(BaseModel):
    image_path: str
    success: bool
    message: str
    class_id: Optional[int]
    confidence: Optional[float]
    request_timestamp: datetime
    response_timestamp: datetime
