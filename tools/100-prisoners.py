from random import shuffle, sample


def look_for_number(target_id, last_paper, remaining_tries):
    """
    Le prisonnier ouvre la boîte correspondant à son `target_id`,
    puis celle indiquée par `last_paper`, et ainsi de suite.
    Renvoie `True` si le prisonnier de numéro `target_id` trouve son numéro, `False` sinon.
    """
    if remaining_tries == 0:
        return False
    new_paper = boxes[last_paper]
    return new_paper == target_id or look_for_number(
        target_id, new_paper, remaining_tries - 1
    )


def launch_optimal():
    """
    Lance le problème des 100 prisonniers avec la stratégie optimale.
    Renvoie `True` si tous les prisonniers survivent, `False` sinon.
    """
    for i in range(nb_of_prisoners):
        if not look_for_number(i, i, nb_of_prisoners // 2):
            return False
    return True


def launch_random():
    """
    Lance le problème des 100 prisonniers avec la stratégie aléatoire
    Renvoie `True` si tous les prisonniers survivent, `False` sinon.
    """
    for i in range(nb_of_prisoners):
        # La fonction sample(l, n) renvoie une liste composée de n éléments distincts de l choisis aléatoirement
        random_choices = sample(boxes, nb_of_prisoners // 2)
        if i not in random_choices:
            return False
    return True


# Initialisation des boîtes et des prisonniers
nb_of_prisoners = 100
boxes = [i for i in range(nb_of_prisoners)]

nb_of_iterations = 10000

print("Testons d'abord la méthode aléatoire :")

cmp_alea = 0
for i in range(nb_of_iterations):
    shuffle(boxes)
    if launch_random():
        cmp_alea += 1

print(
    "Avec la méthode aléatoire, les prisonniers ont survécu",
    cmp_alea,
    "/",
    nb_of_iterations,
    "fois, soit un taux de réussite à hauteur de",
    cmp_alea * 100 / nb_of_iterations,
    "%\n",
)

print("Ensuite, la méthode optimale :")

cmp_opt = 0
for i in range(nb_of_iterations):
    shuffle(boxes)
    if launch_optimal():
        cmp_opt += 1

print(
    "Avec la méthode optimale, les prisonniers ont survécu",
    cmp_opt,
    "/",
    nb_of_iterations,
    "fois, soit un taux de réussite à hauteur de",
    cmp_opt * 100 / nb_of_iterations,
    "%\n",
)
