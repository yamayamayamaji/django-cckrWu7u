from django.urls import path
from . import views


urlpatterns = [
    # /image_analysis_app/analyze
    path('analyze', views.analyze, name='analyze'),

    # /image_analysis_app/analysis_log
    path('analysis_log/<int:log_id>', views.analysis_log, name='analysis_log'),
]
