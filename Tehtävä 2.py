numerot = []

while True:
    luvut = input("Anna luku:")
    if luvut == "":
        break

    else:
        numero = int(luvut)
        numerot.append(numero)


numerot.sort(reverse=True)
viisi_suurinta = numerot[:5]

print(f"Viisi suurinta lukua ovat:{viisi_suurinta}")