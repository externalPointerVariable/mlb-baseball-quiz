from google.cloud import aiplatform
import os
from config import GOOGLE_APPLICATION_CREDENTIALS

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

def generate_text(prompt: str) -> str:
    client = aiplatform.gapic.PredictionServiceClient()
    model_name = "projects/your-project-id/locations/us-central1/models/gemini"
    response = client.predict(
        name=model_name,
        instances=[{"prompt": prompt}],
        parameters={}
    )
    return response.predictions[0]
