import numpy as np

def cross_ratio(z1, z2, z3, z4):
    """
    Cross ratio (z1,z2;z3,z4) = (z1-z3)*(z2-z4) / ((z1-z4)*(z2-z3))
    """
    return ((z1 - z3) * (z2 - z4)) / ((z1 - z4) * (z2 - z3))

def algebraic_geometry_scores(returns):
    """
    For each ETF, compute a Möbius‑invariant cross‑ratio using three reference points:
    - Reference 1: last day's return of the universe median (or mean)
    - Reference 2: minimum return over the window
    - Reference 3: maximum return over the window
    Then score = |log(cross_ratio)| (positive, varying)
    """
    returns_clean = returns.dropna()
    if returns_clean.shape[1] < 4:
        # Not enough assets to define a meaningful cross‑ratio
        return {t: 0.0 for t in returns_clean.columns}

    # Use the last day's return for each ETF
    last_returns = returns_clean.iloc[-1].values   # shape (n,)
    # Reference points (scalars) derived from the cross‑section of last returns
    ref1 = np.median(last_returns)        # median
    ref2 = np.min(last_returns)           # minimum
    ref3 = np.max(last_returns)           # maximum

    scores = {}
    tickers = returns_clean.columns
    for i, ticker in enumerate(tickers):
        z = last_returns[i]
        # Avoid division by zero or identical points
        if abs(z - ref1) < 1e-12 or abs(z - ref2) < 1e-12 or abs(z - ref3) < 1e-12:
            scores[ticker] = 0.0
        else:
            cr = cross_ratio(z, ref1, ref2, ref3)
            scores[ticker] = abs(np.log(abs(cr) + 1e-12))
    return scores
