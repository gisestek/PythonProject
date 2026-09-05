time = input("Anna minuutit:\n")
#aika tunteina
hours = int(time) / 60
#jakojäännös
minutes = int(time) % 60
#täydet tunnit
hours -= minutes/60
#print(time)
#print(hours)
#print(minutes)
print(f"{round(hours)}h {minutes}min")