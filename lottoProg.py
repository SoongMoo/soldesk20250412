import random
count = int(input("구매수량을 입력하세요. : ")) #5
cnt = 1
lotto = []
while cnt <= count:
    i = 1
    while i <= 45:
        lotto.append(i)
        i += 1 # i = i + 1
    size = len(lotto) # 45
    y = 1
    while y <= 6:
        size -= 1
        idx = random.randint(0, size) # 44 , 43, 42,41,40,39
        result = lotto.pop(idx) # 44 : 0 ~ 43
        print(result ,end = ", ") 
        y += 1  
    lotto.clear() # lotto:45- 6 : 39
    print()    
    cnt += 1