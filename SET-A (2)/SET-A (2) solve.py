def isSquareNumber(num):
      if num < 0:
        return False
      for i in range(1,num+1):
          if i*i==num:
              return True
          elif i*i>num:
              break
      return False
def largestSquareNumber(number):
      largest_number=0
      for i in number:
            if isSquareNumber(i):
                  if i>largest_number:
                        largest_number=i
      return largest_number
def countSquareNumbers(number):
     sum=0
     for i in number:
      if isSquareNumber(i):
            sum+=1
     return sum
def sumSquareNumbers(number):
     count=0
     for i in number:
          if isSquareNumber(i):
               count+=i
     return count
numbers = [16, 23, 25, 2, 9, 36, 50, 81]
print(f"Largest Square Number: {largestSquareNumber(numbers)}")
print(f"The number of Square Numbers: {countSquareNumbers(numbers)}")
print(f"The sum of the Square Numbers: {sumSquareNumbers(numbers)}")