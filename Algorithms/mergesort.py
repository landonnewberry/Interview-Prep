def mergesort(a):
	def combine(x, y):
		ix = iy = 0
		c = list()
		while True:
			if (len(x) == ix) and (len(y) == iy):
				return c
			elif len(x) == ix:
				c.append(y[iy])
				iy += 1
			elif (len(y) == iy) or (x[ix] <= y[iy]):
				c.append(x[ix])
				ix += 1
			else:
				c.append(y[iy])
				iy += 1
	if len(a) == 2:
		return [min(a[0],a[1]), max(a[0],a[1])]
	elif len(a) <= 1:
		return a
	else:
		return combine(
			mergesort(a[:len(a) // 2]),
			mergesort(a[len(a) // 2:])
		)
