#materi phyton data structures
#list = []urut.berubah,boleh duplikat
#index=urutan
daftar = [
    "pisang", #index 0
    "susu,", #index 1
    "gabin", #index 2
    "teh", #index 3
]
print("tas belanja:", daftar)
# akses item dengan index
print(daftar[1])
# append () untk menambah item ke akhir list
daftar.append("teh desa")
# insert () untk menambah item ke index tertentu
daftar.append("kopi")
daftar.insert(1, "batagor")
# remove () untuk menghapus item 
daftar.remove("pisang")
print("tas belanja sekarang: ",daftar)
# menggabungkan list +
jajan_ishaq = ["olive","macaroni","keripik"]
jajan_bilal = ["naspad","mie","jajan"]
titip_belanjaan = jajan_bilal + jajan_ishaq
print("titipan belanja : ", titip_belanjaan)
# menggandakan item list dengan ****
print("bilal nambah: ", jajan_bilal * 3)
# list bercabang (list multi dimensi)
daftar_menu = [
    ["kopi", "teh", "susu jahe"], # baris 0
    ["jus apel", "jus jeruk", "jus alpukat", "jus mangga"], # baris 1
    ["es teler", "es dawet"] # baris 2
]
print("daftar menu :",daftar_menu)
print(daftar_menu[1][2])
print("    ")
# tuple () berurutan ,tdk berubah,boleh duplikat 
ttl = ("purworejo", 21, "januari", 2009)
print("ttl :", ttl )
print("bulan lahir ujang:", ttl[2])
# unpacking variable (mengekstrak tuple ke variable baru sesuai urutan)
tempat_lahir, tgl_lahir, bln_lahir, thn_lahir = ttl
print("tahun lahir: ", thn_lahir)
# set {} tdk berurutan,berubah tdk duplikat
game_ridho = {"ghensin","mlbb","delta force"}
game_imam = {"valorant","point blank"}
# add()menambahkan itemke set
game_ridho.add("valorant")#jika sudah ada akan di 
game_imam.add("mlbb")
#remove()untk menghapus item dari set
game_ridho.remove("mlbb")
# len (menghitung jumlah item)
print("ridho ada ",len(game_ridho), "= ", game_ridho)
print("imam ada ",len(game_imam), "= ", game_imam)
# union () menggabungkan 2set yg berbeda
game_gabungan = game_imam.union(game_ridho)
total_game = len(game_gabungan)
print("game gabungan ",total_game,"=",game_gabungan)
# intersection () mencari item yang kembar dari 2 set berbeda
# difference ()mencari item yang  beda dari 2 set berbeda
game_kembar = game_ridho.intersection(game_imam) 
game_beda = game_ridho.difference(game_imam)
print("game kembar ", game_kembar)
print("game berbeda ", game_beda)
# dict dictionary {key=value}
# berurutan berdasarkan key, berubah,tdk duplikat
daftar_anime = {
    "jujutsu_kaisen": "gojo satoru", 
    "one_puch_man": "saitama",
    "jigoku_roku": "sagiri",
    "waifu": {
        "demon_slayer": "mitsuri",
        "spy_x_family": "anya",
        "naruto": "tsunade"
    }
}
print("daftar anime", daftar_anime)
print("mc one puch man", daftar_anime["one_puch_man"])
print("waifu loli", daftar_anime["waifu"]["spy_x_family"])
# mengubah item value bedasarkan key
daftar_anime["one_puch_man"] = "genos"
daftar_anime["waifu"]["demon_slayer"] = "nezuko"
print("mc one puch man baru ", daftar_anime["one_puch_man"])
print("waifu loli bisa gede ",daftar_anime["waifu"]["demon_slayer"])
# menambah item value bedasarkan key
daftar_anime["wind_breker"] = "sakura" 
print("mc wind breker ", daftar_anime["wind_breker"])
