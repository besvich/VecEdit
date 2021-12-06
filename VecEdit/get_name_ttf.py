#!/usr/bin/env python

import os
from contextlib import redirect_stderr
from fontTools import ttLib


def font_name(font_path):
    font = ttLib.TTFont(font_path, ignoreDecompileErrors=True)
    with redirect_stderr(None):
        names = font['name'].names

    details = {}
    for x in names:
        if x.langID == 0 or x.langID == 1033:
            try:
                details[x.nameID] = x.toUnicode()
            except UnicodeDecodeError:
                details[x.nameID] = x.string.decode(errors='ignore')

    return {'name': details[4], 'family': details[1], 'style': details[2]}

if __name__ == "__main__":
    print(font_name('myfont.ttf'))  # ('Century Bold Italic', 'Century', 'Bold Italic') – name, family, style
