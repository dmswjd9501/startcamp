# number.txt를 읽어서
with open('number.txt', 'r') as file:
    numbers = file.readlines()
print(numbers)
# 리스트로 받아오는게 좋음 (readlines) 

    
# 4
# 3
# 2
# 1
# 0

