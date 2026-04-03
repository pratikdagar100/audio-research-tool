import random

def generate_questions(keyword):

    question_templates = [
        # Concept
        f"What is the fundamental concept behind {keyword}?",
        
        # Application
        f"How is {keyword} applied in real-world scenarios?",
        
        # Technical
        f"What are the key techniques or models used in {keyword}?",
        
        # Comparison
        f"How does {keyword} differ from traditional approaches in this field?",
        
        # Impact
        f"What impact has {keyword} had on modern technology or society?",
        
        # Challenges
        f"What are the main challenges or limitations of {keyword}?",
        
        # Future
        f"What is the future potential of {keyword} in upcoming technologies?"
    ]

    # 🔥 pick 4–5 diverse questions randomly
    selected = random.sample(question_templates, 5)

    return selected
