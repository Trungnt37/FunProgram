# Cho 2 danh sach, in ra phan tu chung cua chung (Loai bo duplicate)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# My solution
output = []
for i in a:
	if i in b and i not in output:
		output.append(i)
print output

# Sulution
# set(a) tra ve cac phan tu khong trung lap cua a, va sap xep lai theo hasing
c = [x for x in set(a) if x in set(b)]
print c