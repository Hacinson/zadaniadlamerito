from collections import Counter

data = [{'item': 'item1', 'amount': 400},
        {'item': 'item2', 'amount': 300},
        {'item': 'item1', 'amount': 750}]

combined_counter = Counter()

for d in data:
    combined_counter[d['item']] += d['amount']

print("Combined values in the list of dictionaries:")
print(combined_counter)
