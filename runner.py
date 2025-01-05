from calculator import Calculator
import sys

calc = Calculator()
func = ("subtract","divide","multiply","add")

nums = [float(x) for x in sys.argv[2:]]

if sys.argv[1] not in func:
  print("This function does not exist")

else:
  if sys.argv[1] == "add":
    print(calc.add(*nums))

  elif sys.argv[1] == "multiply":
    print(calc.multiply(*nums))

  elif sys.argv[1] == "subtract":
    if len(nums) == 2:
      print(calc.subtract(*nums))
    else:
      print("Only 2 numbers can be subtracted at once")

  elif sys.argv[1] == "divide":
      if len(nums) == 2:
        print(calc.divide(*nums))
      else:
        print("Only 2 numbers can be divided at once")
  