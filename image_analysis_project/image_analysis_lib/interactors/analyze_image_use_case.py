from pydantic import BaseModel
from ..entities import AnalysisLog, AnalysisMetadata, AnalysisResult
from .use_case_interface import UseCaseInterface
from ..repositories.ai_analysis_log_repository_interface import AIAnalysisLogRepositoryInterface
# 
from ..gateway.ai_image_analysis_service import AIImageAnalysisService
from django.utils import timezone


class AnalyzeImageInput(BaseModel):
    """
    AnalyzeImageUseCaseの入力モデル

    Attributes:
        image_path (str): 分析対象の画像パス
    """
    image_path: str

class AnalyzeImageOutput(BaseModel):
    """
    AnalyzeImageUseCaseの出力モデル

    Attributes:
        log_id (int): 記録した分析ログのID
        image_path (str): 分析対象の画像パス
    """
    log_id: int
    image_path: str

class AnalyzeImageUseCase(UseCaseInterface):
    """
    画像分析を行うユースケースクラス

    Attributes:
        _repository (AIAnalysisLogRepositoryInterface): 分析ログを永続化するためのリポジトリ
    """

    def __init__(self, repository: AIAnalysisLogRepositoryInterface):
        """
        コンストラクタ

        Args:
            repository (AIAnalysisLogRepositoryInterface): 分析ログを永続化するためのリポジトリ
        """
        self._repository = repository

    def execute(self, input: AnalyzeImageInput) -> AnalyzeImageOutput:
        """
        ユースケースを実行します。

        Args:
            input (AnalyzeImageInput): 分析対象の画像ファイルパスを含む入力データ

        Returns:
            AnalyzeImageOutput: 分析ログのIDと画像ファイルパスを含む出力データ
        """
        image_path = input.image_path

        # 分析依頼時刻を記録
        request_timestamp = timezone.now()

        # 分析を依頼、分析結果を取得
        ai_image_analysis_service = AIImageAnalysisService()
        analysis_result = ai_image_analysis_service.analyze(image_path)

        # 分析完了時刻を記録
        response_timestamp = timezone.now()

        analysis_metadata = AnalysisMetadata(
            image_path=image_path,
            request_timestamp=request_timestamp,
            response_timestamp=response_timestamp
        )

        log = AnalysisLog.create(analysis_result, analysis_metadata)

        log_id = self._repository.save(log)

        return AnalyzeImageOutput(
            log_id=log_id,
            image_path=image_path,
        )
