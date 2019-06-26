hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]


total_price = 0

for cost in prices:
  total_price += cost
  print(total_price)
  
average_price = (total_price / (len(prices)))  

print('Average Haircut Price: ' + str(average_price))

new_prices = [price - 5 for price in prices]

print(new_prices)

total_revenue = 0

for i in range (len(hairstyles)):
  total_revenue += ((prices[i] * last_week[i]))
  
print('Total Revenue: ' + str(total_revenue))  

average_daily_revenue = (int(total_revenue / 7))

print('Average Daily Revenue ' + str(average_daily_revenue))

cuts_under_30 = []
for i in range (len(prices)):
  if prices[i] < 30:
    cuts_under_30.append(hairstyles[i])
    
print(cuts_under_30)
