"""Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield."""

nums = 19
odd_gen = (num for num in range(1, nums + 1, 2))
for num in odd_gen:
    print(num)
