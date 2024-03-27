
def check_antisymmetric(relation):
    antisymmetric = all(pair1 == pair2 or (pair1[0] != pair2[1] or pair1[1] != pair2[0]) for pair1 in relation for pair2 in relation)
    if antisymmetric:
        print("Function is antisymmetric")
    else:
        print("Function is not antisymmetric")
    return antisymmetric

def check_transitive(relation):
    transitive = all((a, d) in relation for a, b in relation for c, d in relation if b == c)
    if transitive:
        print("Function is transitive")
    else:
        print("Function is not transitive")
    return transitive

def check_reflexive(set_elements, relation):
    reflexive = all((str(element), str(element)) in relation for element in set_elements)
    if reflexive:
        print("Function is reflexive")
    else:
        print("Function is not reflexive")
    return reflexive

def is_poset(set_elements, relation):
    reflexive = check_reflexive(set_elements, relation)
    antisymmetric = check_antisymmetric(relation)
    transitive = check_transitive(relation)

    return reflexive and antisymmetric and transitive

set_elements = [int(x) for x in input("Enter the set elements (comma-separated): ").split(',')]
relation = []

while True:
    input_relation = input("Enter a relation (Enter 'q' to quit): ")
    if input_relation == 'q':
        break
    a, b = input_relation.split(',')
    relation.append((a, b))
print(relation)
if is_poset(set_elements, relation):
    print("The given set and relation form a POSET.")
else:
    print("The given set and relation do not form a POSET.")
