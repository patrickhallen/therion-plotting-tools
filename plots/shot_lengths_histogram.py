import numpy as np
import pandas as pd
import matplotlib.pyplot as  plt
from os import path

def plot(args, conn):
    df = pd.read_sql_query("select * from SHOT;", conn)

    plt.hist(df["LENGTH"], bins=args.bins)
    plt.xlabel("Shot length / m")
    plt.ylabel("Count")
    if args.log:
        plt.yscale("log")

    if args.save:
        plt.savefig(path.join(args.save, "shot_lengths_histogram." + args.format))
    else:
        plt.show()
