def lag_features(series: list, lags: list) -> list:
    """
    Returns the lag feature matrix.
    """
    # Write code here
    max_lag = max(lags)
    return [[series[i-lag] for lag in lags] for i in range(max_lag , len(series))]
    pass