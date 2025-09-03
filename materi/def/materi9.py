def halo_dek(nama):
    print(f"halo dek {nama}")
halo_dek("yulianti")

halo_kak = lambda nama: print(f"halo kak {nama}")
halo_kak("anya")
# higher other funcion map,sorted, filter
uang_jajan = [100000,200000,10000,50000,75000]

#map mentransformasi data item
kurangi_jajan = map(lambda uang: uang - 5000, uang_jajan)
list_kurangi_jajan = list(kurangi_jajan)
print(f"uang jajan: {uang_jajan} ")
print(f"kurangi jajan : {list_kurangi_jajan}")
# sorted mengurutkan data
urutkan_uang = sorted(uang_jajan)
balik_uang = sorted(uang_jajan, reverse=True)
print(f"urutkan uang: {urutkan_uang}")
print(f"urutkan uang terbalik: {balik_uang}")
# filter menyaring data sesuai kondisi
filter_uang_gede = filter(lambda uang: uang > 50000, uang_jajan)
list_uang_gede = list(filter_uang_gede)
print(f"filter uang gede: {list_uang_gede} ")
