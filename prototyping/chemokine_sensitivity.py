# It is clear that T cells do not all share a common "sensitivity" threshold
# attractant concentration value at which they perform chemotaxisself.
# Here we investigate distributions of sensitivities, from which each cell
# samples to obtain a bespoke sensitivit.
#
# Mark N. Read, 2018
import numpy as np
import scipy.stats as ss
import matplotlib
matplotlib.rcParams['figure.autolayout'] = True
import matplotlib.pyplot as plt

def logistic_distribution(x, k, x0):
    """
    x = numpy array of x values to apply function to.
    k = scale factor
    x0 = median value of distribution

    This has all manner of issues. Firstly, it permits values of <0, which corresponds to cells that are sensitive to
    the most miniscule level of chemokine (actually sensitive to zero). Second, it has no upper bound. Third, I have
    no idea why I ever thought this was a good choice!
    """
    print(x)
    print(x + x0)
    print(np.exp(x + x0))
    return 1. / (1. + np.exp(-k * (x + x0)))


def scaled_beta(x, a, b):
    """
    smallest possible value is zero, maximum is 1, which can be scaled to the cell attractant secretion rate, which
    is the highest concentration possible. Much flexibility over shape of distribution.
    """
    return ss.beta.cdf(x, a=a, b=b)


# 40k is roughly rate of secretion.
# Investigating more than this doesn't make sense; it's the highest
# concentration likely to be encountered.
# x = np.arange(0, 40000, step=5)
# log_distro = logistic_distribution(x, 1e-1, 1e-1)

x = np.arange(0, 1, step=0.001)

distro = scaled_beta(x, 5, 10)

plt.clf()
plt.plot(x, distro)
plt.show()
plt.savefig('chemokine_sensitivity_threshold_distribution.png', dpi=600)
