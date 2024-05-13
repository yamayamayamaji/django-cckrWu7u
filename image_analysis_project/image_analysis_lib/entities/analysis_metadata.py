from datetime import datetime
from pydantic import BaseModel


class AnalysisMetadata(BaseModel):
    """
    画像分析の関連データモデル

    Attributes:
        image_path (str): 分析対象の画像パス
        request_timestamp (datetime): 分析依頼時刻
        response_timestamp (datetime): 分析完了時刻
    """
    image_path: str
    request_timestamp: datetime
    response_timestamp: datetime
