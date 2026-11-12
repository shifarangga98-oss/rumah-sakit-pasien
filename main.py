
# PROGRAM APOTEK DAN PASIEN RUMAH SAKIT
# Operator Pembanding dan Kondisional

print("====================================")
print(" PROGRAM APOTEK DAN RUMAH SAKIT")
print("====================================")

# DATA 10 JENIS OBAT APOTEK
obat = [
    ["Paracetamol", 10000, 50],
    ["Amoxicillin", 15000, 30],
    ["Antasida", 8000, 20],
    ["Vitamin C", 12000, 40],
    ["Ibuprofen", 13000, 25],
    ["CTM", 5000, 10],
    ["Oralit", 7000, 15],
    ["OBH", 18000, 5],
    ["Omeprazole", 20000, 0],
    ["Salbutamol", 25000, 12]
]

print("\n===== DATA OBAT APOTEK =====")

for nama, harga, stok in obat:
    print("\nNama Obat:", nama)
    print("Harga: Rp", harga)
    print("Stok:", stok)

    if stok == 0:
        print("Status: Stok Habis")
    elif stok < 10:
        print("Status: Stok Hampir Habis")
    else:
        print("Status: Stok Tersedia")

    if harga > 15000:
        print("Kategori: Harga Mahal")
    else:
        print("Kategori: Harga Terjangkau")


# DATA 10 PASIEN OPNAME RUMAH SAKIT
pasien = [
    ["Andi", 25, 2, "Stabil"],
    ["Budi", 45, 5, "Stabil"],
    ["Citra", 30, 3, "Observasi"],
    ["Dewi", 60, 7, "Observasi"],
    ["Eko", 18, 1, "Stabil"],
    ["Fitri", 50, 10, "Pemantauan"],
    ["Gita", 35, 4, "Stabil"],
    ["Hasan", 70, 8, "Pemantauan"],
    ["Indah", 22, 2, "Stabil"],
    ["Joko", 55, 6, "Observasi"]
]

print("\n===== DATA PASIEN OPNAME =====")

for nama, usia, lama, kondisi in pasien:
    print("\nNama Pasien:", nama)
    print("Usia:", usia, "tahun")
    print("Lama Opname:", lama, "hari")
    print("Kondisi:", kondisi)

    if usia >= 60:
        print("Kategori Usia: Lansia")
    elif usia >= 18:
        print("Kategori Usia: Dewasa")
    else:
        print("Kategori Usia: Anak")

    if lama > 7:
        print("Status Rawat: Lebih dari 7 hari")
    elif lama >= 3:
        print("Status Rawat: 3 sampai 7 hari")
    else:
        print("Status Rawat: Kurang dari 3 hari")

    if kondisi == "Stabil":
        print("Status Pasien: Stabil")
    elif kondisi == "Observasi":
        print("Status Pasien: Perlu Observasi")
    else:
        print("Status Pasien: Dalam Pemantauan")


print("\n====================================")
print(" PROGRAM SELESAI")
print("====================================")
