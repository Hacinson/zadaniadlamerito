import re

def extract_numbers(text):
    numbers = re.findall(r'\d+', text)
    return list(map(int, numbers))

text = "32 leche or 99 chevals"
numbers = extract_numbers(text)

print(f"Original string: {text}")
print(f"Extract numbers from the said string: {numbers}")
