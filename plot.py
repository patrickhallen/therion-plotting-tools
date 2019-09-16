# Copyright (c) 2019 Patrick Hallen

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from argparse import ArgumentParser
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as  plt


if __name__ == "__main__":

    parser = ArgumentParser("Plot rosen diagram from a Therion DB")
    parser.add_argument("input", help="Input sqlite database exported by Therion")
    args = parser.parse_args()

    conn = sqlite3.connect(args.input)
    df = pd.read_sql_query("select * from SHOT;", conn)

    bins = 72
    h, e = np.histogram(df["BEARING"] * np.pi/180., weights=df["LENGTH"], bins=bins)

    ax = plt.subplot(111, projection="polar")
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.bar(e[:-1], h, align="edge", width=e[1]-e[0])
    plt.show()
