import time
import os
# from IPython.display import clear_output # the corresponding to os.system('cls') on IPyhotn IDE
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import click
import sys

def clear():
    print("\n"*50)

def run_experiment(q1_of_y0, q1_of_y1, s=1, trails=100):
    results = pd.DataFrame(None, columns=["y", "r"])
    for t in range(trails):
        y = None  # initialization
        # print("im here y=", y)
        while not y in {"0", "1"}:
            y = input("Please Enter 0 or 1\n")

        q = q1_of_y0 if y == "0" else q1_of_y1  # parameter of corresponding Ber dist
        r = np.random.binomial(n=1, p=q)  # reward

        results.loc[t, "y"], results.loc[t, "r"] = y, r

        # choose what announcement to print
        print("reward: ", r)
        time.sleep(s)
        clear()

    return results

q0 = 0.4
q1 = 0.6
res = run_experiment(q1_of_y0=q0, q1_of_y1=q1)
res.to_csv(r"C:\Users\yuvfr\OneDrive\שולחן העבודה\results_Aba.csv")