print("===== TUGAS KELOMPOK 10 =====")
print("===== NAMA : Feby Alliya Putri =====")
print("===== KELAS : 1A =====")
#dictionary menyimpan informasi tentang buah-buahan Dan menampilkan informasi tentang buah-buahan 
buah = {
    'Apel': 'Merah , Menstabilkan Gula darah dan menurunkan resiko Stroke',
    'Mangga': 'Hijau, Mencegah Penyakit jantung dan menurunkan tekanan darah tinggi',
    'Anggur': 'Ungu, Membantu pembekuan darah secara efektif dan membantu mencegah anemia'
}

#input user
nama_buah = input("Silahkan pilih nama buah dibawah ini :\n* Apel\n* Mangga\n* Anggur\nSilahkan memilih...\n")

#tampilin informasi
if nama_buah in buah:
    print(f"Informasi tentang {nama_buah}: {buah[nama_buah]}")
else:
    print("Sori kawan e tidak ada buah itu.")