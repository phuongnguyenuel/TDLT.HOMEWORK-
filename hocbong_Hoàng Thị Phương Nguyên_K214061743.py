def nhapsinhvien():
    n = int(input("So sinh vien: "))
    lstten = []
    for i in range(n):
        ten = input("Ten sinh vien " + str(i+1) + " : ")
        lstten.append(ten)
    return lstten
def tinhdiemtbcua1sv(ten):
    mon = ['TDLT', 'TCC']#, 'GTN', 'KTVM', 'LLNN', 'TTHCM']
    STC = [3, 3, 2, 3, 3, 2]
    print("Diem cua ban ", ten)
    while True:
        try:
            drl = float(input('Nhap diem ren luyen: '))
        except:
            print('Diem ren luyen k hop le. Moi nhap lai')
        else:
            break
    tongcacmon = 0
    for i in range(len(mon)):
        print('nhap diem mon', mon[i], end=':')
        while True:
            try:
                diem = float(input())
            except:
                print('Diem k hop le. Moi nhap lai', end=':')
            else:
                break
        s = diem * STC[i]
        tongcacmon += s
    GPA = tongcacmon/sum(STC)
    tongdiem = GPA + drl*20/100
    print('Tong: ', tongdiem)
    return tongdiem
lstten = nhapsinhvien()

ds_diem = []
for i in lstten:
    ds_diem.append([tinhdiemtbcua1sv(i), i])

ds_diem = sorted(ds_diem)[::-1]
print(ds_diem)
print('5 BAN DAT HOC BONG: ')
for a in ds_diem[:3]:
    print(a[0])
  

