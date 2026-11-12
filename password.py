import random

user_input = 4
CHOICES = ["A", "a", "B", "b", "C", "c", "D", "d", "1", "2", "3", "#", "@", "&"]

print(random.choices(CHOICES, k = user_input))