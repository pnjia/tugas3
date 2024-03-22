nomor_punggung = int(input("Masukkan nomor punggung: "))
posisi = ''
if nomor_punggung % 2 == 0:
    if nomor_punggung >= 50 and nomor_punggung <= 100:
        posisi = "berhak dipilih menjadi capten team"
    else : 
        posisi = "target attacker"
else:
    if nomor_punggung > 90:
        posisi = "Playmaker"
    elif nomor_punggung % 3 == 0 and nomor_punggung % 5 == 0:
        posisi = "keeper"
    else: 
        posisi = "defender"
print("Posisi: "+posisi)   