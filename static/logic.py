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
import yfinance as yf

def analyze_stock(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period='6mo')

        if data.empty:
            return {"error": "No data found for this symbol."}

        # Calculate basic metrics
        current_price = round(data['Close'].iloc[-1], 2)
        volatility = data['Close'].pct_change().std() * 100  # % standard deviation

        # Classify risk level
        if volatility < 1:
            risk = "Low"
            duration = "Long-term (3–5 years)"
            plan = "Stable stock with low volatility. Ideal for long-term growth."
        elif 1 <= volatility < 2:
            risk = "Medium"
            duration = "Mid-term (1–3 years)"
            plan = "Balanced opportunity. Moderate risk, suitable for steady investors."
        else:
            risk = "High"
            duration = "Short-term (6–12 months)"
            plan = "Volatile stock. Suitable for short-term trades or high-risk investors."

        return {
            "symbol": symbol.upper(),
            "price": current_price,
            "risk": risk,
            "duration": duration,
            "plan": plan
        }

    except Exception as e:
        return {"error": str(e)}
