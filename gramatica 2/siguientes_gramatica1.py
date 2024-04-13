from primeros_gramatica2 import calculate_first


def calculate_follow_for_grammar(grammar):
    follow = {}
    # Initialize FOLLOW sets for all non-terminals
    for non_terminal in grammar:
        follow[non_terminal] = set()

    # Add $ to FOLLOW(S), where S is the start symbol of the grammar
    start_symbol = next(iter(grammar))  # Get the first key in the grammar dictionary
    follow[start_symbol].add('$')

    # Iteratively calculate FOLLOW sets until no changes occur
    while True:
        updated = False
        for non_terminal in grammar:
            current_follow_set = follow[non_terminal].copy()
            for left_symbol in grammar:
                for production in grammar[left_symbol]:
                    # Find occurrences of non_terminal in production
                    for i in range(len(production)):
                        if production[i] == non_terminal:
                            if i < len(production) - 1:
                                # Case 2a: Add FIRST(β) - {ε} to FOLLOW(A)
                                first_of_beta = calculate_first(grammar, production[i + 1:])
                                follow[non_terminal].update(first_of_beta - {'ε'})
                                # Case 2b: If ε in FIRST(β), add FOLLOW(left_symbol) to FOLLOW(A)
                                if 'ε' in first_of_beta:
                                    follow[non_terminal].update(follow[left_symbol])
                            else:
                                # Case 2b (production ends with non_terminal): Add FOLLOW(left_symbol) to FOLLOW(A)
                                follow[non_terminal].update(follow[left_symbol])
            
            # Check if FOLLOW(non_terminal) has changed
            if follow[non_terminal] != current_follow_set:
                updated = True
        
        # If no changes were made in this iteration, stop
        if not updated:
            break
    
    return follow

grammar2 = {
    'S': [['A', 'B', 'uno'], ['S', 'dos']], 
    'A': [['dos', 'B'], ['ε']], 
    'B': [['C', 'D'], ['tres'], ['ε']], 
    'C': [['cuatro', 'A', 'B'], ['cinco']], 
    'D': [['seis'], ['ε']]
}

follow = calculate_follow_for_grammar(grammar2)

for non_terminal, first_set in follow.items():
    print(f"FOLLOW({non_terminal}): {first_set}")
