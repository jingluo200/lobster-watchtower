from typing import Dict, Any


def format_single_report(question: str, metrics: Dict[str, float], regime: Dict[str, Any]) -> str:
    return f"""
User Question: {question}

Parsed Metrics: {metrics}

Current Regime: {regime["label"]}

Explanation:
{regime["summary"]}

Confidence:
{regime["confidence"]}
""".strip()


def format_comparison_report(result: Dict[str, Any]) -> str:
    return f"""
Comparison Question:
Compare {result["ecosystem_a"]} and {result["ecosystem_b"]} in current regime terms

{result["ecosystem_a"]}: {result["regime_a"]}
{result["ecosystem_b"]}: {result["regime_b"]}

Difference:
{result["difference"]}

Confidence:
{result["confidence"]}
""".strip()


def format_shift_report(result: Dict[str, Any]) -> str:
    return f"""
Regime Shift Detection

Previous Regime:
{result["previous_regime"]}

Current Regime:
{result["current_regime"]}

Shift Detected:
{result["shift_detected"]}

Reason:
{result["reason"]}

Confidence:
{result["confidence"]}
""".strip()
