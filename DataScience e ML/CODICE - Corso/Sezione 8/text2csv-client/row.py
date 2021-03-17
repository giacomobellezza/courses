#!/usr/bin/env python3


fields = ["review", "sentiment"]


def packer(review, sentiment):
    return {"review": review, "sentiment": sentiment}


def output(filepath):
    return open(filepath, "w", encoding='utf8', newline='')
