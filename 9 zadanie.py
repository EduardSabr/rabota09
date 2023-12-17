# -*- coding: utf-8 -*-
import random
import logging
import keyboard as keyb

# Вызов логгера
logging.basicConfig(filename='bochka.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def a(n):
# Генерирует последовательность чисел от 1 до N в случайном порядке.
    logging.info('Игра начинается!')
    posl = list(range(1, n+1))
    random.shuffle(posl)
    return posl

def b(posl):
#Вытаскивает очередной бочонок из последовательности и удаляет его из нее
    barrel = posl.pop(0)
    logging.info(f"Выпал бочонок: {barrel}")
    return barrel

def main():
    while True:
        try:
            N = int(input("Введите количество бочек: "))
            if N <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое положительное число.")
    sequence = a(N)

    # Пока в последовательности остались бочки
    while sequence:
        print("Нажмите Сtrl, чтобы вытащить очередной бочонок ")
        keyb.wait('ctrl')
        barrel = b(sequence)
        print("Вытащен бочонок:", barrel)

if __name__ == '__main__':
    main()
logging.info('Игра закончилась!')