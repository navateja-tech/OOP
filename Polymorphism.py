from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Every shape must know how to calculate its own area."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Every shape must know how to calculate its own perimeter."""
        pass

    def __str__(self) -> str:
        # Operator overloading: customizes what str(obj) / print(obj) shows
        return f"{self.__class__.__name__} -> Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, base: float, height: float, a: float, b: float, c: float):
        self.base = base
        self.height = height
        self.a, self.b, self.c = a, b, c   # side lengths, needed for perimeter

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def perimeter(self) -> float:
        return self.a + self.b + self.c


if __name__ == "__main__":
    shapes: list[Shape] = [
        Circle(radius=5),
        Rectangle(width=4, height=6),
        Triangle(base=6, height=4, a=5, b=5, c=6)
    ]

    total_area = 0.0

    for shape in shapes:
        print(shape)              
        total_area += shape.area()

    print(f"\nTotal area of all shapes: {total_area:.2f}")