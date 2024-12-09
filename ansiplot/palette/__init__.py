from ansiplot.palette.pretty import Pretty
from ansiplot.palette.colorless import Colorless
from ansiplot.palette.monochrome import Monochrome
from ansiplot.palette.deuteranopia import DeuteranopiaFriendly
from ansiplot.palette.protanopia import ProtanopiaFriendly
from ansiplot.palette.tritanopia import TritanopiaFriendly


def info():
    print("The following palettes are available:")
    # in the following list, it is important to have colorless be first
    for palette in [
        Colorless,
        Pretty,
        Monochrome,
        ProtanopiaFriendly,
        DeuteranopiaFriendly,
        TritanopiaFriendly,
    ]:
        ret = Pretty.reset_color + palette.__name__.ljust(20)
        for color in palette.colors:
            ret += f" {color}■"
        print(ret)
    print(Pretty.reset_color + " ")
