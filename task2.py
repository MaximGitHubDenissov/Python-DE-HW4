'''

Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента,
а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

'''


def dict_swap(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, int | float | str | tuple | frozenset):
            result[value] = key
        else:
            result[str(value)] = key
    return result


print(dict_swap(one=1, two="2", three=[1, 2, 3, 4], four={1, 2, 3, 4}, five=frozenset({1, 2, 3, 4}), six=(4, 5, 6),
                seven={1: "1", 2: "2"}))
