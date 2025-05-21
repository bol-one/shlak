import keyboard
import time
import random
import sys

print("Введите текст (Ctrl+Z, а затем enter для завершения)")

text = sys.stdin.read()

a = float(input('Введите задержку сообщений (в секундах): '))
x, y = map(int, input('рандом от x до y (1 10): ').split())
text = text.split()
print('У тебя 3 секунды перейти')
time.sleep(3)

while text:
    i = random.randint(x, y)
    print(text[:i])
    time.sleep(a)
    keyboard.write(' '.join(text[:i]))
    keyboard.send('enter')
    del text[:i]
