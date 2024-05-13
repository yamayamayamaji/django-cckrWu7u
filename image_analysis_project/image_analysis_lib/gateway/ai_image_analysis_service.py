import requests
from typing import Any, Dict
from ..entities import AnalysisResult


class AIImageAnalysisService:
    """
    AI画像分析サービスを表すクラス

    外部のAI画像分析WebAPIとのやり取りを担当します。

    ■ 現在はAI画像分析WebAPIのレスポンスはモックアップされたものです。
    """

    def __init__(self, base_url: str = "http://example.com"):
        """
        コンストラクタ

        Args:
            base_url (str): AI画像分析WebAPIのベースURL（デフォルト: "http://example.com"）
        """
        self._base_url = base_url

    def analyze(self, image_path: str) -> AnalysisResult:
        """
        画像を分析する

        Args:
            image_path (str): 分析対象の画像ファイルパス

        Returns:
            AnalysisResult: 分析結果を表すオブジェクト
        """
        url = self._base_url
        payload = {"image_path": image_path}

        try:
            response = self._mock_api_response(payload)
            # response = requests.post(url, json=payload)
            # data = response.json()
        except requests.exceptions.RequestException as e:
            # APIリクエストが失敗した場合のエラーハンドリング
            return AnalysisResult(success=False, message=str(e))

        return self._parse_response(response)

    def _mock_api_response(self, payload: Dict[str, str]) -> Dict[str, Any]:
        """
        AI画像分析WebAPIのレスポンスをモックアップします。

        image_pathに'failure'が含まれている場合、失敗レスポンスを返します。
        そうでない場合は、成功レスポンスを返します。

        Args:
            payload (Dict[str, str]): APIリクエストのペイロード

        Returns:
            Dict[str, Any]: モックアップされたAPIレスポンス
        """
        if 'failure' in payload['image_path']:
            return {
                'success': False,
                'message': 'Error:E50012',
                'estimated_data': {}
            }

        return {
            "success": True,
            "message": "success",
            "estimated_data": {
                "class": 3,
                "confidence": 0.8683
            }
        }

    def _parse_response(self, response_data: Dict[str, Any]) -> AnalysisResult:
        """
        APIレスポンスを解析して、AnalysisResultオブジェクトを作成する

        Args:
            data (Dict[str, Any]): APIレスポンスのデータ

        Returns:
            AnalysisResult: 分析結果を表すオブジェクト
        """
        success = response_data['success']
        message = response_data['message']

        estimated_data = response_data['estimated_data']
        if estimated_data:
            class_id = estimated_data['class']
            confidence = estimated_data['confidence']
        else:
            class_id = None
            confidence = None

        return AnalysisResult(
            success=success,
            message=message,
            class_id=class_id,
            confidence=confidence
        )
