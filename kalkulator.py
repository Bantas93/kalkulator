#KALKULATOR SEDERHANA 
def tambah(a,b):
    tambah = int (a) + int (b)
    return tambah
def kurang(a,b):
    kurang = int (a) - int (b)
    return kurang
def bagi(a,b):
    bagi = int (a) / int (b)
    return bagi
def kali(a,b):
    kali = int (a) * int (b)
    return kali

while True :
    print  ('========== KALKULATOR ==========')
    a = input ('Masukan bilangan 1: ')
    b = input ('Masukan bilangan 2: ')
    print ('\n 1. Penjumlahan\n 2. Pengurangan\n 3. Pembagian\n 4. Perkalian\n 5. Ga jadi deh ')
    print ("")
    c = input ('Silahkan pilih 1-5 = ')
    print ("")
    if c == '1':
        print ('Maka Hasilnya adalah ',tambah( a,b ))
    elif c == '2':
        print ('Maka hasilnya adalah ', kurang (a,b))
    elif c == '3':
        print ('Maka hasilnya adalah ', bagi (a,b))
    elif c == '4':
        print ('Maka hasilnya adalah ', kali (a,b))
    elif c == '5':
        break
    else:
        print ('Error')
    print ("")

    # Note : tanda '==' bisa diganti dengan tanda 'is'
    


