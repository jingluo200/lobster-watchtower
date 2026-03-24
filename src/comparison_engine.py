from typing import Dict, Any

from regime_engine import classify_regime


def compare_regimes(
    ecosystem_a: str,
    metrics_a: Dict[str, float],
    ecosystem_b: str,
    metrics_b: Dict[str, float],
) -> Dict[str, Any]:
    regime_a = classify_regime(metrics_a)
    regime_b = classify_regime(metrics_b)

    score_a = float(metrics_a.get("risk_asset_deployment", 0)) + float(
        metrics_a.get("participation_breadth", 0)
    )
    score_b = float(metrics_b.get("risk_asset_deployment", 0)) + float(
        metrics_b.get("participation_breadth", 0)
    )

    if score_a > score_b:
        difference = (
            f"{ecosystem_a} shows earlier-stage risk deployment and stronger speculative re-entry."
        )
    elif score_b > score_a:
        difference = (
            f"{ecosystem_b} shows earlier-stage risk deployment and stronger speculative re-entry."
        )
    else:
        difference = (
            f"{ecosystem_a} and {ecosystem_b} currently show similar deployment depth and participation breadth."
        )

    comparison_confidence = round(
        min(
            0.93,
            (regime_a["confidence"] + regime_b["confidence"]) / 2,
        ),
        2,
    )

    return {
        "ecosystem_a": ecosystem_a,
        "ecosystem_b": ecosystem_b,
        "regime_a": regime_a["label"],
        "regime_b": regime_b["label"],
        "difference": difference,
        "confidence": comparison_confidence,
    }
