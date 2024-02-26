import random
from graph import Graph

def parse_text(filename):
    with open(filename, 'r') as file:
        text = file.read().lower()
     
        text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text)
       
        words = text.split()
    return words

def generate_markov_chain(words):
    graph = Graph()
    prev_word = None
    for word in words:
        if prev_word is not None:
            graph.add_edge(prev_word, word)
        prev_word = word
    return graph

def compose_text(graph, length):
    composition = []
    current_word = random.choice(list(graph.vertices))
    for _ in range(length):
        composition.append(current_word)
        next_word = graph.get_random_neighbor(current_word)
        current_word = next_word
    return ' '.join(composition)

if __name__ == "__main__":
    filename = 'texts/hp_sorcerer_stone.txt'
    words = parse_text(filename)
    graph = generate_markov_chain(words)
    composition_length = 100 
    composition = compose_text(graph, composition_length)
    print(composition)
