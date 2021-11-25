"""Clustering-related mathematical functions.
"""

from typing import Optional

import numpy as np

import py4research.math.random as r


def kmeans(x: np.ndarray,
           n_clusters: Optional[int] = 1,
           max_iterations: Optional[int] = 100,
           tol: Optional[float] = 1e-4) -> np.ndarray:
    """Performs the K-Means clustering over the input data.

    Args:
        x: Input array with a shape equal to (n_samples, n_variables, n_dimensions).
        n_clusters: Number of clusters.
        max_iterations: Maximum number of clustering iterations.
        tol: Tolerance value to stop the clustering.

    Returns:
        (np.ndarray): Assigned cluster per input sample.

    """

    # Gathers the corresponding dimensions
    n_samples, n_variables, n_dimensions = x.shape[0], x.shape[1], x.shape[2]

    # Creates an array of centroids and labels
    centroids = np.zeros((n_clusters, n_variables, n_dimensions))
    labels = np.zeros(n_samples)

    for i in range(n_clusters):
        # Chooses a random sample to compose the centroid
        idx = r.generate_integer_random_number(0, n_samples)
        centroids[i] = x[idx]

    for _ in range(max_iterations):
        # Calculates the euclidean distance between samples and each centroid
        dists = np.squeeze(np.array([np.linalg.norm(x - c, axis=1) for c in centroids]))

        # Gathers the minimum distance as the cluster that conquers the sample
        updated_labels = np.squeeze(np.array(np.argmin(dists, axis=0)))

        # Calculates the difference ratio between old and new labels
        ratio = np.sum(labels != updated_labels) / n_samples

        if ratio <= tol:
            break

        # Updates the old labels with the new ones
        labels = updated_labels

        for i in range(n_clusters):
            # Gathers the samples that belongs to current centroid
            centroid_samples = x[labels == i]

            # If there are samples that belongs to the centroid
            if centroid_samples.shape[0] > 0:
                # Updates the centroid position
                centroids[i] = np.mean(centroid_samples, axis=0)

    return labels
