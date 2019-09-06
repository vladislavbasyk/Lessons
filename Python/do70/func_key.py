def func(a, b = 5, c = 10):
    print('a = ', a, ', b = ', b, ', a c =', c)

func(3, 7)
func(25, c = 24)
func(c = 50, a = 100)
func(c = 75, a = 100)