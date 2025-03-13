def kalkulator():
    print("Kalkulator Sederhana")
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    operasi = input("Masukkan pilihan (1/2/3/4): ")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if operasi == '1':
        print(f"Hasil: {angka1 + angka2}")
    elif operasi == '2':
        print(f"Hasil: {angka1 - angka2}")
    elif operasi == '3':
        print(f"Hasil: {angka1 * angka2}")
    elif operasi == '4':
        print(f"Hasil: {angka1 / angka2}")
    else:
        print("Pilihan tidak valid!")

kalkulator()