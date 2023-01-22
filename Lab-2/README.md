Bhumika Purohit - Lab 2
#part1
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
part1 = [x*2 for x in part1]
print(part1)
#part2
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
result = sum(part2)
print(result)
#part3
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21]
result = 0
for i in part3:
    if i%2 == 0:
        result += i
print(result)
