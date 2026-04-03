from config import KEYWORDS

def find_keywords(text):

    found = []

    for keyword in KEYWORDS:
        if keyword in text:
            found.append(keyword)

    return found