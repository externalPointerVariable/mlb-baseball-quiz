import vertexai
import os
from dotenv import load_dotenv
from vertexai.preview.generative_models import GenerativeModel
load_dotenv()

project_id = os.getenv('PROJECT_ID')
location = 'us-central1'

vertexai.init(project=project_id, location=location)

model = GenerativeModel('gemini-pro')
response = model.generate_content('Say hi')

print(response.text)