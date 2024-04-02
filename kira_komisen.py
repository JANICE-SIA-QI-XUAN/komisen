#Atur cara mengira komisen

#Isytihar pemboleh ubah
jumlah=0
jualan=0
komisen=0
ulang="Y"

while ulang=="Y":
    #Input
    jualan=float(input("Masukkan jualan :RM"))
    #proses
    if jualan>80:
        kadar_komisen=0.055
    elif jualan>70:
        kadar_komisen=0.05
    elif jualan>60:
        kadar_komisen=0.04
    elif jualan>50:
        kadar_komisen=0.03
    else:
        kadar_komisen=0.02
    komisen=jualan*kadar_komisen
    #Output
    print("komisen anda ialah RM",round(komisen,2))
    #proses
    jumlah=jumlah+komisen
    #input
    ulang=input("Masukkan Y untuk teruskan pengiraan atau N untuk hentikan pengiraan")
#output
print("\n\t...Anda telah selesai membuat pengiraan...")
    
