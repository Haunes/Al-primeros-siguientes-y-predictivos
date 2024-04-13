from collections import defaultdict

def calculate_first(grammar, symbol):
    first_set = set()

    # Case 1: α is ε
    if symbol == []: 
        first_set.add("ε")
        return first_set

    # Case 2: α = a1a2...an
    # where each ai can be terminal or non-terminal
    first_symbol = symbol[0]

    # Case 2a: If a1 is a terminal
    if isinstance(first_symbol, str) and first_symbol.islower():
        first_set.add(first_symbol)
        return first_set

    # Case 2b: If a1 is a non-terminal
    # Add FIRST(a1) - {ε} to FIRST(α)
    for production in grammar[first_symbol]:
        if production[0] != first_symbol:
            first_set |= calculate_first(grammar, production)
    
    # Case 2c: If ε ∈ FIRST(a1)
    if "ε" in first_set:
        # If α = a1
        if len(symbol) == 1:
            first_set.add("ε")
        # If α = a1a2...an
        else:
            first_set -= {"ε"}
            first_set |= calculate_first(grammar, symbol[1:])

    return first_set

def calculate_first_for_grammar(grammar):
    first = {}
    for non_terminal in grammar:
        first[non_terminal] = set()
    for non_terminal in grammar:
        for production in grammar[non_terminal]:
            first[non_terminal] |= calculate_first(grammar, production)
    return first

grammar2 = {
    'S': [['A', 'B', 'uno'], ['S', 'dos']], 
    'A': [['dos', 'B'], ['ε']], 
    'B': [['C', 'D'], ['tres'], ['ε']], 
    'C': [['cuatro', 'A', 'B'], ['cinco']], 
    'D': [['seis'], ['ε']]
}

# Calculate FIRST sets for the grammar
first_sets = calculate_first_for_grammar(grammar2)

# Print FIRST sets
for non_terminal, first_set in first_sets.items():
    print(f"FIRST({non_terminal}): {first_set}")