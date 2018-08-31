#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sqrt(num, threshold):
    y = 0
    while y ** 2 < num - threshold:
        y = y + threshold
    return y

print(sqrt(10, 1))
