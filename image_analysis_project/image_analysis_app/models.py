from django.db import models


class AIAnalysisLog(models.Model):
    image_path = models.CharField(max_length=255, null=True, blank=True)
    success = models.BooleanField()
    message = models.CharField(max_length=255, null=True, blank=True)
    class_id = models.IntegerField(null=True, blank=True, db_column='class')
    confidence = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
    request_timestamp = models.DateTimeField(null=True, blank=True)
    response_timestamp = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'ai_analysis_log'

    def __str__(self):
        fields = [
            f'id={self.id}',
            f'image_path={self.image_path}',
            f'success={self.success}',
        ]
        return f'AIAnalysisLog: {", ".join(fields)}'
