#4.8 연습문제
import random

secret = random.randint(1, 10)
guess = random.randint(1, 10)
if guess < secret :
    print("too low")

elif guess == secret :
    print("just right")

else:
    print("too high")

#4.2

small = True
green = False

if small :
    if green:
        print("완두콩은 작고 녹색이다")
    else:
        print("체리는 작고 녹색이 아니다")
else:
    if green:
        print("수박은 크고 녹색이다")
    else:
        print("호박은 크고 녹색이 아니다")




















