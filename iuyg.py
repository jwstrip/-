import random
print("Игра с кучами камней\n")

try:
    print("Вы хотите ходить первым? 0/1\n")
    p=int(input())
except:
    print("Введено не корректное значение")
flag=-1
if(p==0):
    flag=0
else:
    flag=1
k=int(random.uniform(4,30))
print(f"Кол-во камней в куче:{k}")
while(k>1):
    if(flag):
        try:
            print("Ваш ход. Введите число от 1 до 3:\n")
            i=int(input())
            if(i<1 or i>3):
                 print("Автопроигрыш из-за нарушения правил!")
                 exit()
            if(k-i<1):
                while(k-i<1):
                     print("введите меньшее число. Количество камней в куче не может быть больше 1.\n")
                     i=int(input())
        except:
            print("Автопроигрыш из-за нарушения правил!")
            exit()
        k=k-i
        print(f"Кол-во элементов в куче: {k}")
        if(k==1):
            print("Победа пользователя!")
            break
        print("Ход компьютера:")
        i=int(random.uniform(1,3))
        if(k-i<1):
            while(k-i<1):
                i=random.uniform(1,3)
        k=k-i
        print(f"Кол-во элементов в куче: {k}")
        if(k==1):
            print("Победа компьютера!")
            break
    else:
        print("Ход компьютера:")
        i=int(random.uniform(1,3))
        if(k-i<1):
            while(k-i<1):
                i=random.uniform(1,3)
        k=k-i
        print(f"Кол-во элементов в куче: {k}")
        if(k==1):
            print("Победа компьютера!")
            break
        try:
            print("Ваш ход. Введите число от 1 до 3:\n")
            i=int(input())
            if(i<1 and i>3):
                 print("Автопроигрыш из-за нарушения правил!")
                 exit()
            if(k-i<1):
                while(k-i<1):
                     print("введите меньшее число. Количество камней в куче не может быть больше 1.\n")
                     i=int(input())
        except:
            print("Автопроигрыш из-за нарушения правил!")
            exit()
        k=k-i
        print(f"Кол-во элементов в куче: {k}")
        if(k==1):
            print("Победа пользователя!")
            break
print("Конец игры!")
