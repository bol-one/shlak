from sys import stdin
from pyperclip import copy

print('Потужний текст будет скопирован (чтобы закончить Ctrl+z, а затем enter)')
text = stdin.read()
vowel = 'АаЕеЁёИиОоУуЫыЭэЮюЯя'
for el in vowel:
    text = text.replace(el, 'i')
copy(text)
