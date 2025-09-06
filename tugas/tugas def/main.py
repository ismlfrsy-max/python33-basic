import doa_harian
import hitung_uang
import ranking

print("=== Doa Harian ===")
print(doa_harian.doa_tidur())
print(doa_harian.doa_bangun())
print(doa_harian.doa_makan())

print("\n=== Hitung Uang Jajan ===")
jajan = [50000, 30000, 15000, 70000, 10000]
print("Asli:", jajan)

bonus = hitung_uang.tambah_bonus(jajan)
print("Setelah ditambah bonus 5000:", bonus)

boros = hitung_uang.filter_boros(jajan)
print("Yang boros (>= 50000):", boros)

print("\n=== Ranking Nilai ===")
nilai = [75, 90, 60, 88, 100, 55]
print("Asli:", nilai)

urut = ranking.urutkan_nilai(nilai)
print("Urut Descending:", urut)

print("Nilai Tertinggi:", ranking.nilai_tertinggi(nilai))
print("Nilai Terendah :", ranking.nilai_terendah(nilai))
