dsip = ['ip13', 'ip13 pro', 'ip13 promax', 'ip mini' ]
dic = {'ip13': 0, 'ip13 pro': 1, 'ip13 promax': 2, 'ip mini':3}
gia = [10, 20, 30, 5]
soluong = [0, 0, 0, 0]
doanhthuiphone = [0, 0, 0, 0]

def tinhdoanhthu(sl, gia):
    doanhthu = sl*gia
    return doanhthu
while True:
     print('Nhap loai ip: ip13, ip13 pro, ip13 promax, ip mini')
     iphone = input()
     sl = int(input('So luong mua: '))
     soluong[dic[iphone]] += sl
     doanhthu = tinhdoanhthu(sl, gia[dic[iphone]])
     doanhthuiphone[dic[iphone]] += doanhthu
     #print(soluong, doanhthuiphone)

     x = input('Nhap "done" neu muon ket thuc!, nhan Enter neu muon tiep tuc')
     if x == "done" :
         break

print('TONG KET CUOI NGAY')
for i in range(len(dic)):
    print('So luong', dsip[i], 'ban duoc la: ', soluong[i] )
    print('Doanh thu',dsip[i],': ', doanhthuiphone[i] )
print('TONG DOANH THU: ', sum(doanhthuiphone))
