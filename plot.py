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

from plots import rose, shot_lengths_histogram


if __name__ == "__main__":

    parser = ArgumentParser(description="Create plots from a Therion sqlite database")
    parser.add_argument("input", help="Input sqlite database exported by Therion")
    parser.add_argument("-s", "--save", metavar="PATH", nargs=1,
            help="Save the plots into the given directory")
    parser.add_argument("-f", "--format", choices=["png", "jpg", "pdf", "svg"],
            default="png", help="File format of plots")
    subparsers = parser.add_subparsers(help="Available plots")

    parser_rose = subparsers.add_parser("rose", help="Create a rose diagram")
    parser_rose.add_argument("-b", "--bins", nargs=1, default=72, type=int,
            help="Number of bins")
    parser_rose.set_defaults(function=rose.plot)

    parser_shot_lengths_histogram = subparsers.add_parser("shot-lengths",
            help="Create a histogram of shot lengths")
    parser_shot_lengths_histogram.add_argument("-b", "--bins", nargs=1, default=100, type=int,
            help="Number of bins")
    parser_shot_lengths_histogram.add_argument("-l", "--log", action="store_true",
            help="Use log scale")
    parser_shot_lengths_histogram.set_defaults(function=shot_lengths_histogram.plot)

    args = parser.parse_args()

    conn = sqlite3.connect(args.input)

    args.function(args, conn)
