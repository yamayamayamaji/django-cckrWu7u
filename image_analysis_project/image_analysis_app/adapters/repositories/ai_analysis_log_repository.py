from image_analysis_lib import (
    AIAnalysisLogRepositoryInterface,
    AnalysisLog as AnalysisLogEntity,
)
from ...models import AIAnalysisLog


class AIAnalysisLogRepository(AIAnalysisLogRepositoryInterface):
    """
    AIAnalysisLogのリポジトリクラス

    Attributes:
        model_class (AIAnalysisLog): AIAnalysisLogのDjangoモデルクラス
    """

    def __init__(self) -> None:
        self.model_class = AIAnalysisLog

    def get(self, log_id: int) -> AnalysisLogEntity | None:
        """
        指定されたログIDのAIAnalysisLogを取得します。

        Args:
            log_id (int): 取得するログのID

        Returns:
            AnalysisLogEntity | None: 取得したAIAnalysisLogエンティティ。
                                    指定されたログIDのAIAnalysisLogが存在しない場合はNoneを返します。
        """
        try:
            model = self.model_class.objects.get(id=log_id)
            return AnalysisLogEntity(**model.__dict__)
        except self.model_class.DoesNotExist:
            return None

    def save(self, analysis_log: AnalysisLogEntity) -> int:
        """
        AIAnalysisLogを保存する

        Args:
            analysis_log (AnalysisLogEntity): 保存するAIAnalysisLogエンティティ

        Returns:
            int: 保存されたAIAnalysisLogのID
        """
        model = self.model_class(**analysis_log.model_dump())
        model.save()
        return model.id
