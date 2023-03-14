import logging
import unittest
import os
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.tester import TestCase, print_json, to_json

_LOGGER = logging.getLogger(__name__)
TEST_JSON = os.environ.get('test_json', None)


class TestEvent(TestCase):

    def test_alert_full_sample(self):
        data = {
            "account_name": "MY_APPD_SAAS",
            "policy_name": "JAVA alert",
            "events": [
                {
                    "guid": "aaaaaaaa",
                    "severity": "ERROR",
                    "displayName": "Ongoing Critical Health Rule Violation",
                    "eventMessage": "AppDynamics has detected a problem with Business Transaction <b>/</b>.<br><b>Business Transaction Health</b> continues to violate with <b>critical</b>.<br>All of the following conditions were found to be violating<br>For Application <b>MyApp</b>:<br>1) Calls per Minute Condition<br><b>Calls per Minute's</b> value <b>89072.00</b> was <b>greater than</b> the threshold <b>50.00</b> for the last <b>2</b> minutes.<br>",
                    "event_tier_name": "MyTier",
                    "eventTime": "Mon Mar 13 08:57:55 UTC 2023",
                    "deepLink": "https://MY_APPD_SAAS.saas.appdynamics.com/#location=APP_EVENT_VIEWER_MODAL&eventSummary=31062509&application=108979",
                },
                {
                    "guid": "bbbbbbbbbb",
                    "severity": "WARN",
                    "displayName": "Ongoing Critical Health Rule Violation",
                    "eventMessage": "AppDynamics has detected a problem with Business Transaction <b>/manager/WEB-INF</b>.<br><b>Business Transaction Health</b> continues to violate with <b>critical</b>.<br>All of the following conditions were found to be violating<br>For Application <b>MyApp</b>:<br>1) Calls per Minute Condition<br><b>Calls per Minute's</b> value <b>89070.00</b> was <b>greater than</b> the threshold <b>50.00</b> for the last <b>2</b> minutes.<br>",
                    "event_tier_name": "MyTier",
                    "eventTime": "Mon Mar 13 08:57:55 UTC 2023",
                    "deepLink": "https://MY_APPD_SAAS.saas.appdynamics.com/#location=APP_EVENT_VIEWER_MODAL&eventSummary=31062508&application=108979",
                }],
            "topSeverity": "ERROR",
            "controllerUrl": "https://MY_APPD_SAAS.saas.appdynamics.com",
            "action_name": "spaceone-dev-test",
        }
        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': data})
        results = to_json(parsed_data)
        for result in results['results']:
            print(result)
            self.assertEqual(result['event_type'],'ALERT')


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
