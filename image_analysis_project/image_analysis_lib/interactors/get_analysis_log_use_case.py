from pydantic import BaseModel
from typing import Optional
from ..entities import AnalysisLog
from ..repositories import AIAnalysisLogRepositoryInterface
from .exceptions import EntityNotFoundError
from .use_case_interface import UseCaseInterface


class GetAnalysisLogInput(BaseModel):
    """
    GetAnalysisLogUseCaseの入力モデル

    Attributes:
        log_id (int): 取得するログのID
    """
    log_id: int


class GetAnalysisLogOutput(BaseModel):
    """
    GetAnalysisLogUseCaseの出力モデル

    Attributes:
        success (bool): 分析の成功フラグ
        image_path (str): 分析対象の画像パス
        message (str): 分析結果のメッセージ
        class_id (int): 分析結果のclass
        confidence (float): 分析結果の信頼度
    """
    success: bool
    image_path: str
    message: str
    class_id: Optional[int]
    confidence: Optional[float]


class GetAnalysisLogUseCase(UseCaseInterface):
    """
    分析ログを取得するユースケース
    """

    def __init__(self, repository: AIAnalysisLogRepositoryInterface):
        """
        コンストラクタ

        Args:
            repository (AIAnalysisLogRepositoryInterface): AI分析ログリポジトリ
        """
        self._repository = repository

    def execute(self, input: GetAnalysisLogInput) -> GetAnalysisLogOutput:
        """
        ユースケースを実行します。

        Args:
            input (GetAnalysisLogInput): 入力データ

        Returns:
            GetAnalysisLogOutput: 出力データ

        Raises:
            EntityNotFoundError: 指定されたログIDに対応するログが存在しない場合
        """
        log_id = input.log_id
        log: AnalysisLog = self._repository.get(log_id)

        if log is None:
            raise EntityNotFoundError

        return GetAnalysisLogOutput(
            success=log.success,
            image_path=log.image_path,
            message=log.message,
            class_id=log.class_id,
            confidence=log.confidence,
        )
