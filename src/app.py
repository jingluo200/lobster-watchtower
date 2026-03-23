from data_adapter import get_mock_metrics
from regime_engine import classify_regime
from report_formatter import format_report

def main():
    print("OKX Onchain OS Macro Regime Mapper")
    print("Type a macro question about onchain market behavior.\n")

    question = input("Question: ").strip()
    metrics = get_mock_metrics(question)
    regime = classify_regime(metrics)
    report = format_report(question, metrics, regime)

    print("\n--- RESULT ---")
    print(report)

if __name__ == "__main__":
    main()
