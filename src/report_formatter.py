def format_report(question: str, metrics: dict, regime: str) -> str:
    explanations = {
        "Defensive Parking": (
            "Stablecoin presence is increasing faster than broad risk deployment. "
            "Capital is onchain, but conviction remains shallow."
        ),
        "Risk Expansion": (
            "Capital is deploying with wider participation breadth. "
            "This suggests stronger risk appetite and broader market involvement."
        ),
        "Risk Rotation": (
            "Capital appears to be rotating out of defensive posture into selected risk areas. "
            "This suggests improving appetite, but not yet a fully broad expansion."
        ),
        "Narrative Exhaustion": (
            "Attention is still visible, but participation breadth and follow-through are fading. "
            "This suggests weakening momentum beneath the surface."
        )
    }

    return f"""
User Question: {question}

Parsed Metrics: {metrics}

Current Regime: {regime}

Explanation:
{explanations.get(regime, 'No explanation available.')}
""".strip()
