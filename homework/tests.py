import math
def test_even_fucntion():
     """
     Необходимо реализовать функцию even_filter, которая получает неограниченное количество аргументов
     и возвращает из них только четные.
     """
 
    def even_filter(*args):
        pass

	    return[i for i in args if i % 2 == 0]
    assert even_filter(1, 2, 3, 4, 5, 6) == [2, 4, 6]
 
 
def test_increment_decorator():
     """
     Необходимо реализовать декоратор increment_derocator, который увеличивает полученное значение на 1 и передает его в
     декрорируемую функцию.
     """
    def increment_derocator(func):
        pass
        def wrapper(value):
            func(value+1)
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
            pass
            self.p1 = p1
            self.p2 = p2
 
        def length(self):
            return 0
            length = math.hypot(self.p1.x - self.p2.x, self.p1.y - self.p2.y)
            return lenght
 
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert Segment(p1, p2).length() == 5.0
    assert Segment(p2, p1).length() == 5.0
