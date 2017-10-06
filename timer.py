from time import time, sleep
import pygame
h = input('How many hours?')
m = input('Minutes?')
s = int(input('Seconds?'))
s += int(m) * 60 + int(h) * 3600
timer = time() + s
print('Timer is working...')
sleep(s)
print("Time's up!")
pygame.init()
pygame.mixer.music.load('/home/andrew/you on kazoo.wav')
pygame.mixer.music.play(1)
sleep(6)
