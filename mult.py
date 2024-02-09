'''
Karatsuba's basic step works for any base B (Here, 10) and any m (Here, floor(n/2)=32 for 64-digit number), but the recursive 
algorithm is most efficient when m is equal to n/2 (Here, n=64 is number of digits in the number), rounded up.
If number of digits is a power of 2 i.e., n = 2^k, recursion stops only when n = 1, then the number of single-digit
multiplications is 3^k i.e., n^c where c = lg(3).

Though one can extend any inputs with zero digits until their length is a power of 2, it follows that the number of elementary 
multiplications, for any n, is atmost 3^lg(n) <= 3 * n^lg(3).
'''

# Given 64-digit numbers
num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627


# Karatsuba's algorithm
def karatsuba (num1, num2):

	if len(str(num1)) == 1 or len(str(num2)) == 1:
		return num1 * num2
	else:
		m = max (len(str(num1)), len(str(num2)))
		m2 = m // 2

		a = num1 // 10**(m2)
		b = num1 % 10**(m2)
		c = num2 // 10**(m2)
		d = num2 % 10**(m2)

		stepOne = karatsuba (b, d)
		stepTwo = karatsuba (a + b, c + d)
		stepThree = karatsuba (a, c)

		return (stepThree * 10**(2*m2)) + ((stepTwo - stepThree - stepOne) * 10**(m2)) + (stepOne)

result = karatsuba (num1, num2)

print("Product of the given two numbers", num1, "&", num2, "is", result)

