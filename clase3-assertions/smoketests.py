from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from assertions import AssertionsTest
from searchtests import SearchTests

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)


smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
    "output": "reports/smoke-report",
    "report_name": "smoke-report",
    "combine_reports": True,
    "add_timestamp": True
    }

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)

