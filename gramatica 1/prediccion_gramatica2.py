from primeros_gramatica1 import calculate_first
from siguientes_gramatica1 import calculate_follow_for_grammar

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


grammar1 = {
    'S': [['A', 'uno', 'B', 'C'], ['S', 'dos']], 
    'A': [['B', 'C', 'D'], ['A', 'tres'], ['ε']], 
    'B': [['D', 'cuatro', 'C', 'tres'], ['ε']], 
    'C': [['cinco', 'D', 'B'], ['ε']], 
    'D': [['seis'], ['ε']]
}

follow_sets = calculate_follow_for_grammar(grammar1)
prediction_sets = calculate_prediction_sets(grammar1, follow_sets)


for non_terminal, first_set in prediction_sets .items():
    print(f"PRED({non_terminal}): {first_set}")
