from read_OEIS import features
import matplotlib.pyplot as plt
import numpy as np

plt.clf()
plt.hist(features["val_0mod2"], 100)
plt.title("Pairty Histogram")
plt.xlabel("mean(A_n % 2)")
plt.ylabel("Number of Sequences")
plt.savefig("figs/0mod2.png")

plt.clf()
s = features["diff1_val_0mod2"]
plt.hist(s[~np.isnan(s)], 100)
plt.title("Diff1 Pairty Histogram")
plt.xlabel("mean((A_{n+1} - A_n) % 2)")
plt.ylabel("Number of Sequences")
plt.savefig("figs/diff1_0mod2.png")

plt.clf()
s = features["log_log_ols_slope"]
plt.hist(s[~np.isnan(s)], 100)
plt.title("Log-Log Slope Histogram")
plt.xlabel("Log-Log slope")
plt.ylabel("Number of Sequences")
plt.savefig("figs/log_log_slope.png")

