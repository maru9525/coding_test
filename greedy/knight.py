#말의 여행.
#입력된 말의 위치에서 이동할 수 있는 경우의 수를 나타내시오

input_data = input()
row = int(input(input_data[1]))
column = int(ord(input_data[0]))-int(ord('a'))+1

steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]
  if next_row >= 1 and next_row<= 8 and next_column >=1 and next_column<=8:
    result +=1

print(result)