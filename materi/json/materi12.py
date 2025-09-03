import json
print("materi 12")
print("                -----------")
file_json_path = r"C:\Users\Admin\OneDrive\Desktop\phyton\json\rukun_islam.json"
with open(file_json_path, "r") as file_json:
    data_json = json.load(file_json)
    print(f"judul file: {data_json['judul']}")
    print(f"jumlah rukun islam: {data_json['jumlah']}")
    print(f"daftar rukun islam:")
    for item_rukun in data_json['rukun']:
        print(item_rukun)
    print("-" * 45)
    print("daftar 3 surah di al quran")
    print("-" * 45)
    # tampilkan surat sebagai tabel
    # keys nomor,nama,jumlah ayat, tempT TURUN
    print("| No | Nama | Jumlah Ayat | Tempat Turun")
    print("-" * 45)
    for surah in data_json['surah']:
        print(f"| {surah['nomor']} | {surah['nama']} | {surah['jumlah ayat']} | {surah['tempat turun']} | ")
