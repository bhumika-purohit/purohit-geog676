#part1
from functools import reduce
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
result1 = reduce(lambda x, y: x*y, part1)
print('The result of the first part is:', result1) 
#part2
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177] 
result2 = sum(part2) 
print('The result of the second part is:', result2) 
#part3
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
result3 = 0 
for i in part3: 
      if i%2 == 0: 
         result3 += i 
print('The result of the third part is:', result3)