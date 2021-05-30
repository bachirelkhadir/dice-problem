#!/usr/bin/env python3

#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])
import numpy as np
from dice_utils import make_dice_face
from common import vstack, hstack, halign


class LawLargeNumbers(Scene):
    def construct(self):
        X = Tex("X")
        X.shift(UP)
        self.add(X)

        Xis = [Tex(rf"X_{i}" for i in [1, 2, 3, 4, "..."])]
        hstack(Xis)
        self.add(*Xis)
