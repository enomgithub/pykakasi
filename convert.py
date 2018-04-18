#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from pykakasi import kakasi
try:
    import simplejson as json
except ImportError:
    import json


def main():
    kks = kakasi()
    kks.setMode("J", "a")
    conv = kks.getConverter()

    input_file = open("myouji.json", "r", encoding="utf-8")
    input_data = json.load(input_file)

    ls = []
    for s in input_data:
        ls.append(conv.do(s))

    output_data = json.dumps(ls, indent=2)
    output_file = open("myouji_rome.json", "w", encoding="utf-8")
    output_file.write(output_data)

    input_file.close()
    output_file.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())