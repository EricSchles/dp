def get_fib(n):
	fib = [1,1]
	if n >= 2:
		for i in xrange(2,n):
			fib.append(fib[i-1] + fib[i-2])
	return fib

print get_fib(15)[14]

def r_fib(n):
	if n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return r_fib(n-1) + r_fib(n-2)

print r_fib(15) 
