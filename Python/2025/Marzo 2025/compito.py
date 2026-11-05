def doppio(q):
    counter = 0
    for i in range(1, len(q)):
        if q[i] == q[i-1]*2:
            counter += 1
    return counter


def frequenza(nums):
    f = []
    for num in nums:
        f.append(nums.count(num))
    i = f.index(max(f))
    return nums[i]


print(f"Numeri doppi totali nella lista: {doppio([4, 3, 6, 12, 10, 19])}")
print(f"Questo numero ha frequenza maggiore nella lista: {frequenza([4, 3, 7, 12, 3, 12])}")
