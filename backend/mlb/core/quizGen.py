import vertexai
import os
import json
from dotenv import load_dotenv
from vertexai.preview.generative_models import GenerativeModel
load_dotenv()

project_id = os.getenv('PROJECT_ID')
location = 'us-central1'

vertexai.init(project=project_id, location=location)

model = GenerativeModel('gemini-pro')

def generate_quiz(topic, difficulty_level):
    try:
        prompt = f'''Generate 10 Multiple Choice Questions in JSON format about the topic "{topic}" with difficulty level {difficulty_level}. Each question should follow this structure:
        [
            {{
                "question": "Your generated question",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "answer": "The correct option"
            }},
            ...
        ]
        '''

        response = model.generate_content(prompt)
        response = json.loads(response.text)
        return json.dumps(response, indent=4)
    except Exception as e:
        return str(e)
