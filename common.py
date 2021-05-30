#!/usr/bin/env python3

from manimlib import *

def vstack(objs, buff=LARGE_BUFF):
    for t1, t2 in zip(objs, objs[1:]):
        t2.next_to(t1, DOWN, buff)
    return objs

def hstack(objs, buff=LARGE_BUFF):
    for t1, t2 in zip(objs, objs[1:]):
        t2.next_to(t1, RIGHT, buff)
    return objs

def halign(objs):
    for t in objs[1:]:
        t.align_to(objs[0])
    return objs


def hstack_fixed_width(obj, width, buff):
    vstack(obj[::width], buff)

    for i in range(len(obj) // width):
        hstack(obj[i*width:(i+1)*width], buff)

    hstack(obj[(i+1)*width:], buff)
