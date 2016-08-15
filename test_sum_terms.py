INVALID_INPUT = u'the argument must be a positive whole number or 0'
Test.assert_equals(series_sum(0), "0.00")
Test.assert_equals(series_sum(1), "1.00")
Test.assert_equals(series_sum(2), "1.25")
Test.assert_equals(series_sum(3), "1.39")
Test.assert_equals(series_sum(-1), INVALID_INPUT)
Test.assert_equals(series_sum(1.5), INVALID_INPUT)
Test.assert_equals(series_sum('abc'), INVALID_INPUT)