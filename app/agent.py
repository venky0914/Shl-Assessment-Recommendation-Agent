from app.retriever import search_assessments

def detect_intent(user_message):

    user_message = user_message.lower()

    # Off-topic detection
    off_topic_keywords = [
        "legal",
        "medical",
        "finance",
        "politics",
        "religion"
    ]

    for word in off_topic_keywords:
        if word in user_message:
            return "off_topic"

    # Comparison detection
    if "difference" in user_message or "compare" in user_message:
        return "compare"

    # Vague query detection
    vague_words = [
        "assessment",
        "test",
        "need hiring"
    ]

    for word in vague_words:
        if user_message.strip() == word:
            return "clarify"

    # Default
    return "recommend"


def generate_response(user_message):

    intent = detect_intent(user_message)

    # Clarification
    if intent == "clarify":

        return {
            "reply": "Can you specify the role or skills you are hiring for?",
            "recommendations": [],
            "end_of_conversation": False
        }

    # Off-topic
    if intent == "off_topic":

        return {
            "reply": "I can only help with SHL assessment recommendations.",
            "recommendations": [],
            "end_of_conversation": True
        }

    # Comparison
    if intent == "compare":

        return {
            "reply": "Comparison functionality will be added soon.",
            "recommendations": [],
            "end_of_conversation": False
        }

    # Recommendations
    results = search_assessments(user_message)

    recommendations = []

    for r in results:

        recommendations.append({
            "name": r["name"],
            "url": r["url"],
            "test_type": "K"
        })

    return {
        "reply": f"I found {len(recommendations)} relevant SHL assessments.",
        "recommendations": recommendations,
        "end_of_conversation": False
    }


# Testing
if __name__ == "__main__":

    query = "Java backend developer"

    response = generate_response(query)

    print(response)