"""
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
```
Подсказка: использовать возможности python, изученные на уроке."""
from time import perf_counter
from sys import getsizeof

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = (src[idx] for idx in range(1, len(src)) if src[idx] > src[idx - 1])
print('1. Результат:', *result)

# Оптимизация по памяти
start = perf_counter()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = (src[idx] for idx in range(1, len(src)) if src[idx] > src[idx - 1])
print('2. Результат:', *result)
print('Время:', perf_counter() - start)
print('Память:', getsizeof(result))

# Оптимизация по скорости
start = perf_counter()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [src[idx] for idx in range(1, len(src)) if src[idx] > src[idx - 1]]
print('3. Результат:', result)
print('Время:', perf_counter() - start)
print('Память:', getsizeof(result))
