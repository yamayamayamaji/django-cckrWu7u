from image_analysis_app.models import AIAnalysisLog

import datetime
from unittest import TestCase
from django.utils import timezone


class TestAIAnalysisLog(TestCase):
    def setUp(self):
        self.ai_analysis_log = AIAnalysisLog(
            image_path = '/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg',
            success = True,
            message = 'success',
            class_id = 3,
            confidence = 0.8683,
            request_timestamp = datetime.datetime(2024, 4, 1, 12, 34, 56),
            response_timestamp = datetime.datetime(2024, 4, 1, 12, 34, 57),
        )

    def test_image_pathが正しく設定されている(self):
        self.assertEqual(self.ai_analysis_log.image_path, '/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg')

    def test_successが正しく設定されている(self):
        self.assertEqual(self.ai_analysis_log.success, True)

    def test_messageが正しく設定されている(self):
        self.assertEqual(self.ai_analysis_log.message, 'success')

    def test_class_idが正しく設定されている(self):
        self.assertEqual(self.ai_analysis_log.class_id, 3)

    def test_confidenceが正しく設定されている(self):
        self.assertEqual(self.ai_analysis_log.confidence, 0.8683)

    def test_request_timestampが正しく設定されている(self):
        self.assertEqual(self.ai_analysis_log.request_timestamp, datetime.datetime(2024, 4, 1, 12, 34, 56))

    def test_response_timestampが正しく設定されている(self):
        self.assertEqual(self.ai_analysis_log.response_timestamp, datetime.datetime(2024, 4, 1, 12, 34, 57))
