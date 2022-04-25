from threading import Thread
import time


def formula1(piloto, velocidade):
    km = 0
    while km <= 100:
        km += velocidade
        time.sleep(0.5)
        print(f'{piloto}: {km}km')


verstappen = Thread(target=formula1, args=['Verstappen', 1.5])
hamilton = Thread(target=formula1, args=['Hamilton', 1.0])

verstappen.start()
hamilton.start()
