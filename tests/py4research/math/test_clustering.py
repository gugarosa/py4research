import numpy as np

from py4research.math import clustering


def test_kmeans():
    x = np.random.uniform(0, 1, (20, 2, 1))

    y = clustering.kmeans(x, n_clusters=3)

    assert y.shape[0] == 20
