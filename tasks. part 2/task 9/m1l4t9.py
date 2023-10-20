'''
Задача 9

Оптимизируй код программы

Бо написал программу, которая будет искать 
подходящую по размеру одежду, Бо очень сложно 
иногда самому находить одежду своего размера, 
поэтому он решил сделать это через программу, 
только вот Бо заметил что написанная им программа 
работает медленно, помоги Бо оптимизировать код программы.

Строки кода которые не используются можно убрать.
'''

t_shirt_1 = "зеленая футболка XXL"
shirt_1 = "зеленая рубашка XL"
t_shirt_2 = "фиолетовая футболка XS"
shirt_2 = "фиолетовая рубашка XXL"

right_size = "XXL"
string_size = len(right_size)

t_shirt_1_info = t_shirt_1.endswith(right_size)
shirt_1_info = shirt_1.endswith(right_size) 
t_shirt_2_info = t_shirt_2.endswith(right_size)
shirt_2_info = shirt_2.endswith(right_size)

print("Подходит ли:",t_shirt_1, ":", t_shirt_1_info)
print("Подходит ли:",shirt_1, ":", shirt_1_info)
print("Подходит ли:",t_shirt_2, ":", t_shirt_2_info)
print("Подходит ли:",shirt_2, ":", shirt_2_info)
print()
print()
