def determinan(matriks):
  # Inisialisasi
  baris = len(matriks)
  kolom = len(matriks[0])
  sumDiagonalKanan, sumDiagonalKiri = 0, 0 
  indeksKolomKanan, indeksKolomKiri = 0, kolom-1

  # Kalkulasi
  for i in range(kolom):
    indeksBaris, diagonalKanan, diagonalKiri = 0, 1, 1
    
    for j in range(baris): 
      # Diagonal Kanan
      diagonalKanan *= matriks[indeksBaris%baris][indeksKolomKanan%kolom]
      indeksKolomKanan += 1

      # Diagonal Kiri
      diagonalKiri *= matriks[indeksBaris%baris][indeksKolomKiri%kolom] 
      indeksKolomKiri -= 1
     
      indeksBaris += 1
      
    indeksKolomKanan = indeksKolomKanan-kolom+1
    indeksKolomKiri = indeksKolomKiri+kolom+1
    sumDiagonalKanan += diagonalKanan
    sumDiagonalKiri += diagonalKiri
         
  # Hasil
  return (sumDiagonalKanan - sumDiagonalKiri)

    
print("=============PROGRAM DETERMINAN MATRIKS=============")

# Input Baris dan Kolom
baris = int(input("Masukkan jumlah baris : "))
kolom = int(input("Masukkan jumlah kolom : "))

# Deklarasi Array Matriks
matriks = []

print("Silakan masukkan matriks yang ingin dihitung determinannya!")

# Input Matriks
for i in range(baris):
  row = list(map(int, input().split()))
  matriks.append(row)


# Hasil Determinan Matriks
print("\nHasil determinan matriks :", determinan(matriks))
