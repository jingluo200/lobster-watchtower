from data_adapter import (
    get_mock_metrics,
    get_mock_comparison_metrics,
    get_mock_shift_metrics,
    route_demo_mode,
)
from regime_engine import classify_regime
from comparison_engine import compare_regimes
from shift_detector import detect_regime_shift
from report_formatter import (
    format_single_report,
    format_comparison_report,
    format_shift_report,
)


def run_single(question: str) -> None:
    metrics = get_mock_metrics(question)
    regime = classify_regime(metrics)
    report = format_single_report(question, metrics, regime)

    print("\n--- RESULT ---")
    print(report)


def run_comparison() -> None:
    comparison_data = get_mock_comparison_metrics()
    result = compare_regimes(
        "Base",
        comparison_data["Base"],
        "Ethereum",
        comparison_data["Ethereum"],
    )
    report = format_comparison_report(result)

    print("\n--- RESULT ---")
    print(report)


def run_shift_detection() -> None:
    shift_data = get_mock_shift_metrics()
    result = detect_regime_shift(
        shift_data["previous"],
        shift_data["current"],
    )
    report = format_shift_report(result)

    print("\n--- RESULT ---")
    print(report)


def main() -> None:
    print("OKX Onchain OS Macro Regime Mapper")
    print("Type a macro question about onchain market behavior.\n")
    print("Suggested questions:")
    print("- Risk expansion or defensive parking?")
    print("- Are stablecoins being redeployed into risk or staying idle?")
    print("- Compare Base and Ethereum in current regime terms")
    print("- Did the market shift from defensive parking to risk rotation?\n")

    question = input("Question: ").strip()
    mode = route_demo_mode(question)

    if mode == "compare":
        run_comparison()
    elif mode == "shift":
        run_shift_detection()
    else:
        run_single(question)


if __name__ == "__main__":
    main()
