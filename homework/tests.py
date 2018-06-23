def test_translate():
    """
    Реализовать функцию-переводчик translate. Она принимает на вход 2 значения: переводимую фразу fraze и словарь dictionary.
    Фраза состоит из слов, написанных в нижнем регистре, разделенных пробелом (знаки препинания в фразе отсутствуют).
    Словарь состоит из пар ключ-значение, где каждый ключ это слово на языке оригинале, значение - перевод этого слова.
    Перевод осуществляется пословно. В словаре переведены все слова, которые встречаются в оригинале.

    Для разделения строки на список слов можно воспользоваться методом split(). Пример:
    >>> s = "My little string"
    >>> s.split()
    ['My', 'little', 'string']
    Документация по этому методу: https://docs.python.org/3/library/stdtypes.html#str.split

    Для объединения списка строк в одну, разделенную пробелами можно воспользоваться методом " ".join(l). Пример:
    >>> l = ["My", "little", "string"]
    >>> " ".join(l)
    'My little string'
    Документация по этому методу: https://docs.python.org/3/library/stdtypes.html#str.join
    """
    def translate(fraze, dictionary):
        list = []
        words = fraze.split()
        for word in words:
            for arg in dictionary:
                if arg == word:
                    list.append(dictionary[arg])
        l = " ".joint(list)
        return(l)

    assert translate("hello world", {"hello": "привет", "world": "мир"}) == "привет мир"
    assert translate("привет мир", {"привет": "hello", "мир": "world"}) == "hello world"
    assert translate("я люблю питон", {"я": "i", "люблю": "love", "питон": "python"}) == "i love python"


def test_is_prime():
    """
    Реализовать функцию is_prime, возвращающую, является ли переданное значение простым.
    Простым числом считается такое число, которое целочисленно делится на 1 и на само себя.
    Подробнее про простые числа: https://ru.wikipedia.org/wiki/Простое_число

    Для решения может понадобиться функция range(), которая может принимать 2 числа, и
    генерировать список чисел от a до b, не включая b. Пример:
    >>> list(range(3, 10))
    [3, 4, 5, 6, 7, 8, 9]
    Документация по функции range: https://docs.python.org/3.5/library/stdtypes.html?highlight=range#range
    """

    def is_prime(n):
        if n <= 1:
            return False
        my_list = list(range(2, n))
        for x in my_list:
            if n % 1 == 0:
                returne False
        return True

    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert not is_prime(4)
    assert not is_prime(15)
    assert not is_prime(21)
