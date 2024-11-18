# ANSIplot

![Compatibility](https://github.com/maniospas/ansiplot/actions/workflows/compatibility.yaml/badge.svg)


A small library for legible console plotting in Python. 

## Quickstart

Install the library with `pip install ansiplot`.
Create a canvas of given dimensions
that scales automatically, and plot on it like so:

```python
import ansiplot

x = [(i - 100) * 0.01 for i in range(200)]
square = [value**2 for value in x]

plot = ansiplot.Scaled(30, 10)
plot.plot(x, x, title="tautology")
plot.plot(x, square, title="square")
plot.show()
```

<img src="example/quickstart.png" alt="Quickstart image" width="200">

Plot differences remain mostly legible,
even for overlapping regions and small canvases.
ANSI is used to color the console output.

## Details

For a more detailed example,
prepare three curves:
two similar cosine functions that lie close to 
each other, and a sine function.

```python
import math

x = [(i - 100) * 0.01 for i in range(200)]
y1 = [math.cos(value * 10) for value in x]
y2 = [math.cos(value * 10 + 0.1) for value in x]
y3 = [math.sin(value * 10) for value in x]
```

Import `ansiplot` and create a rectangle
60x10 canvas. This has specific scaling limits,
but you can also use the `Scaled` canvas from
before to automatically detect those limits.
For demonstration purposes,
hide the default axis to add some on specific
locations at the end with `bar` and `hbar`. 
Those forcefully rewrite entries, whereas other
plots try to preserve some overwritten information
from being hidden if they can help it.

```python
import ansiplot
from ansiplot.palette import Pretty

plot = ansiplot.Rect(60, 10, 
     xlimits=(-1, 1), 
     ylimits=(-1, 1), 
     axis=False)
plot.plot(x, y1, title="cos")
plot.plot(x, y2, title="cos offset")
plot.plot(x, y3, title="cos")
# plot a custom axis
plot.bar(0, (-1, 1), symbol="▕▎");
plot.hbar((-1, 1), 0, symbol=Pretty.xaxis, title="x=0 or y=0")
# show
plot.show()
```


<img src="example/example.png" alt="Example image" width="400">

Get the text manually with `plot.text()`.
Both this and the show method have
colorless versions (useful for exporting to
files) and control whether legends are shown.
Here is an example for exporting the canvas
to a file:

```python
with open("example.txt", "w") as file:
    file.write(plot.text(colorless=True, legend=True))
```