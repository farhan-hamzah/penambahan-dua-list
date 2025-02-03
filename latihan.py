nums = list(map(int, input("Masukan Array: ").split()))
n = list(map(int, input("Masukan Array: ").split()))

hasil = []
carry = 0 
for i in range(len(nums)):
    jumlah = nums[i] + n[i] + carry
    hasil.append(jumlah % 10)
    carry = jumlah // 10 
if carry > 0:
    hasil.append(carry)

print(hasil)