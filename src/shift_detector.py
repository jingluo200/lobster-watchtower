from typing import Dict, Any

from regime_engine import classify_regime


def detect_regime_shift(
    previous_metrics: Dict[str, float],
    current_metrics: Dict[str, float],
) -> Dict[str, Any]:
    previous_regime = classify_regime(previous_metrics)
    current_regime = classify_regime(current_metrics)

    shift_detected = previous_regime["label"] != current_regime["label"]

    previous_deployment = float(previous_metrics.get("risk_asset_deployment", 0))
    current_deployment = float(current_metrics.get("risk_asset_deployment", 0))

    previous_breadth = float(previous_metrics.get("participation_breadth", 0))
    current_breadth = float(current_metrics.get("participation_breadth", 0))

    previous_stablecoin = float(previous_metrics.get("stablecoin_growth", 0))
    current_stablecoin = float(current_metrics.get("stablecoin_growth", 0))

    reason_parts = []

    if current_deployment > previous_deployment:
        reason_parts.append("risk asset deployment improved")
    elif current_deployment < previous_deployment:
        reason_parts.append("risk asset deployment weakened")

    if current_breadth > previous_breadth:
        reason_parts.append("participation breadth improved")
    elif current_breadth < previous_breadth:
        reason_parts.append("participation breadth narrowed")

    if current_stablecoin > previous_stablecoin:
        reason_parts.append("stablecoin presence increased")
    elif current_stablecoin < previous_stablecoin:
        reason_parts.append("stablecoin parking eased")

    reason = ", ".join(reason_parts) if reason_parts else "signal mix changed"

    confidence = round(
        min(
            0.91,
            (previous_regime["confidence"] + current_regime["confidence"]) / 2,
        ),
        2,
    )

    return {
        "previous_regime": previous_regime["label"],
        "current_regime": current_regime["label"],
        "shift_detected": shift_detected,
        "reason": reason.capitalize() + ".",
        "confidence": confidence,
    }
