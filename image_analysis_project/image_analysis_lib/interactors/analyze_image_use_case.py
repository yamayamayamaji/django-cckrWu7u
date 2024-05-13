from datetime import datetime
from pydantic import BaseModel
from ..entities import AnalysisLog, AnalysisResult
from .use_case_interface import UseCaseInterface
from ..repositories.ai_analysis_log_repository_interface import AIAnalysisLogRepositoryInterface
# 
from django.utils import timezone
import time


class AnalyzeImageInput(BaseModel):
    image_path: str

class AnalyzeImageOutput(BaseModel):
    log_id: int
    image_path: str

class AnalyzeImageUseCase(UseCaseInterface):
    def __init__(self, repository: AIAnalysisLogRepositoryInterface):
        self._repository = repository

    def execute(self, input: AnalyzeImageInput) -> AnalyzeImageOutput:
        request_timestamp = timezone.now()

        # 仮実装 TODO
        analysis_result = AnalysisResult(
            success = True,
            message = 'success',
            class_id = 3,
            confidence = 0.8683,
        )
        if input.image_path.endswith("failure.jpg"):
            analysis_result = AnalysisResult(
                success = False,
                message = 'Error:E50012',
                class_id = None,
                confidence = None,
            )

        response_timestamp = timezone.now()

        log = AnalysisLog(
            image_path = input.image_path,
            success = analysis_result.success,
            message = analysis_result.message,
            class_id = analysis_result.class_id,
            confidence = analysis_result.confidence,
            request_timestamp = request_timestamp,
            response_timestamp = response_timestamp,
        )

        log_id = self._repository.save(log)

        return AnalyzeImageOutput(
            log_id=log_id,
            image_path=input.image_path,
        )
