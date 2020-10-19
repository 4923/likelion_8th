import random

print("☆★☆★ 로또 번호 자동 생성기 ★☆★☆")
print("-"*30)

print("게임 수를 입력하세요!")
game_num = int(input("게임 수:  "))
print("-"*30)

for _ in range(0, game_num):
  num_list = []
  for i in range(6):
    num_list.append(random.randrange(1,46))
  print(num_list)

print("-"*30)
print("☆★☆★ 로또 번호 생성 완료 ★☆★☆")
print("-"*30)