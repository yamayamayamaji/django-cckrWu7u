import json
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestImageAnalysisApp:
    @classmethod
    def setup_class(cls):
        cls.image_path = '/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg'

    def test_画像分析を行い結果を確認できる(self, client):
        # /image_analysis/analyze/ にPOSTリクエストを送信
        response = client.post(
            reverse('analyze'),
            data=json.dumps({'image_path': self.image_path}),
            content_type='application/json'
        )

        # レスポンスを検証
        assert response.status_code == 200
        analyze_output = response.json()
        assert analyze_output['success'] == True
        assert 'log_id' in analyze_output

        log_id = analyze_output['log_id']

        # /image_analysis/analysis_log/<log_id>/ にGETリクエストを送信
        response = client.get(reverse('analysis_log', kwargs={'log_id': log_id}))

        # レスポンスを検証
        assert response.status_code == 200

        # 分析ログの保存内容を検証
        log_output = response.json()
        assert log_output['image_path'] == self.image_path
        assert log_output['success'] == True
        assert log_output['message'] == 'success'
        assert log_output['class_id'] == 3
        assert log_output['confidence'] == 0.8683
