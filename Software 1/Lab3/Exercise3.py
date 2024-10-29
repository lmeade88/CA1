print("Please enter the number of chip portions sold:")
chipsSold = int(input())

print("Please enter the number of hamburgers sold:")
hamburgersSold = int(input())

chipsProfit = 75 - 30
totalChipsProfit = chipsSold*chipsProfit

hamBurgersProfit = 95 - 40
totalHamProfit = hamBurgersProfit*hamburgersSold

totalProfit = round((totalChipsProfit + totalHamProfit) / 100, 2)

print(f"Total profit is €{totalProfit}")