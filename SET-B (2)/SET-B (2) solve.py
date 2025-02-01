def isPerfectNumber(n):
    if n < 2:
        return False
    divisors = 0
    for i in range(1, n):
        if n % i == 0:
            divisors += i
    return divisors == n
def largestPerfectNumber(nums):
    numbers = []
    for num in nums:
        if isPerfectNumber(num):
            numbers.append(num)
    if numbers:
        return max(numbers) 
    else:
      return -1
def CountPerfectNumber(number):
    count = 0
    for num in number:
        if isPerfectNumber(num): 
            count += 1
    return count
def sumPerfectNumbers(numbers):
    suma = 0
    for numb in numbers:
        if isPerfectNumber(numb):
            suma += numb  
    return suma
nums = [6, 28, 496, 8128, 33550336, 12, 97, 12345]
print("Largest Perfect Number:", largestPerfectNumber(nums))
print("The number of Perfect Numbers:", CountPerfectNumber(nums))  
print("The summation of the Perfect Numbers:", sumPerfectNumbers(nums))
