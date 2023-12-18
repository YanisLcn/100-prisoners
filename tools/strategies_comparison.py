from random import sample, shuffle
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np


def find_number(target_id, last_paper, remaining_tries):
    """
    Le prisonnier ouvre la boîte correspondant à son `target_id`,
    puis celle indiquée par `last_paper`, et ainsi de suite.
    Renvoie `True` si le prisonnier de numéro `target_id` trouve son numéro, `False` sinon.
    """
    if remaining_tries == 0:
        return False
    new_paper = boxes[last_paper]
    return new_paper == target_id or find_number(
        target_id, new_paper, remaining_tries - 1
    )


def optimal_strategy():
    """
    Lance le problème des 100 prisonniers avec la stratégie optimale.
    Renvoie `(True, nb_found)` si tous les prisonniers survivent, `(False, nb_found)` sinon.
    `nb_found` est le nombre de prisionniers qui ont trouvé leur numéro.
    """
    nb_found = 0
    for i in range(nb_of_prisoners):
        if find_number(i, i, nb_of_prisoners // 2):
            nb_found += 1

    return nb_found == nb_of_prisoners, nb_found


def random_strategy():
    """
    Lance le problème des 100 prisonniers avec la stratégie aléatoire
    Renvoie `(True, nb_found)` si tous les prisonniers survivent, `(False, nb_found)` sinon.
    `nb_found` est le nombre de prisionniers qui ont trouvé leur numéro.
    """
    nb_found = 0
    for i in range(nb_of_prisoners):
        # La fonction sample(l, n) renvoie une liste composée de n éléments distincts de l choisis aléatoirement
        random_choices = sample(boxes, nb_of_prisoners // 2)
        if i in random_choices:
            nb_found += 1

    return nb_found == nb_of_prisoners, nb_found


def run_strategy(strategy):
    """Lance la stratégie `strategy`
    Retourne `(percentage, prisonners_count_list)` qui représente respectivement
    le pourcentage de succès de la stratégie et
    la liste contenant les occurences que i prisonniers aient trouvé leur numéro
    (0 <= i <= n)
    """
    prisonners_count_dict = dict(
        zip([x for x in range(0, nb_of_prisoners + 1)], [0] * (nb_of_prisoners + 1))
    )

    count_success = 0
    for _ in range(nb_of_iterations):
        shuffle(boxes)
        success, nb_found = strategy()

        prisonners_count_dict[nb_found] += 1

        if success:
            count_success += 1

    percentage = count_success * 100 / nb_of_iterations

    print(
        "Avec la méthode aléatoire, les prisonniers ont survécu",
        count_success,
        "/",
        nb_of_iterations,
        "fois, soit un taux de réussite à hauteur de",
        percentage,
        "%\n",
    )
    return percentage, list(prisonners_count_dict.values())


def compare_strategies_success(random, optimal):
    """Affiche le diagramme de comparaison du succès
    des stratégies aléatoire et optimale.
    """
    _, ax = plt.subplots()

    strategies = ["Aléatoire", "Optimale"]
    probabilities = [random, optimal]
    bar_colors = ["tab:red", "tab:blue"]

    # Ajout des probabilités au diagramme
    bars = ax.bar(strategies, probabilities, color=bar_colors)

    # Ajout des détails du diagramme
    ax.set_ylabel("Probabilité")
    ax.set_ylim(0, 100)
    ax.set_title("Taux de réussite selon la stratégie")
    ax.yaxis.set_major_formatter(PercentFormatter())
    ax.bar_label(bars, fmt="%.3f%%", label_type="edge", color="black", fontsize=10)

    # Affichage du diagramme
    plt.show()


def compare_strategies_outcomes(random_prisonners_record, optimal_prisonners_record):
    """Affiche le diagramme de comparaison des issues
    des stratégies aléatoire et optimale.
    """
    indexes = np.arange(nb_of_prisoners + 1)
    width = 0.4

    # Ajout des données au diagramme
    plt.bar(
        indexes,
        random_prisonners_record,
        width=width,
        label="Aléatoire",
        color="blue",
        alpha=0.7,
        align="center",
    )
    plt.bar(
        indexes + width,
        optimal_prisonners_record,
        width=width,
        label="Optimale",
        color="orange",
        alpha=0.7,
        align="center",
    )

    SMALL_SIZE = 8
    MEDIUM_SIZE = 10
    BIGGER_SIZE = 12

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    # Ajout des détails du diagramme
    plt.xlabel("Nombre de prisonniers qui ont trouvé leur numéro")
    plt.ylabel("Probabilité")
    plt.title("Probabilité que n prisonniers aient trouvés leur numéro")
    plt.legend(title="Stratégie")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(nb_of_iterations))
    plt.xticks(np.arange(0, 101, step=5))

    # Afficher le diagramme
    plt.show()


def show_strategies_comparison(random_result, optimal_result):
    """Affiche les diagrammes de comparaison des aléatoire et optimale"""
    random_percentage, random_prisonners_record = random_result
    optimal_percentage, optimal_prisonners_record = optimal_result

    compare_strategies_success(random_percentage, optimal_percentage)
    compare_strategies_outcomes(random_prisonners_record, optimal_prisonners_record)


def run_comparison():
    print("Testons d'abord la méthode aléatoire :")

    random_strategy_results = run_strategy(random_strategy)

    print("Ensuite, la méthode optimale :")

    optimal_strategy_results = run_strategy(optimal_strategy)

    print("Voici un diagramme en barres:")
    show_strategies_comparison(random_strategy_results, optimal_strategy_results)


if __name__ == "__main__":
    # Initialisation des boîtes et des prisonniers
    nb_of_iterations = 10000
    nb_of_prisoners = 100
    boxes = [i for i in range(nb_of_prisoners)]
    run_comparison()
