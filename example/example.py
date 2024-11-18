import math
import ansiplot
from ansiplot.palette import Pretty

x = [(i - 100) * 0.01 for i in range(200)]
y1 = [math.cos(value * 10) for value in x]
y2 = [math.cos(value * 10 + 0.1) for value in x]
y3 = [math.sin(value * 10) for value in x]

plot = ansiplot.Scaled(40, 10, axis=False, palette=Pretty)
plot.plot(x, y1, title="cos")
plot.plot(x, y2, title="cos offset")
plot.plot(x, y3, title="cos")

plot.bar(0, None, symbol=Pretty.separator)
plot.hbar(None, 0, symbol=Pretty.xaxis, title="x=0 or y=0")

plot.show()

with open("example.txt", "w") as file:
    file.write(plot.text(colorless=True))
