class Calculator:
  def subtract(self, a, b):
    return a-b
  
  def divide(self, a, b):
    return a/b
  
  def add(self, *args):
    return sum(args)
  
  def multiply(self, *args):
    product = 1 
    for i in args:
      product *= i
    return product
  


if __name__ == "__main__":
  calc = Calculator() 
  print(calc.subtract(2,1))
  print(calc.divide(2,1))
  print(calc.add(2,1,3,4,5))
  print(calc.multiply(2,1,3,6,3))

