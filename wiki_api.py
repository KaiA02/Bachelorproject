import wikipedia
wikipedia.set_lang('en')

def extract_wikipedia_title(prompt: str) -> str:
    lower = prompt.lower()

    if "find" not in lower or " from " not in lower:
        return ""

    start = lower.find("find") + len("find")
    end = lower.find(" from ", start)
    title = prompt[start:end].strip()

    return title.strip(" '\"")


def fetch_wikipedia_article(title: str) -> str:
    try:
        summary = wikipedia.summary(title)
        return summary

    except wikipedia.DisambiguationError as e:
        try:
            option = e.options[0]
            summary = wikipedia.summary(option)
            return summary
        except:
            return f"Der Titel '{title}' ist mehrdeutig und konnte nicht aufgelöst werden."

    except wikipedia.PageError:
        results = wikipedia.search(title)
        if not results:
            return f"Kein Wikipedia-Artiekl für '{title}' gefunden."
        try:
            summary = wikipedia.summary(results[0])
            return summary
        except:
            return f"Konnte '{title}' nicht laden."

    except Exception as e:
        return f"Wikipedia-Fehler: {e}"


def get_wikipedia_article_from_prompt(prompt: str) -> str:
    """
    High-Level: Prompt -> Titel -> Artikeltext
    """
    title = extract_wikipedia_title(prompt)

    if not title:
        return "Ungültige Query. Nutze das Muster: 'find <Titel> from wikipedia ..."

    return fetch_wikipedia_article(title)
