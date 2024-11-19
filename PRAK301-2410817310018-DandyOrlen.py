print("Masukkan tiga angka dipisahkan dengan spasi: ")
a, b, c = map(int, input().split())

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print("Urutan dari kecil ke besar:", a, b, c)