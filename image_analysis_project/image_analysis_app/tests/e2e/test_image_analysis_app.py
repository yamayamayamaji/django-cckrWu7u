import json
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestImageAnalysisApp:
    @classmethod
    def setup_class(cls):
        cls.success_image_path = '/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/success.jpg'
        cls.failure_image_path = '/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/failure.jpg'

    def request_analyze(self, client, image_path: str):
        """
        /image_analysis/analyze/ にPOSTリクエストを送信
        """
        return client.post(
            reverse('analyze'),
            data=json.dumps({'image_path': image_path}),
            content_type='application/json'
        )

    def request_analysis_log(self, client, log_id: int):
        """
        /image_analysis/analysis_log/<log_id>/ にGETリクエストを送信
        """
        return client.get(reverse('analysis_log', kwargs={'log_id': log_id}))

    def test_画像分析が成功し結果を確認できる(self, client):
        # /image_analysis/analyze/
        response = self.request_analyze(client, self.success_image_path)

        # レスポンスを検証
        assert response.status_code == 200
        analyze_output = response.json()
        assert 'log_id' in analyze_output

        log_id = analyze_output['log_id']

        # /image_analysis/analysis_log/<log_id>/
        response = self.request_analysis_log(client, log_id)

        # レスポンスを検証
        assert response.status_code == 200

        # 分析ログの保存内容を検証
        analysis_log_output = response.json()
        assert analysis_log_output['image_path'] == self.success_image_path
        assert analysis_log_output['success'] == True
        assert analysis_log_output['message'] == 'success'
        assert analysis_log_output['class_id'] == 3
        assert analysis_log_output['confidence'] == 0.8683

    def test_画像分析が失敗し結果を確認できる(self, client):
        # /image_analysis/analyze/
        response = self.request_analyze(client, self.failure_image_path)

        # レスポンスを検証
        assert response.status_code == 200
        analyze_output = response.json()
        assert 'log_id' in analyze_output

        log_id = analyze_output['log_id']

        # /image_analysis/analysis_log/<log_id>/
        response = self.request_analysis_log(client, log_id)

        # レスポンスを検証
        assert response.status_code == 200

        # 分析ログの保存内容を検証
        analysis_log_output = response.json()
        assert analysis_log_output['image_path'] == self.failure_image_path
        assert analysis_log_output['success'] == False
        assert analysis_log_output['message'] != 'success'
        assert analysis_log_output['class_id'] == None
        assert analysis_log_output['confidence'] == None
