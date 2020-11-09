#정수 N을 입력받아 N시 59분 59초에서 3이 하나라도 포함된 시각의 수는?

h = int(input())

count = 0 
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count +=1

print(count)