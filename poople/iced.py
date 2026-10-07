import string, queue
from concurrent.futures.thread import ThreadPoolExecutor

import networkx as nx


from pooptils import is_one_different

STARTING_WORD = "iced"
ENDING_WORD = "poop"
THREADS = 24

VOWELS = ['a', 'e', 'i', 'o', 'u']
CONSONANTS = list("bcdfghjklmnpqrstvwxyz")
LETTERS = list(string.ascii_lowercase)

VALID_WORDS = []

def load_valid_words():
    global VALID_WORDS
    words = []
    with open("words.txt") as f:
        words = f.read().splitlines()

    for word in words:
        VALID_WORDS.append(word.lower().strip())

def find_one_diff(starting):
    global VALID_WORDS

    one_diff_lst = []
    for word in VALID_WORDS:
        if is_one_different(starting, word):
            one_diff_lst.append(word)
    return one_diff_lst

def gen_solution_map():
    visited = set()
    visit_map = {}

    word_queue = queue.Queue()
    word_queue.put(STARTING_WORD)

    while word_queue.qsize() > 0:
        print(word_queue.qsize())

        word = word_queue.get()
        diffs = find_one_diff(word)

        visited.add(word)
        visit_map[word] = diffs

        if "poop" in diffs:
            print(f"POOP FOUND at {word}")
            break

        for adj in diffs:
            if adj not in visited: word_queue.put(adj)

    return visit_map, visited

if __name__ == "__main__":
    load_valid_words()
    print(f"words loaded. length {len(VALID_WORDS)}")

    solution_map, words = gen_solution_map()

    solution_edges = []
    for key, vals in solution_map.items():
        for val in vals:
            solution_edges.append((key, val))

    graph = nx.Graph()
    graph.add_nodes_from(words)
    graph.add_edges_from(solution_edges)
    path = nx.algorithms.dijkstra_path(graph, "coed", "poop")
    print(f"Path: {path}")

