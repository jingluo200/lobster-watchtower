def get_mock_metrics(question: str) -> dict:
    q = question.lower()

    if "stablecoin" in q:
        return {
            "stablecoin_growth": 8,
            "risk_deployment": 3,
            "participation_breadth": 4,
            "narrative_strength": 4
        }

    if "base" in q:
        return {
            "stablecoin_growth": 6,
            "risk_deployment": 6,
            "participation_breadth": 5,
            "narrative_strength": 7
        }

    return {
        "stablecoin_growth": 5,
        "risk_deployment": 8,
        "participation_breadth": 7,
        "narrative_strength": 6
    }
