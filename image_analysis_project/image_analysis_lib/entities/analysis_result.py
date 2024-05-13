from pydantic import BaseModel
from typing import Optional


class AnalysisResult(BaseModel):
    """
    画像分析APIのレスポンスモデル

    Attributes:
        success (bool): 分析の成功フラグ
        message (str): 分析結果のメッセージ
        class_id (int): 分析結果のクラスID
        confidence (float): 分析結果の信頼度
    """
    success: bool
    message: str
    class_id: Optional[int] = None
    confidence: Optional[float] = None
