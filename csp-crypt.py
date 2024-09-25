from itertools import permutations

def is_valid_mapping(mapping, words, result):
    total = 0
    for word in words:
        num = int(''.join(str(mapping[char]) for char in word))
        total += num
    return total == int(result)

def solve_cryptarithmetic(words, result):
    unique_chars = set(''.join(words) + result)
    
    if len(unique_chars) > 10:
        return None

    for perm in permutations(range(10), len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        
        if any(mapping[word[0]] == 0 for word in words + [result]):
            continue
        
        if is_valid_mapping(mapping, words, result):
            return mapping

    return None

def print_solution(mapping):
    if mapping is None:
        print("No solution exists.")
    else:
        print("Valid mapping:")
        for char, digit in mapping.items():
            print(f"{char} -> {digit}")

words = ["SEND", "MORE"]
result = "MONEY"

mapping = solve_cryptarithmetic(words, result)
print_solution(mapping)
