from google.cloud import aiplatform
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service-account-file.json"

def generate_text(prompt: str) -> str:
    client = aiplatform.gapic.PredictionServiceClient()
    model_name = "projects/your-project-id/locations/us-central1/models/gemini"
    response = client.predict(
        name=model_name,
        instances=[{"prompt": prompt}],
        parameters={}
    )
    return response.predictions[0]
