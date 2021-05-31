#!/usr/bin/env python3

#!/usr/bin/env python3

from manimlib import *
exec(get_custom_config()["universal_import_line"])
import numpy as np
from dice_utils import make_dice_face


class EquallyLikely(Scene):
    def construct(self):
        dice =[
            make_dice_face(i) for i in range(1, 7)
        ]
        hstack(dice)
        probs = [
            Tex(r"\frac 1 6")
        ]
        self.add(*dice)
