import ansiplot

values = {"dogs": 59.8E6, "cats": 42.2E6, "fish": 4.9E6,
          "reptiles": 2.3E6, "birds": 2.1E6, "small mammals": 1.3E6}

canvas = ansiplot.Scaled(40, 10)
for pos, (key, value) in enumerate(values.items()):
    canvas.bar(pos, value, title=key)
canvas.show()