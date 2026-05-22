import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API KEY LOADED:", api_key)


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def analyze_job_with_ai(job_title, company, description):

    try:
        prompt = f"""
        Analyze this remote job posting.

        Job Title: {job_title}
        Company: {company}
        Description: {description}

        Evaluate:
        1. Scam likelihood
        2. Job legitimacy
        3. Remote job quality
        4. Suspicious signals
        5. Positive trust signals
        """

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"AI Error: {str(e)}"