import random

# stock_prices = []
# for _ in range(20):
#     stock_prices.append(random.randint(75, 150))

# Für die Prüfung:

stock_prices = []
for _ in range(20):
    stock_prices.append(random.randint(75, 150))

print(stock_prices)
average_stock_price = sum(stock_prices) / len(stock_prices)
print(f"Durchschnitt: {average_stock_price:.2f}")
max_stock_price = max(stock_prices)
print(f"Max: {max_stock_price}")
# min_stock_price = min(stock_prices)
# print(f"Min: {min_stock_price}")

#  Für die Prüfung:

stock_price_min = stock_prices[0]
for stock_price in stock_prices:
    if stock_price < stock_price_min:
        stock_price_min = stock_price
print(f"Min: {stock_price_min}")

days_with_rise = 0
for i in range(1, len(stock_prices)):
    if stock_prices[i] > stock_prices[i - 1]:
        days_with_rise += 1
print (f"Anzahl der Tage, an denen der Kurs gestiegen ist: {days_with_rise}")

days_with_decline = 0
for i in range(1, len(stock_prices)):
    if stock_prices[i] < stock_prices[i - 1]:
        days_with_decline += 1
print (f"Anzahl der Tage, an denen der Kurs gesunken ist: {days_with_decline}")

total_trend = (stock_prices[-1] - stock_prices[0]) / stock_prices[0] * 100
print(total_trend)