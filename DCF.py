def dcf_valuation(free_cash_flows, discount_rate):
    npv = sum([fcf / (1 + discount_rate) ** i for i, fcf in enumerate(free_cash_flows, 1)])
    return npv


# Example free cash flows (in millions) and discount rate
free_cash_flows = [10, 15, 20, 25, 30]
discount_rate = 0.10

npv = dcf_valuation(free_cash_flows, discount_rate)
print(f"Company Valuation (NPV): ${npv:.2f} million")


