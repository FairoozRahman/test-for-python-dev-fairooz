from django.db import models
import uuid


# Model to store the text data and sentiment analysis
class Analysis(models.Model):

    SENTIMENT_TYPE = (
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
    ) # Left out neutral type because hugging face model only predicts positive or negative by default

    text = models.TextField(max_length=1000)
    result = models.CharField(max_length=100, choices=SENTIMENT_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

