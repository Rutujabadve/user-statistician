#
# user-statistician: Github action for generating a user stats card
# 
# Copyright (c) 2021 Vincent A Cicirello
# https://www.cicirello.org/
#
# MIT License
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import json
import pprint

if __name__ == "__main__" :
    with open("default-widths.json", "r") as f :
        defaultWidths = json.load(f)
    with open("default-widths.py", "wb") as f :
        heading = """########################################
# The dict that follows is derived from
# default-widths.json from
# https://github.com/google/pybadges,
# which is licensed under Apache-2.0.
########################################
"""
        formatted = pprint.pformat(defaultWidths)
        formatted = formatted.replace(" " * 23, " " * 2)
        formatted = formatted.replace(" " * 19, " " * 2)
        s = heading + "\ndefaultWidths = " + formatted
        f.write(s.encode(encoding="UTF-8"))
