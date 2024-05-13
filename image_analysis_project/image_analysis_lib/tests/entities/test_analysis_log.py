from image_analysis_lib.entities import AnalysisLog

from unittest import TestCase
from image_analysis_lib.entities import AnalysisMetadata, AnalysisResult
from django.utils import timezone


class TestAnalysisLog(TestCase):
    def test_AnalysisResultとAnalysisMetadataからインスタンスを生成できる(self):
        analysis_result = AnalysisResult(
            success=True,
            message="message",
            class_id=1,
            confidence=0.5000,
        )
        analysis_metadata = AnalysisMetadata(
            image_path="path/to/image",
            request_timestamp=timezone.now(),
            response_timestamp=timezone.now(),
        )

        ai_analysis_log = AnalysisLog.create(analysis_result, analysis_metadata)

        self.assertIsInstance(ai_analysis_log, AnalysisLog)
