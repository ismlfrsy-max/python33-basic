import csv
from collections import defaultdict

# Buka semua file CSV
with open("keuangan.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)
# 1️⃣ Tampilkan Semua Data
print("=== Semua Data ===")
for row in data:
    print(f"{row['Tanggal']} | {row['Keterangan']} | {row['Kategori']} | Rp{row['Jumlah']}")

# 2️⃣ Hitung Total Pengeluaran
total_pengeluaran = sum(int(row["Jumlah"]) for row in data)
print("=== Total Pengeluaran ===")
print(f"Total Pengeluaran: Rp{total_pengeluaran}")
# sum untuk menahbah
# 3️⃣ Hitung Total per Kategori
kategori_total = defaultdict(int)
for row in data:
    kategori_total[row["Kategori"]] += int(row["Jumlah"])

print("\n=== Pengeluaran per Kategori ===")
for kategori, total in kategori_total.items():
    print(f"- {kategori}: Rp{total}")

# 4️⃣ Cari Kategori dengan Pengeluaran Terbesar
kategori_terbesar = max(kategori_total, key=kategori_total.get)
print("\n=== Kategori Terbesar ===")
print(f"Kategori Terbesar: {kategori_terbesar} (Rp{kategori_total[kategori_terbesar]})")

# 🎲 Tantangan Tambahan (Opsional)
# Cari tanggal dengan pengeluaran terbanyak
tanggal_total = defaultdict(int)
for row in data:
    tanggal_total[row["Tanggal"]] += int(row["Jumlah"])

tanggal_terbesar = max(tanggal_total, key=tanggal_total.get)

print("\n=== Tantangan Tambahan ===")
print(f"Tanggal dengan pengeluaran terbanyak: {tanggal_terbesar} (Rp{tanggal_total[tanggal_terbesar]})")

# Hitung rata-rata pengeluaran per hari
rata_rata = total_pengeluaran / len(tanggal_total)
print(f"Rata-rata pengeluaran per hari: Rp{int(rata_rata)}")
