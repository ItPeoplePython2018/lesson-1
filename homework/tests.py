def test_even_fucntion():
    """
    Необходимо реализовать функцию even_filter, которая получает неограниченное количество аргументов
    и возвращает из них только четные.
    """


    def even_filter(*args):
        my_list = []
        for arg in args:
            try:
                arg % 2 == 0
            except TypeError:
                continue
            if arg % 2 == 0:
                my_list.append(arg)
            else:
                pass
        return my_list
    
    assert even_filter(1, 2, 3, 4, 5, 6) == [2, 4, 6]
    assert even_filter(8, 1, 2, 3, 4, 5, 6, "qwe", "asd", 8 , 8) == [8, 2, 4, 6, 8, 8]


def test_increment_decorator():
    """
    Необходимо реализовать декоратор increment_derocator, который увеличивает полученное значение на 1 и передает его в
    декрорируемую функцию.
    """
    def increment_derocator(func):
        def wrapper(value):
            value +=1
            func(value)
            return value
        return wrapper

    @increment_derocator
    def returner(value):
        return value

    assert returner(1) == 2


def test_point_segment_class():
    """
    Дано: есть класс Point, описывающий точку на плоскости. Необходимо закончить класс Segment, описывающий отрезок,
    принимающий на вход 2 точки и позволяющий посчитать его длину.
    Модуль с математическими функциями называется math, документация по нему находится здесь:
    https://docs.python.org/3/library/math.html?highlight=math#module-math
    """

    class Point():
        def __init__(self, x, y):
            self.x = x
            self.y = y


    class Segment():
        def __init__(self, p1, p2):
            self.x1 = p1.x
            self.y1 = p1.y
            self.x2 = p2.x
            self.y2 = p2.y
        
        def length(self):
            return math.sqrt(pow(self.x1 - self.x2 , 2) + pow(self.y1 - self.y2 , 2))
    
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    
    assert Segment(p1, p2).length() == 5.0
    assert Segment(p2, p1).length() == 5.0
