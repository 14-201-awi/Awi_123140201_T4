import math

while True:
    angka = input("Masukkan angka: ")

    try:
        angka = float(angka)

        if angka < 0:
            print("Input tidak valid. Harap masukkan angka positif.")
        elif angka == 0:
            print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
        else:
            akar = math.sqrt(angka)
            print(f"Akar kuadrat dari {angka} adalah {akar}")
            break

    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang valid.")
