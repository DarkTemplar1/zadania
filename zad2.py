from typing import List


def find_missing_elements(elements: List[int], n: int) -> List[int]:
    full_set = set(range(1, n + 1))
    given_set = set(elements)
    missing_elements = sorted(full_set - given_set)

    return missing_elements


input_list = [2, 6, 8, 4, 9]
n = 10
result = find_missing_elements(input_list, n)
print(result)
