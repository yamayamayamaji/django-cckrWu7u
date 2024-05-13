import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST


@require_POST
def analyze(request):
    if request.method == 'POST':
        # リクエストからデータを取得
        data = json.loads(request.body)
        image_path = data.get('image_path')

        # 仮実装
        response_data = {
            'success': True,
            'message': 'success',
            'log_id': 123
        }
        return JsonResponse(response_data)


@require_GET
def analysis_log(request, log_id):
        # 仮実装
        response_data = {
            'success': True,
            'image_path': "/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg",
            'message': "success",
            'class_id': 3,
            'confidence': 0.8683,
        }
        return JsonResponse(response_data)
