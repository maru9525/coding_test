#알파벳 대문자와 숫자가 들어왔을 경우 알파벳을 오름차순으로 정렬한후 그 뒤에 모든 숫자를 더한 값을 이어서 출력
#리스트에 알파벳 별도 저장
#숫자인 경우 따로 합계를 계산

data = input()
result = []
value = 0

for x in data:
  if x.isalpha():
    result.append(x)
  else:
    value += int(x)

result.sort()

if value != 0:
  result.append(str(value))

print(''.join(result))