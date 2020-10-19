from faker import Faker
from faker.factory import Factory

# faker 객체 생성
myfake = Faker()

# 이렇게 하면 한국어로 생성 가능 (https://egg-money.tistory.com/112)
Faker = Factory.create
myfake = Faker('ko_KR')

myfake.seed(1)

print(myfake.name()) 
print(myfake.address())
print(myfake.text()) 
print(myfake.sentence())
print(myfake.random_number())

# 이거 pip 업그레이드 하고 pip install faker 해야 돌아감

# Faker.seed(1)
# TypeError: Calling `.seed()` on instances is deprecated. Use the class method `Faker.seed()` instead.
# 라는데 myfake.seed(1) 하면 왜...
# 계속 다르게 뜨는데 뭐지???
# https://faker.readthedocs.io/en/master/fakerclass.html
# 원래 쓰고싶던대로 쓰려면 `Faker = Factory.create`써야한다나봄 (`from faker.factory import Factory` 이거 쓰고)