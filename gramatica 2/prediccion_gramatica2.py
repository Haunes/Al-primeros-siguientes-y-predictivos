from primeros_gramatica2 import calculate_first
from siguientes_gramatica2 import calculate_follow_for_grammar

def calculate_prediction_sets(grammar, follow_sets):
    prediction_sets = {}
    
    for non_terminal in grammar: 
        for production in grammar[non_terminal]:
            prediction_set = set()
            first_of_alpha = calculate_first(grammar, production)
            
            if 'ε' in first_of_alpha:
                prediction_set.update(first_of_alpha - {'ε'})
                prediction_set.update(follow_sets[non_terminal])
            else:
                prediction_set.update(first_of_alpha)
            
            prediction_sets[(non_terminal, tuple(production))] = prediction_set
    
    return prediction_sets

def predict_production(grammar, prediction_sets, non_terminal, terminal):
    for production in grammar[non_terminal]:
        if terminal in prediction_sets[(non_terminal, tuple(production))]:
            return production
    return None  # No applicable production found for the given terminal


grammar2 = {
    'S': [['A', 'B', 'uno'], ['S', 'dos']], 
    'A': [['dos', 'B'], ['ε']], 
    'B': [['C', 'D'], ['tres'], ['ε']], 
    'C': [['cuatro', 'A', 'B'], ['cinco']], 
    'D': [['seis'], ['ε']]
}

follow_sets = calculate_follow_for_grammar(grammar2)
prediction_sets = calculate_prediction_sets(grammar2, follow_sets)


for non_terminal, first_set in prediction_sets .items():
    print(f"PRED({non_terminal}): {first_set}")
