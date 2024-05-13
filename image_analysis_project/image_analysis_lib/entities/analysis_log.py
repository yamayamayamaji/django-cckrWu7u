from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from .analysis_metadata import AnalysisMetadata
from .analysis_result import AnalysisResult


class AnalysisLog(BaseModel):
    image_path: str
    success: bool
    message: str
    class_id: Optional[int]
    confidence: Optional[float]
    request_timestamp: datetime
    response_timestamp: datetime

    @classmethod
    def create(cls, analysis_result: AnalysisResult, metadata: AnalysisMetadata) -> 'AnalysisLog':
        """
        AnalysisResultとAnalysisMetadataからAnalysisLogを作成します。

        Args:
            analysis_result (AnalysisResult): 分析結果
            metadata (AnalysisMetadata): 分析関連データ

        Returns:
            AnalysisLog: 作成されたAnalysisLogインスタンス
        """
        return cls(
            image_path = metadata.image_path,
            success = analysis_result.success,
            message = analysis_result.message,
            class_id = analysis_result.class_id,
            confidence = analysis_result.confidence,
            request_timestamp = metadata.request_timestamp,
            response_timestamp = metadata.response_timestamp,
        )