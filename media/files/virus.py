kode = 'print("Я вирус и все испорчу")'

with open('lesson_6.py', 'a', encoding='utf-8') as file:
    file.write(f'\n{kode}\n')

