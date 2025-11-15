import wikipedia
wikipedia.set_lang('en')

def extract_wikipedia_title(prompt: str) -> str:
    lower = prompt.lower()

    title = prompt.strip() # Fallback

    if "find" in lower and " from " in lower:
        start = lower.find("find") + len("find")
        end = lower.find(" from ", start)
        title = prompt[start:end].strip()

    return title.strip(" '\"")


def fetch_wikipedia_article(title: str) -> str:
    try:
        page = wikipedia.page(title)
        return page.content

    except wikipedia.DisambiguationError as e:
        try:
            page = wikipedia.page(e.options[0])
            return page.content
        except:
            return f"Der Titel '{title}' ist mehrdeutig und konnte nicht aufgelöst werden."

    except wikipedia.PageError:
        results = wikipedia.search(title)
        if not results:
            return f"Kein Wikipedia-Artiekl für '{title}' gefunden."
        try:
            page = wikipedia.page(results[0])
            return page.content
        except:
            return f"Konnte '{title}' nicht laden."

    except Exception as e:
        return f"Wikipedia-Fehler: {e}"


def get_wikipedia_article_from_prompt(prompt: str) -> str:
    """
    High-Level: Prompt -> Titel -> Artikeltext
    """
    title = extract_wikipedia_title(prompt)
    return fetch_wikipedia_article(title)
