import vertexai
import os
import json
from dotenv import load_dotenv
from vertexai.preview.generative_models import GenerativeModel
import google.generativeai as genai
load_dotenv()


# project_id = os.getenv('PROJECT_ID')
# location = 'us-central1'

# vertexai.init(project=project_id, location=location)

# model = GenerativeModel('gemini-pro')

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-8b",
  generation_config=generation_config,
)



def generate_quiz(topic, difficulty_level):
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
    response_text = response.text.strip()


    # Fixing the JSON parsing code
    try:
        # Find the start of the JSON array
        json_start = response_text.find('[')
        if json_start == -1:
            raise ValueError("No JSON array found in the response.")

        # Extract the JSON string from the response
        json_str = response_text[json_start:]

        # Find the end of the JSON array
        json_end = json_str.rfind(']')
        if json_end == -1:
            raise ValueError("JSON array not properly closed in the response.")

        # Get the complete JSON array string
        json_str = json_str[:json_end + 1]

        # Parse the JSON string
        response_data = json.loads(json_str)
        return json.dumps(response_data, indent=4)
    except json.JSONDecodeError as e:
        print("Failed to parse JSON:", e)
        print("Response text:", response_text)
        return None
    except ValueError as e:
        print("Error:", e)
        print("Response text:", response_text)
        return None


print(generate_quiz("MLB", "Medium"))