dsip = ['iphone 13', 'iphone 13 pro', 'iphone 13 promax', 'iphone mini' ]
gia = [10, 20, 30, 5]
soluong = [0, 0, 0, 0]
doanhthuiphone = [0, 0, 0, 0]

def tinhdoanhthu(sl, gia):
    doanhthu = sl*gia
    return doanhthu
while True:
     print('Nhap loai iphone:','0.',dsip[0],'1.',dsip[1],'2.', dsip[2],'3.', dsip[3])
     iphone = int(input())
     sl = int(input('So luong mua: '))
     soluong[iphone] += sl
     doanhthu = tinhdoanhthu(sl, gia[iphone])
     doanhthuiphone[iphone] += doanhthu
     #print(soluong, doanhthuiphone)

     x = input('Nhap "done" neu muon ket thuc!, nhan Enter neu muon tiep tuc')
     if x == "done" :
         break

print('TONG KET CUOI NGAY')
print(soluong, doanhthuiphone)
for i in range(len(dsip)):
    print('So luong', dsip[i], 'ban duoc la: ', soluong[i] )
    print('Doanh thu',dsip[i],':', doanhthuiphone[i] )
print('TONG DOANH THU: ', sum(doanhthuiphone))

