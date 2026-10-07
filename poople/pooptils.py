from __future__ import annotations

import string

def is_one_different(first, second):
    diff_chars = 0
    second_lst = list(second)
    for idx, c in enumerate(list(first)):
        if c != second_lst[idx]:
            diff_chars += 1

    return diff_chars == 1

def generate_variants(starting: str, valid_words: list[str] | None = None) -> list[str]:
    starting_lst = list(starting)
    variants = []
    for idx, _ in enumerate(starting_lst):
        for l in string.ascii_lowercase:
            new_word_lst = list(starting_lst)
            new_word_lst[idx] = l

            if valid_words is not None and "".join(new_word_lst) in valid_words:
                variants.append("".join(new_word_lst))


    return variants



# def recursive_poop_search(current_word, path, visited):
#     one_diffs = find_one_diff(current_word)
#     new_path = list(path)
#     new_path.append(current_word)
#     if "poop" in one_diffs:
#         new_path.append("poop")
#         print(new_path)
#     elif len(one_diffs) == 0:
#         print(f"FAIL at {current_word} via {path}")
#     else:
#         for adj in one_diffs:
#             if adj not in visited:
#                 recursive_poop_search(adj, new_path, visited)
#
