#!/usr/bin/env python3
from manimlib import *

exec(get_custom_config()["universal_import_line"])

class QuestionOne(Scene):
    def construct(self):
        self.add(Tex("Q1"))
