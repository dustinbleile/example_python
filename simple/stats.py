# coding: utf-8
import numpy, pandas, scipy, pandas
import scipy.stats
np = numpy
x = numpy.random.uniform(10, size=(1000))
x
x.mean()
x.median()
np.percentile(x, 50)
np.percentile(x, 50, interpolation='nearest')
x.max()
x.mean()
x.min()
pandas.Series(x).quantile([0.01, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99])
x.percentile(x, 0.1)
scipy.stats.percentileofscore(x, 3.23)
scipy.stats.percentileofscore(x, 5)
scipy.stats.percentileofscore(x, 0)
scipy.stats.percentileofscore(x, 11)

np.std(x)
scipy.std(x)
scipy.stats.iqr(x)
