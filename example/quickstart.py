import ansiplot

x = [(i - 100) * 0.01 for i in range(200)]
square = [value**2 for value in x]

plot = ansiplot.Scaled(30, 10)
plot.plot(x, x, title="tautology")
plot.plot(x, square, title="square")
plot.show()
