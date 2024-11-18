# ANSIplot

![Compatibility](https://github.com/maniospas/ansiplot/actions/workflows/compatibility.yaml/badge.svg)

<img src="example/example.png" alt="Example image" width="300">

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

Curve differences remain mostly legible,
even for overlapping regions and small canvases.
ANSI is used to color the console output, and any
numeric iterable -such as numpy arrays- can be given as data.

## Read more

[Showcase](example/showcase.md) - see all features in action<br>
[Documentation](example/docs.md) - available methods