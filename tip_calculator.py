# Task 4: Tip Calculator

def calculate_tip(bill, tip_percent):
    tip = bill * tip_percent / 100
    total = bill + tip
    return {"tip": tip, "total": total}

result1 = calculate_tip(500, 10)
print(f"Bill: 500 | Tip: {result1['tip']} | Total: {result1['total']}")

result2 = calculate_tip(1200, 15)
print(f"Bill: 1200 | Tip: {result2['tip']} | Total: {result2['total']}")

result3 = calculate_tip(350, 20)
print(f"Bill: 350 | Tip: {result3['tip']} | Total: {result3['total']}")