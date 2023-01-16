# Задача 2. В файле находятся названия фруктов. Выведите все фрукты,
# названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.
data = open('spisok_fruit.txt', mode='r', encoding='utf-8')
text = data.readlines()
data.close()

a = input('Введите первую букву фрукта: ')
for elm in text:
    if elm[0] == a:
        print(elm, end='')
