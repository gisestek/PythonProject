total = input("Anna 1-100 senttiä:\n") #voi periaatteessa olla mikä vaan positiivinen summa
#Muutetaan input luvuksi
total = int(total)

coin = 50 #käsiteltävä kolikko
left = total % coin #paljon jää rahaa kun "coin" senttiset otetaan pois
pieces = (total - left) / coin #kolikoiden määrä
total = left
print(f"{coin} snt kolikoita {round(pieces)} kpl")

coin = 20
left = total % coin #paljon jää rahaa kun "coin" senttiset otetaan pois
pieces = (total - left) / coin #kolikoiden määrä
total = left
print(f"{coin} snt kolikoita {round(pieces)} kpl")

coin = 10
left = total % coin #paljon jää rahaa kun "coin" senttiset otetaan pois
pieces = (total - left) / coin #kolikoiden määrä
total = left
print(f"{coin} snt kolikoita {round(pieces)} kpl")

coin = 5
left = total % coin #paljon jää rahaa kun "coin" senttiset otetaan pois
pieces = (total - left) / coin #kolikoiden määrä
total = left
print(f"{coin} snt kolikoita {round(pieces)} kpl")

coin = 2
left = total % coin #paljon jää rahaa kun "coin" senttiset otetaan pois
pieces = (total - left) / coin #kolikoiden määrä
total = left
print(f"{coin} snt kolikoita {round(pieces)} kpl")

coin = 1
left = total % coin #paljon jää rahaa kun "coin" senttiset otetaan pois
pieces = (total - left) / coin #kolikoiden määrä
total = left
print(f"{coin} snt kolikoita {round(pieces)} kpl")

#print(f"Jäljellä rahaa {round(left)} snt")