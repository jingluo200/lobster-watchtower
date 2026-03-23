def classify_regime(metrics: dict) -> str:
    stablecoin_growth = metrics.get("stablecoin_growth", 0)
    risk_deployment = metrics.get("risk_deployment", 0)
    participation_breadth = metrics.get("participation_breadth", 0)
    narrative_strength = metrics.get("narrative_strength", 0)

    if stablecoin_growth > 7 and risk_deployment < 4:
        return "Defensive Parking"

    if risk_deployment > 7 and participation_breadth > 6:
        return "Risk Expansion"

    if risk_deployment > 5 and narrative_strength > 5:
        return "Risk Rotation"

    return "Narrative Exhaustion"
