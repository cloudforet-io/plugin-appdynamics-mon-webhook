import logging
import unittest
import os
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.tester import TestCase, to_json

_LOGGER = logging.getLogger(__name__)
TEST_JSON = os.environ.get("test_json", None)


class TestEvent(TestCase):
    def test_alert_full_sample(self):
        data = {
            "event_name": "New Critical Health Rule Violation",
            "event_guid": "a35260de-34ff-476f-bcb9-c44fd1afd913",
            "event_id": "33021165",
            "policy": "JAVA alert",
            "event_time": "Mon Apr 03 02:04:55 UTC 2023",
            "app_id": "108979",
            "app_name": "MyApp",
            "event_message": "AppDynamics has detected a problexm .....",
            "severity": "ERROR",
            "event_deep_link": "https://painted20230307xxxx.saas.appdynamics.com/#location=APP_EVENT_Vxxxx",
            "controller_url": "https://painted20230307xxxxx.saas.appdynamics.com",
            "node_id": "${latestEvent.node.id}",
            "node_name": "${latestEvent.node.name}",
            "summary": "AppDynamics has detected a problem with Business xxxxxx.",
            "event_type": "POLICY_OPEN_CRITICAL",
            "tier_id": "201066",
            "tier_name": "MyTier",
            "health_rule_id": "615178",
            "health_rule_name": "Business Transaction Health",
            "incident_id": "70646",
            "incident_name": "Business Transaction Health",
        }
        parsed_data = self.monitoring.Event.parse({"options": {}, "data": data})
        results = to_json(parsed_data)
        for result in results["results"]:
            self.assertEqual(result["event_type"], "ALERT")
            print(result)


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
