def compare_regimes(name_a: str, metrics_a: dict, name_b: str, metrics_b: dict):
    regime_a = classify_regime(metrics_a)
    regime_b = classify_regime(metrics_b)

    return {
        "ecosystem_a": name_a,
        "ecosystem_b": name_b,
        "regime_a": regime_a,
        "regime_b": regime_b,
        "difference": f"{name_a} shows stronger risk deployment than {name_b}."
    }
