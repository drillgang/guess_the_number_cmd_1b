import os
import random
import sys

class GTN:
    
    def __init__(self):
        
        """
        init object
        """
        self.number=random.randint(-1000,1000)
    
    def ans(self,val):
        
        """
        func that determines the correctness of guessing a number
        """
        
        os.system("clear")
        
        if val==self.number:
            print("Вы угадали, хотите повторить?")
            print("1. Да")
            print("0. Нет")
            answer=int(input())
            if answer==1:
                os.system("clear") 
                self.number=random.randint(-1000,1000)
                self.guessnumber()
            elif answer==0:
                os.system("clear")
                print("Выход")
                sys.exit(2)
            else:
                print("Неверный ввод")
        elif val>self.number:
            os.system("clear")
            print("Вы ошиблись, выбранное число меньше, попробуйте еще раз")
            self.guessnumber()
        elif val<self.number:
            os.system("clear")
            print("Вы ошиблись, выбранное число больше, попробуйте еще раз")
            self.guessnumber()
                
    def guessnumber(self):
        
        """
        func that control input number
        """
        
        print(self.number)
        print("Введите число: (если хотите выйти введите '-') ")
        answer=str(input())
        if answer:
            if answer=="-":
                os.system("clear")
                print("Выход")
                sys.exit(2)
            else:
                self.ans(int(answer))
        else:
            os.system("clear")
            print("Неверный ввод,попробуйте еще раз")
            self.guessnumber()
        
if __name__=="__main__":
    print("Число выбрано")
    GTN().guessnumber()