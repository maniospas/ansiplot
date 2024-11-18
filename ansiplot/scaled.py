from ansiplot.rect import Canvas
from ansiplot.rect import Rect


class Scaled(Canvas):
    """A variation of Rect canvas that automatically determines scaling limits."""
    def __init__(self,
        width: int,
        height: int,
        symbol_state: int = 0,
        palette=None,
        axis=True):
        super().__init__(palette=palette, symbol_state=symbol_state)
        self.width = width
        self.height = height
        self.axis = axis
        # lists to hold pending plots
        self._hbars = list()
        self._bars = list()
        self._scatters = list()
        self._plots = list()

    def _bar(self, x, y, symbol, ymin=0):
        self._bars.append((x, y, symbol, ymin))

    def _hbar(self, x, y, symbol, xmin=0):
        self._hbars.append((x, y, symbol, xmin))

    def _scatter(self, x, y, symbol):
        self._scatters.append((x, y, symbol))

    def _plot(self, x, y, symbol):
        self._plots.append((x, y, symbol))

    def _text(self):
        min_x = float("inf")
        max_x = float("-inf")
        min_y = float("inf")
        max_y = float("-inf")
        for x, y, _, xmin in self._hbars:
            if x is not None:
                min_x = min(x, min_x)
                min_x = min(xmin, min_x)
                max_x = max(x, max_x)
                max_x = max(xmin, max_x)
            min_y = min(y, min_y)
            max_y = max(y, max_y)
        for x, y, _, ymin in self._bars:
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            if y is not None:
                min_y = min(y, min_y)
                min_y = min(ymin, min_y)
                max_y = max(y, max_y)
                max_y = max(ymin, max_y)
        for x, y, _ in self._scatters:
            for x, y in zip(x, y):
                min_x = min(x, min_x)
                max_x = max(x, max_x)
                min_y = min(y, min_y)
                max_y = max(y, max_y)
        for x, y, _ in self._plots:
            for x, y in zip(x, y):
                min_x = min(x, min_x)
                max_x = max(x, max_x)
                min_y = min(y, min_y)
                max_y = max(y, max_y)

        rect = Rect(self.width,
                    self.height,
                    xlimits=(min_x, max_x),
                    ylimits=(min_y, max_y),
                    axis=self.axis,
                    palette=self.palette)

        for x, y, symbol in self._plots:
            rect.plot(x, y, symbol)
        for x, y, symbol in self._scatters:
            rect.scatter(x, y, symbol)

        for x, y, symbol, xmin in self._hbars:
            if x is None:
                xmin, x = min_x, max_x
            rect.hbar((xmin, x), y, symbol=symbol)
        for x, y, symbol, ymin in self._bars:
            if y is None:
                ymin, y = min_y, max_y
            rect.bar(x, (ymin, y), symbol=symbol)

        return rect.text(legend=False)
