
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Hamukichi (Nombiri)"
__version__ = "0.1.0"
__date__ = "2015-03-09"
__licence__ = "MIT License"

import random
import browser


KUJI = {"大吉": 8, "中吉": 46, "小吉": 15, "吉": 15, "末吉": 8, "凶": 8}

KUJILIST = []
for k, v in KUJI.items():
    KUJILIST += [k] * v


def omikuji(ev):

    # Get the result
    result = random.choice(KUJILIST)

    # Output
    res_elt = browser.document["result"]
    res_elt.text = result


sub_elt = browser.document["submit_button"]
sub_elt.bind("click", omikuji)