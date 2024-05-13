from image_analysis_lib import GetAnalysisLogUseCase, GetAnalysisLogInput, GetAnalysisLogOutput
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from ..adapters.repositories import AIAnalysisLogRepository


@require_GET
def analysis_log(request, log_id):
    # ユースケース実行
    repository = AIAnalysisLogRepository()
    input = GetAnalysisLogInput(log_id=log_id)
    controller = GetAnalysisLogUseCase(repository)
    output: GetAnalysisLogOutput = controller.execute(input)

    # レスポンス
    return JsonResponse(output.model_dump())
