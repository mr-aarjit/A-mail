import os


SYSTEM_PROMPT = """
You are an elite professional email writer whose name is Aarjit's Mail generator for executives and business leaders.

If English:
GREETING RULES:
- Boss, professor, elder, official → "Respected [Title] [Surname],"
- Friend, family, peer → "Dear [Name],"
- Default → "Respected [Name],"

STRUCTURE:
1. Greeting
2. Blank line
3. Subject: ...
4. Blank line
5. Body (clear, structured, professional)
6. Blank line
7. Closing
8. [Your Name]

QUALITY:
- Detailed, polished, professional
- No meta-commentary

If unrelated request:
Return:
"Hello, I am Aarjit's Mail Generator. I am designed to generate mails."
"""

def Mail_geneneration(propmt):
    cohere_api_key = os.environ.get("COHERE_API_KEY")
    openrouter_api_key = os.environ.get("OPENROUTER_API_KEY")

    cohere_client = None
    openai_client = None

    if cohere_api_key:
        try:
            import cohere

            cohere_client = cohere.ClientV2(api_key=cohere_api_key)
        except Exception:
            cohere_client = None

    if openrouter_api_key:
        try:
            import openai

            openai_client = openai.Client(
                api_key=openrouter_api_key,
                base_url="https://openrouter.ai/api/v1",
            )
        except Exception:
            openai_client = None

    if cohere_client is None and openai_client is None:
        return "Service temporarily unavailable due to missing API configuration."

    try:
        if cohere_client is None:
            raise RuntimeError("Cohere unavailable")

        response = cohere_client.chat(
            model="command-a-03-2025",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": propmt},
            ],
            max_tokens=500,
        )
        return response.message.content[0].text
    except Exception:
        try:
            if openai_client is None:
                raise RuntimeError("OpenRouter unavailable")

            response2 = openai_client.chat.completions.create(
                model="openai/gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": propmt},
                ],
                max_tokens=400,
            )
            return response2.choices[0].message.content
        except Exception:
            return "Service temporarily unavailable due to API limits."