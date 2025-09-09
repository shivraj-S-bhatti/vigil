import numpy as np

def zscore_anomalies(series, thresh=3.0, window=200):
    x = np.asarray(series, dtype=float)
    if len(x) < 5: return []
    mu = np.convolve(x, np.ones(window)/window, mode='same')
    sigma = np.sqrt(np.convolve((x-mu)**2, np.ones(window)/window, mode='same')) + 1e-6
    z = (x-mu)/sigma
    return np.where(np.abs(z) >= thresh)[0].tolist()
