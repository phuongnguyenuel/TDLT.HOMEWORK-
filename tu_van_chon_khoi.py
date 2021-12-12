mon = ['toan', 'ly', 'hoa', 'sinh', 'su', 'dia', 'van', 'anh']
tenkhoi = ['A', 'B', 'C', 'D']

def nhap_diem():
    ds_diem = []
    for i in range(len(mon)):
        print('nhap diem mon', mon[i], end=": ")
        diem = float(input())
        ds_diem.append(diem)
    return ds_diem

def tinhdiemkhoi(mon1, mon2, mon3):
    khoi = mon1*2 + mon2 + mon3
    return khoi

def indiemkhoi():
    for i in range(len(diemkhoi)):
        print('DIEM KHOI', tenkhoi[i], 'LA', diemkhoi[i] )

ds_diem = nhap_diem()

khoiA = tinhdiemkhoi(ds_diem[0], ds_diem[1], ds_diem[2])
khoiB = tinhdiemkhoi(ds_diem[3], ds_diem[0], ds_diem[2])
khoiC = tinhdiemkhoi(ds_diem[6], ds_diem[2], ds_diem[3])
khoiD = tinhdiemkhoi(ds_diem[7], ds_diem[0], ds_diem[6])
diemkhoi = [khoiA, khoiB, khoiC, khoiD]
indiemkhoi()

khoicaonhat = [0, 0]
for i in range(len(diemkhoi)):
    if diemkhoi[i] > khoicaonhat[0]:
        khoicaonhat[0] = diemkhoi[i]
        khoicaonhat[1] = tenkhoi[i]
print('Ban nen thi khoi', khoicaonhat[1])


