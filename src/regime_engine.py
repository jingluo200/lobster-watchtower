from typing import Dict, Any


def classify_regime(metrics: Dict[str, float]) -> Dict[str, Any]:
    stablecoin_growth = float(metrics.get("stablecoin_growth", 0))
    risk_asset_deployment = float(metrics.get("risk_asset_deployment", 0))
    participation_breadth = float(metrics.get("participation_breadth", 0))
    capital_stickiness = float(metrics.get("capital_stickiness", 0))
    narrative_strength = float(metrics.get("narrative_strength", 0))

    # Defensive Parking:
    # lots of capital present, but weak deployment and shallow participation
    if stablecoin_growth >= 7 and risk_asset_deployment <= 4:
        confidence = min(
            0.95,
            0.62
            + (stablecoin_growth * 0.03)
            + ((4 - risk_asset_deployment) * 0.04),
        )
        return {
            "label": "Defensive Parking",
            "summary": (
                "Stablecoin presence is rising faster than broad risk deployment."
            ),
            "confidence": round(confidence, 2),
        }

    # Risk Expansion:
    # strong deployment + broad participation + decent stickiness
    if (
        risk_asset_deployment >= 7
        and participation_breadth >= 7
        and capital_stickiness >= 6
    ):
        confidence = min(
            0.95,
            0.60
            + (risk_asset_deployment * 0.025)
            + (participation_breadth * 0.025),
        )
        return {
            "label": "Risk Expansion",
            "summary": (
                "Capital is deploying with broader participation and stronger risk appetite."
            ),
            "confidence": round(confidence, 2),
        }

    # Risk Rotation:
    # capital is moving out of defensive posture into selected risk areas
    if risk_asset_deployment >= 6 and narrative_strength >= 6:
        confidence = min(
            0.92,
            0.58
            + (risk_asset_deployment * 0.025)
            + (narrative_strength * 0.02),
        )
        return {
            "label": "Risk Rotation",
            "summary": (
                "Capital is beginning to move from defensive posture into selected risk areas."
            ),
            "confidence": round(confidence, 2),
        }

    # Default:
    confidence = min(
        0.88,
        0.55 + (max(narrative_strength, 4) * 0.02),
    )
    return {
        "label": "Narrative Exhaustion",
        "summary": (
            "Attention remains visible, but participation breadth and follow-through are fading."
        ),
        "confidence": round(confidence, 2),
    }
