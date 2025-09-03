# buat fungsi dengan 'def' lalu nama fungsinya
def hello():
    print ("hello")
    print ("dunia")
# panggil nama fungsi dengan ()
hello()
# parameter 'nama' untuk mengambil nilai dari luar ke isi fungsi
def hello(nama):
    print ("hello")
    print ("halo mr ", nama)
hello("ishaq")
# fungsi luas persegi panjang
def luas_persegi_panjang (panjang, lebar):
    print("p =", panjang)
    print("l =", lebar)
    rumus = panjang * lebar
    print("hasil luas persegi panjang =", rumus)
def halo_dek(nama):
    print(f"halo dek {nama}")
halo_dek("yulianti")

halo_kak = lambda nama: print(f"halo kak {nama}")
halo_kak("anya")

luas_persegi_panjang(10, 5)
luas_persegi_panjang(100, 50)