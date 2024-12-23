# İki sayıyı toplayan ve toplamlarını ikili sayı sisteminde olarak döndüren bir fonksiyon uygulayın. 
# Dönüştürme, toplamadan önce veya sonra yapılabilir.
# Döndürülen ikili sayı bir dize olmalıdır.
# Örnekler: (Input1, Input2 --> Output (açıklama)))
# 1, 1 --> "10" (1 + 1 = ondalık tabanda 2 veya ikili tabanda 10)
# 5, 9 --> "1110" (5 + 9 = ondalık tabanda 14 veya ikili tabanda 1110)


def binaryCevirici(a, b):
    toplam = a + b  
    return bin(toplam)[2:] #oluşturulan değerde 2. indisten sonrasını yazdırdı baştaki 0b yi atmak için.   
    #return bin(toplam)


sayi1 = int(input("Birinci Sayı: "))
sayi2 = int(input("İkinci Sayı: "))


sonuc = binaryCevirici(sayi1, sayi2)
print(f"Sonuç: {sonuc}")

