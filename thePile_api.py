from openai import OpenAI
from config_loader import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def extract_chatgpt_query(prompt: str) -> str:
    lower = prompt.lower()

    if "find" in lower and " from " in lower:
        start = lower.find("find") + len("find")
        end = lower.find(" from ", start)
        query = prompt[start:end].strip()
        return query.strip()

    return prompt.strip()


def get_chatgpt_answer_from_prompt(prompt: str) -> str:
    question = extract_chatgpt_query(prompt)

    if not OPENAI_API_KEY or OPENAI_API_KEY.strip() == "":
        return "Fehler: Kein OpenAI API-Key gefunden."

    try:
        responses = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful Assistant."},
            {"role": "user", "content": question},
        ],
        max_tokens=500,
        )

        return responses.choices[0].message.content

    except Exception as e:

        error_str = str(e).lower()

        if "invalid api key" in error_str or "incorrect api key" in error_str:
            return "API-Key ungültig"

        if "connection" in error_str or "timed out" in error_str:
            return "Netzwerkfehler: Keine Verbindung zu OpenAI"

        if "rate limit" in error_str:
            return "Rate limit erreicht. Bitte warten."

        if "billing" in error_str:
            return "Kein Guthaben auf dem OpenAI-Konto."

        # Fallback für alle unbekannten Fehler
        return f"Unbekannter OpenAI-Fehler: {e}"