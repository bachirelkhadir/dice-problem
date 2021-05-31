#!/usr/bin/env python3

#!/usr/bin/env python3

from manimlib import *
exec(get_custom_config()["universal_import_line"])
import numpy as np
from dice_utils import make_dice_face
from common import vstack, hstack, halign

class EquallyLikely(Scene):
    def construct(self):
        dice =[
            make_dice_face(i) for i in range(1, 7)
        ]
        hstack(dice)
        probs = [
            Tex(r"\frac 1 6").next_to(d, UP)
            for d in dice
        ]
        self.add(*dice)
        self.add(*probs)
