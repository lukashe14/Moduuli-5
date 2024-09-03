import random

arpakuutiot = int(input("Kuinka monta arpakuutiota:"))

kokonaisumma = 0

for _ in range(arpakuutiot):
    arvo = random.randint(1,6)
    kokonaisumma += arvo

print(f"Silmälukujen summa on {kokonaisumma}")