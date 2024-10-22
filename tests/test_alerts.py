import unittest
from alerts import check_alerts

class TestAlerts(unittest.TestCase):

    def test_alert_trigger(self):
        alert = check_alerts(36.0, 35.0)  # Example: current temp exceeds threshold
        self.assertTrue(alert)

    def test_no_alert_trigger(self):
        alert = check_alerts(30.0, 35.0)
        self.assertFalse(alert)

if __name__ == '__main__':
    unittest.main()
