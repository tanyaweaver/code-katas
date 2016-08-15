def series_sum(n):
    """Return the sum of 1 + 1/4 + 1/7 +... series up to n-th term"""
    if isinstance(n, int) and n >= 0:
        if n == 0:
            sum_series = 0
        elif n == 1:
            sum_series = 1
        else:
            sum_series = 1
            x = 1
            for i in range(n - 1):
                x += 3
                sum_series += 1 / x
        return '{:.2f}'.format(sum_series)
    else:
        return u'the argument must be a positive whole number or 0'
