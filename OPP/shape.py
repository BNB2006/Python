# Q1. Write a program to create a class Shape having to variables length and width. Also having one function which display area of rectangle. 

# class
class Shape:
    def __init__(self, length, width):
        self.lenght = length
        self.width = width
    
    def areOfRectangle(self):
        result = self.lenght * self.width
        print(f"Area of rectangle is: {result}m")

# main function
def main():
    rectangle = Shape(30,10)
    rectangle.areOfRectangle()

if __name__ == main():
    main()
