import string
import time
text = 'kak she ya krut'
a = string.printable
cur = ''
i = 0
while i < len(text):
    for el in a:
        print(cur + el)
        time.sleep(0.00)
        if el == text[i]:
            cur += el
            i += 1
            break
