from abc import ABC, abstractmethod
from ..entities import AnalysisLog


class AIAnalysisLogRepositoryInterface(ABC):
    @abstractmethod
    def get(self, log_id: int) -> AnalysisLog | None:
        raise NotImplementedError()

    @abstractmethod
    def save(self, analysis_log: AnalysisLog) -> int:
        raise NotImplementedError()
