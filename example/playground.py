import ansiplot

values = {
    "dogs": 59.8e6,
    "cats": 42.2e6,
    "fish": 4.9e6,
    "reptiles": 2.3e6,
    "birds": 2.1e6,
    "small mammals": 1.3e6,
}

canvas = ansiplot.Scaled(40, 10)
for pos, (key, value) in enumerate(values.items()):
    canvas.bar(pos, value, title=key)
canvas.show()
