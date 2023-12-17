from random import shuffle


def main():
    # Vous avez la possibilité de générer une permutation aléatoire de n éléments
    # ou de renseigner votre propre permutation
    # N'oubliez pas de commenter/décommenter

    # n = 5
    # permutation = random_permutation_cycles(n)

    # Vous pouvez entrer votre propre permutation
    permutation = [1, 3, 2, 6, 4, 5]

    print(f"Voici les cycles de la permutation {permutation}:")
    print(f"{permutation_cycles(permutation)}")


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


def random_permutation_cycles(nb_elements):
    assert nb_elements > 0

    random_permutation = [x for x in range(1, nb_elements + 1)]
    shuffle(random_permutation)

    return random_permutation


if __name__ == "__main__":
    main()
