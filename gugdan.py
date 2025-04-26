start = int(input("곱의 시작 숫자를 입력하세요.")) # 2
end = int(input("곱의 마지막 숫자를 입력하세요.")) # 8
dan = int(input("단 숫자를 입력하세요."))
while start <= end:
    print(f"{dan} * {start} = {dan * start}")
    start = start + 1