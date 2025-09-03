import csv

print("MATERI 10 - FILE HANDLING")
print("==========================")
# file extension/ekstensi yg membedakan 
# jenis suatu file, lihat di akhir nama file
# .py (python), .doc (document), .txt (text file)
# cari posisi detail file yg mau dibuka
file_path = r"C:\Users\Admin\OneDrive\Desktop\phyton\file\alamat.csv"
# buka file target dengan mode tertentu
file_pesan = open(file_path, "r") # r = read only
# fungsi read() = membaca semua isi file
baca_pesan = file_pesan.read()
print(f"Isi pesannnya: {baca_pesan}")
# tutup file
file_pesan.close()

print('------- OPEN CSV -------')
csv_alamat_path = r"C:\Users\Admin\OneDrive\Desktop\phyton\file\alamat.csv"
with open(csv_alamat_path, "r") as file_alamat:
  baca_alamat = csv.reader(file_alamat)
  list_alamat = list(baca_alamat) # ubah csv object ke list
  print(f"Daftar alamat: {list_alamat}")

print('------- ADD ROW CSV -------')
alamat_khalid = [9,"Khalid","Sukabumi"]
print(f"Alamat baru: {alamat_khalid}")
# buka file dengan mode "a" (append/tambah) 
# beserta newline/baris baru nya kosong atau ""
with open(csv_alamat_path, "a", newline="") as file_alamat:
  tulis_alamat = csv.writer(file_alamat) # targetkan file
  tulis_alamat.writerow(alamat_khalid) # tambah baris baru
  print("--> selesai menambah baris baru ke csv")