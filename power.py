def power(basis :int, exponent :int) -> int:
	sum = basis
	for i in range(1, exponent):
		sum *= i
	return sum
