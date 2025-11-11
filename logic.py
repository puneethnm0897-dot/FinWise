def recommend_portfolio(amount, years, risk_level):
    INVESTMENTS = {
        "FD": {"rate": 0.06, "risk": "Low"},
        "RD": {"rate": 0.065, "risk": "Low"},
        "Gold": {"rate": 0.08, "risk": "Medium"},
        "SIP": {"rate": 0.11, "risk": "Medium"},
        "Stocks": {"rate": 0.16, "risk": "High"}
    }

    if risk_level == "Low":
        split = {"FD": 0.6, "RD": 0.3, "Gold": 0.1}
    elif risk_level == "Medium":
        split = {"SIP": 0.4, "Gold": 0.3, "FD": 0.3}
    else:
        split = {"Stocks": 0.5, "SIP": 0.3, "Gold": 0.2}

    result = []
    total_value = 0

    for invest, portion in split.items():
        invest_amount = amount * portion
        rate = INVESTMENTS[invest]["rate"]
        final_amt = invest_amount * ((1 + rate) ** years)
        total_value += final_amt

        result.append({
            "type": invest,
            "invested": round(invest_amount, 2),
            "expected_return": round(final_amt, 2),
            "growth": round(final_amt - invest_amount, 2)
        })

    result.append({
        "total_invested": amount,
        "total_value": round(total_value, 2),
        "total_gain": round(total_value - amount, 2)
    })

    return result
