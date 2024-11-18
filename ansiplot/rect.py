from ansiplot.canvas import Canvas


def normalize(value, min_val, max_val, scale):
    if max_val == min_val:
        return scale // 2
    return int((value - min_val) / (max_val - min_val) * (scale - 1))


class Rect(Canvas):
    def __init__(
        self,
        width: int,
        height: int,
        xlimits: tuple[float, float] = (0, 1),
        ylimits: tuple[float, float] = (0, 1),
        symbol_state: int = 0,
        palette=None,
        axis=True,
    ):
        super().__init__(symbol_state=symbol_state, palette=palette)
        self._grid = [[" " for _ in range(width)] for _ in range(height)]
        self.legend = ""
        self._xlimits = xlimits
        self._ylimits = ylimits
        if not axis:
            return
        for x in range(width):
            self._grid[height - 1][x] = self.palette.reset_color + self.palette.xaxis
        for y in range(height):
            self._grid[y][0] = self.palette.reset_color + self.palette.yaxis

    def _bar(self, x: float, y: float, symbol: str, ymin: float = 0):
        min_x, max_x = self._xlimits
        min_y, max_y = self._ylimits
        height = len(self._grid)
        width = len(self._grid[0])
        if y is None:
            ymin, y = self._ylimits

        grid_x = normalize(x, min_x, max_x, width)
        grid_ymax = height - 1 - normalize(y, min_y, max_y, height)
        grid_ymin = height - 1 - normalize(ymin, min_y, max_y, height)

        if grid_x < 0 or grid_x >= width:
            raise Exception(
                f"Value {x} lies outside the x-axis range [{min_x}, {max_x}] of this Rext canvas"
            )
        if grid_ymax < 0 or grid_ymax >= height:
            raise Exception(
                f"Value {y} lies outside the y-axis range [{min_y}, {max_y}] of this Rext canvas"
            )
        if grid_ymin < 0 or grid_ymin >= height:
            raise Exception(
                f"Value {ymin} lies outside the y-axis range [{min_y}, {max_y}] of this Rext canvas"
            )

        for grid_y in range(
            grid_ymax, grid_ymin + 1
        ):  # inverse order due to substraction from height
            self._grid[grid_y][grid_x] = symbol

    def _hbar(self, x: float, y: float, symbol: str, xmin: float = 0):
        min_x, max_x = self._xlimits
        min_y, max_y = self._ylimits
        height = len(self._grid)
        width = len(self._grid[0])
        if x is None:
            xmin, x = self._xlimits

        grid_y = normalize(y, min_y, max_y, height)
        grid_xmax = normalize(x, min_x, max_x, width)
        grid_xmin = normalize(xmin, min_x, max_x, width)

        if grid_xmax < 0 or grid_xmax >= width:
            raise Exception(
                f"Value {x} lies outside the x-axis range [{min_x}, {max_x}] of this Rext canvas"
            )
        if grid_xmin < 0 or grid_xmax >= width:
            raise Exception(
                f"Value {xmin} lies outside the x-axis range [{min_x}, {max_x}] of this Rext canvas"
            )
        if grid_y < 0 or grid_y >= height:
            raise Exception(
                f"Value {y} lies outside the y-axis range [{min_y}, {max_y}] of this Rext canvas"
            )

        for grid_x in range(grid_xmin, grid_xmax + 1):
            self._grid[grid_y][grid_x] = symbol

    def _scatter(self, x: list[float], y: list[float], symbol: str):
        self._plot(x, y, symbol=symbol, continuous=False)

    def _plot(
        self, x: list[float], y: list[float], symbol: str, continuous: bool = True
    ):
        # retrieve width and height from the grid
        height = len(self._grid)
        width = len(self._grid[0])
        if len(x) != len(y):
            raise ValueError("x_coords and y_coords must have the same length.")

        min_x, max_x = self._xlimits
        min_y, max_y = self._ylimits

        # Place points on the grid
        prev = None
        for x, y in zip(x, y):
            grid_x = normalize(x, min_x, max_x, width)
            grid_y = height - 1 - normalize(y, min_y, max_y, height)
            if grid_x < 0 or grid_x >= width:
                raise Exception(
                    f"Value {x} lies outside the x-axis range [{min_x}, {max_x}] of this Rect canvas"
                )
            if grid_y < 0 or grid_y >= height:
                raise Exception(
                    f"Value {y} lies outside the y-axis range [{min_y}, {max_y}] of this Rect canvas"
                )
            # interpolate
            if prev is not None:
                grid_x_to, grid_y_to = grid_x, grid_y
                grid_x_from, grid_y_from = prev
                dx = abs(grid_x_to - grid_x_from)
                dy = abs(grid_y_to - grid_y_from)
                sx = 1 if grid_x_from < grid_x_to else -1
                sy = 1 if grid_y_from < grid_y_to else -1
                err = dx - dy

                x, y = grid_x_from, grid_y_from
                while True:
                    # Set the symbol at each interpolated point
                    if (
                        x == 0
                        or self._grid[y][x - 1] != symbol
                        or self._grid[y][x]
                        in [
                            " ",
                            self.palette.reset_color + self.palette.xaxis,
                            self.palette.reset_color + self.palette.yaxis,
                        ]
                    ):
                        self._grid[y][x] = symbol
                    if (x, y) == (grid_x_to, grid_y_to):
                        break
                    e2 = 2 * err
                    if e2 > -dy:
                        err -= dy
                        x += sx
                    elif e2 < dx:
                        err += dx
                        y += sy
            # add the symbol while taking care to not over-clutter by placing it on top of others
            if (
                x > 0
                and self._grid[grid_y][grid_x - 1] == symbol
                and self._grid[grid_y][grid_x]
                not in [
                    " ",
                    self.palette.reset_color + self.palette.xaxis,
                    self.palette.reset_color + self.palette.yaxis,
                ]
            ):
                continue
            self._grid[grid_y][grid_x] = symbol
            # if we're plotting a continuous curve (not a scatter plot) then remember this point to connect to
            if continuous:
                prev = (grid_x, grid_y)

    def _text(self):
        """Concert to a string."""
        min_x, max_x = self._xlimits
        min_y, max_y = self._ylimits
        plot = f"({min_x}, {max_y})\n"
        plot += f"\n{self.palette.reset_color}".join("".join(row) for row in self._grid)
        plot += (
            self.palette.reset_color
            + "\n"
            + f"({max_x}, {min_y})".rjust(len(self._grid[0]))
        )
        return plot
