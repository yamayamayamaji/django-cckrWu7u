import json
from image_analysis_lib import AnalyzeImageUseCase, AnalyzeImageInput, AnalyzeImageOutput
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from ..adapters.repositories import AIAnalysisLogRepository


@require_POST
def analyze(request):
    # リクエストからデータを取得
    data = json.loads(request.body)
    image_path = data.get('image_path')

    # ユースケース実行
    repository = AIAnalysisLogRepository()
    input = AnalyzeImageInput(image_path=image_path)
    controller = AnalyzeImageUseCase(repository)
    output: AnalyzeImageOutput = controller.execute(input)

    # レスポンス
    return JsonResponse(output.model_dump())
