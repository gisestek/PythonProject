veroton = input("Anna tuotteen hinta ilman veroa:\n")
alv = 1.255
verollinen = int(veroton) * alv
print(f"Hinta uuden alv:n kanssa: {round(verollinen,2)}")
