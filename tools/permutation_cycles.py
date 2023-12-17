def main():
    input_string = input("Veuillez entrez votre permutation sous la forme d'une liste d'entiers séparée par des virugles.\n")
    input_list = [int(s.strip()) for s in input_string.strip().split(",")] 
    print(f"Voici les cycles de la permutation {input_list}:")
    print(f"{permutation_cycles(input_list)}.\n")

def permutation_cycles(permutation: list[int]):
    cycles = []
    visited = [False] * len(permutation)

    while False in visited:
        cycle = []

        start_index = visited.index(False)
        start_element = permutation[start_index]
        cycle.append(start_element)
        visited[start_element - 1] = True

        element = permutation[start_element - 1]

        # Parcours pour former le cycle
        while element != start_element:
            cycle.append(element)
            visited[element - 1] = True

            # Transition
            element = permutation[element - 1]

        cycles.append(cycle)

    # Pour chaque cycle dans cycles, on réarrange le cycle de façon à ce
    # que le minimum débute le cycle
    reordered_cycles = []
    for cycle in cycles:
        index = cycle.index(min(cycle))
        reordered_cycles.append(cycle[index:] + cycle[:index])

    return reordered_cycles

if __name__ == "__main__":
    main()
