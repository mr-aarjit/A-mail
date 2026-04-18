import cohere, openai


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

openai_client = openai.Client(
    api_key  = "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",
    base_url= "https://openrouter.ai/api/v1",
)

cohere_client = cohere.ClientV2(
    api_key= "YT6kYqGD4qBToDKs19txBpCq32puEo5yBhPhbcj8" 
    )

def Mail_geneneration(propmt):
    try:
        response = cohere_client.chat(
            model = "command-a-03-2025",
            messages= [{"role": "system", "content": SYSTEM_PROMPT},{"role":"user", "content":propmt}],
            max_tokens=500        )

        return response.message.content[0].text
        print("Cohere is used")

    except:
        try:
            response2 = openai_client.chat.completions.create(
                model = "codex-mini-latest",
                messages = [{"role": "system", "content": SYSTEM_PROMPT},{"role":"user", "content":propmt}],
                max_tokens=400
            )

            return response.choices[0].message
            print("Open_AI used")
        except:
            return "Server error, API tokens (limit) is finished, might get re-stocked soon. Sry, my bad"