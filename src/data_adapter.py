from typing import Dict, Any


def get_mock_metrics(question: str) -> Dict[str, float]:
    q = question.lower().strip()

    if "stablecoin" in q:
        return {
            "stablecoin_growth": 8,
            "risk_asset_deployment": 3,
            "participation_breadth": 4,
            "capital_stickiness": 5,
            "narrative_strength": 4,
        }

    if "base" in q and "ethereum" in q:
        # default single-bundle response if the caller is not using compare mode
        return {
            "stablecoin_growth": 6,
            "risk_asset_deployment": 6,
            "participation_breadth": 5,
            "capital_stickiness": 6,
            "narrative_strength": 7,
        }

    if "shift" in q or "defensive parking to risk rotation" in q:
        return {
            "stablecoin_growth": 5,
            "risk_asset_deployment": 7,
            "participation_breadth": 6,
            "capital_stickiness": 6,
            "narrative_strength": 7,
        }

    return {
        "stablecoin_growth": 5,
        "risk_asset_deployment": 8,
        "participation_breadth": 7,
        "capital_stickiness": 7,
        "narrative_strength": 6,
    }


def get_mock_comparison_metrics() -> Dict[str, Dict[str, float]]:
    return {
        "Base": {
            "stablecoin_growth": 6,
            "risk_asset_deployment": 7,
            "participation_breadth": 6,
            "capital_stickiness": 6,
            "narrative_strength": 7,
        },
        "Ethereum": {
            "stablecoin_growth": 8,
            "risk_asset_deployment": 4,
            "participation_breadth": 5,
            "capital_stickiness": 7,
            "narrative_strength": 5,
        },
        "Solana": {
            "stablecoin_growth": 6,
            "risk_asset_deployment": 8,
            "participation_breadth": 7,
            "capital_stickiness": 5,
            "narrative_strength": 8,
        },
    }


def get_mock_shift_metrics() -> Dict[str, Dict[str, float]]:
    return {
        "previous": {
            "stablecoin_growth": 8,
            "risk_asset_deployment": 3,
            "participation_breadth": 4,
            "capital_stickiness": 6,
            "narrative_strength": 4,
        },
        "current": {
            "stablecoin_growth": 5,
            "risk_asset_deployment": 7,
            "participation_breadth": 6,
            "capital_stickiness": 6,
            "narrative_strength": 7,
        },
    }


def route_demo_mode(question: str) -> str:
    q = question.lower().strip()

    if "compare" in q and "base" in q and "ethereum" in q:
        return "compare"

    if "shift" in q or "defensive parking to risk rotation" in q:
        return "shift"

    return "single"
