import unittest

from china_bills import filter_china_bills


class ChinaBillsFilterTests(unittest.TestCase):
    def test_filters_to_title_match_and_congress_range(self):
        bills = [
            {
                "congress": 118,
                "bill_type": "hr",
                "bill_number": "1",
                "title": "A bill to strengthen trade with China",
                "summary": "No mention needed here",
            },
            {
                "congress": 118,
                "bill_type": "hr",
                "bill_number": "2",
                "title": "A bill to strengthen trade",
                "summary": "This summary mentions China but title does not",
            },
            {
                "congress": 106,
                "bill_type": "hr",
                "bill_number": "3",
                "title": "China policy update",
            },
        ]

        result = filter_china_bills(bills)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["bill_number"], "1")
        self.assertEqual(result[0]["label"], "China")

    def test_word_boundary_is_enforced(self):
        bills = [
            {"congress": 118, "title": "Support Chinatown small businesses"},
            {"congress": 118, "title": "Support China policy changes"},
        ]

        result = filter_china_bills(bills)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Support China policy changes")


if __name__ == "__main__":
    unittest.main()
