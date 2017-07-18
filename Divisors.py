# Nhap vao mot so, in ra danh sach cac uoc cua no
N = int(raw_input("Enter N: "))
b = []
for i in range(1, N/2 + 1):
	if N % i == 0:
		b.append(i)
print "Uoc cua %d la: " %N, b
if N == sum(b):
	print  "%d la so hoan hao." %N
else:
	print "%d khong phai la so hoan hao." %N
