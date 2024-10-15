# Program Penghitungan Zakat
nama = input('masukan nama : ')
pekerjaan = input('masukan pekerjaan : ')
penghasilan = float(input('masukan penghasilan : '))
penghasilan_tahunan = float(input('masukan penghasiln : '))

# Nisab Zakat
nisab = 85000000

list = ['amil','riqob','Fakir','miskin','gharim gahrimin','mualaf','ibnusabil','fisabilillah']

if (pekerjaan not in list) and (penghasilan * 12 >= nisab):
    print ('wajib membayar zakat')
else:
    print ('Tidak wajib membayar zakat')

print ("Sekian Tugas Kali ini _ Terimakasih")
print ("Semoga Nilainya Bagus")