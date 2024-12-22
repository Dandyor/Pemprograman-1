kode = input()
pesan = input()

if len(kode) != len(pesan):
    print("Panjang Kalimat berbeda, pesan palsu")
else:
    bintang = 0
    pagar = 0

    for i in range(len(kode)):
        if kode[i] == ' ' and pesan[i] == ' ':
            continue
        
        if kode[i] == pesan[i]:
            print("*", end="")
            bintang += 1
        else:
            print("#", end="")
            pagar += 1

    print(f"\n *={bintang}")
    print(f" #={pagar}\n")

    if bintang >= pagar:
        print("Pesan Asli")
    else:
        print("Pesan Palsu")
