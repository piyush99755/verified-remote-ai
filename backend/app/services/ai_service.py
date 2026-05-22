from google import genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_job_with_ai(job_title, company, description):

    try:

        prompt = f"""
        Analyze this remote job posting.

        Job Title: {job_title}
        Company: {company}
        Description: {description}

        Evaluate:
        - legitimacy
        - scam risk
        - job quality
        - remote authenticity
        - transparency

        Return ONLY valid JSON in this format:

        {{
            "legitimacy": "HIGH/MEDIUM/LOW",
            "scam_risk": "HIGH/MEDIUM/LOW",
            "job_quality": "HIGH/MEDIUM/LOW",
            "remote_authenticity": "HIGH/MEDIUM/LOW",
            "transparency": "HIGH/MEDIUM/LOW",
            "summary": "Short explanation"
        }}
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        cleaned_response = response.text.strip()

        parsed_response = json.loads(cleaned_response)

        return parsed_response

    except Exception as e:

        return {
            "error": str(e)
        }