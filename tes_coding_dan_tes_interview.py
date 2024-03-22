nilai_tes_coding = int(input("Nilai coding: "))
hasil_tes_coding = ''


if nilai_tes_coding > 80 and nilai_tes_coding <=100:
    hasil_tes_coding = "LOLOS"
elif nilai_tes_coding >= 60 and nilai_tes_coding<= 80:
    hasil_tes_coding = "DIPERTIMBANGKAN"
elif nilai_tes_coding >= 0 and nilai_tes_coding < 60:
    hasil_tes_coding = "GAGAL"
else:
    print("Input nilai salah")
    
    

nilai_interview = input("Nilai interview: ")
hasil_tes_interview = ''

if nilai_interview == "A" or nilai_interview == "B":
    hasil_tes_interview = "LOLOS"    
else:
    hasil_tes_interview = "GAGAL"
    
if (hasil_tes_coding == "LOLOS" or hasil_tes_coding == "DIPERTIMBANGKAN") and hasil_tes_interview == "LOLOS":
    print("Selamat Kamu Berhasil Menjadi Calon Programmer")
else:    
    print("Maaf Kamu Belum Berhasil Menjadi Calon Programmer")