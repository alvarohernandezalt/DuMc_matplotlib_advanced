import matplotlib

matplotlib.use("nbagg")
# %matplotlib inline

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
import pandas as pd

# A sample with seaborn palettes. We'll covered some aspects later in this set of notebooks
sns.set_palette("BuPu_d", desat=0.6)
sns.set_context("notebook", font_scale=2.0)

# generate random data
np.random.seed(42424242)

x = stats.gamma(5).rvs(420)
y = stats.gamma(13).rvs(420)

with sns.axes_style("white"):
    sns.jointplot(x, y, kind="hex", size=16)

plt.style.use(
    "/content/drive/MyDrive/Colab Notebooks/06_PyVisualization/01_MatPlotLib/01_DuMc_MAsPLT/git/preview/styles/custom.mplstyle"
)
data = pd.scatter_matrix(baseball.loc[:, "r":"sb"], figsize=(10, 16))
