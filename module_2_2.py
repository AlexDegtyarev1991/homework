first = int(input())
second = int(input())
third = int(input())
if first == second == third:
    print(f'Одинаковых чисел 3')
elif first == second or second == third or first == third:
    print(f'Одинаковых чисел 2')
elif first != second != third:
    print(f'Одинаковых чисел 0')