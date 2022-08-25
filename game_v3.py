import numpy as np

def super_predict(number:int=1) -> int:
    """Рандомно угадываем число новым способом

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 1
    variant = 50

    while (variant != number):
        if number < variant:
            variant = variant // 2 # уменьшаем искомый интервал в 2 раза влево от предыдущего значения
        else:
            variant += variant // 2 # уменьшаем искомый интервал в 2 раза вправо от предыдущего значения
        count += 1
    return(count)

print(f'Количество попыток: {super_predict()}')


def score_game(super_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
