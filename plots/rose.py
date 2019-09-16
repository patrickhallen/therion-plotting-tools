import numpy as np
import pandas as pd
import matplotlib.pyplot as  plt
from os import path

def plot(args, conn):
    df = pd.read_sql_query("select * from SHOT;", conn)

    h, e = np.histogram(df["BEARING"] * np.pi/180., weights=df["LENGTH"], bins=args.bins)

    ax = plt.subplot(111, projection="polar")
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.bar(e[:-1], h, align="edge", width=e[1]-e[0])
    if args.save:
        plt.savefig(path.join(args.save, "rose_diagram." + args.format))
    else:
        plt.show()
