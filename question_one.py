#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])

from dice_utils import make_dice_face
import numpy as np

class QuestionOne(Scene):
    def construct(self):
        #np.random.randi
        self.add(make_dice_face(1))
