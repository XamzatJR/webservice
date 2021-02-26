import random
from string import digits, ascii_letters, punctuation

print("".join(random.choices(digits + ascii_letters + punctuation, k=64)))
