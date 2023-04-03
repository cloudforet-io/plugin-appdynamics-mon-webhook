from datetime import datetime

"""
Sample data
{
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
    "controller_url": "https://painted202303071552476.saas.appdynamics.com",
    "node_id": "${latestEvent.node.id}",
    "node_name": "${latestEvent.node.name}",
    "summary": "AppDynamics has detected a problem with Business xxxxxx.",
    "event_type": "POLICY_OPEN_CRITICAL",
    "tier_id": "201066",
    "tier_name": "MyTier",
    "health_rule_id": "615178",
    "health_rule_name": "Business Transaction Health",
    "incident_id": "70646",
    "incident_name": "Business Transaction Health"
    }
"""


class Alert:
    def __init__(self, *args, **kwargs):
        self.event_dict = {"event_type": "ALERT"}
        self.alert = args[0]
        self._update()
        self._update_severity()
        self.event_dict["additional_info"] = self._update_additional()
        self.event_dict["occurred_at"] = self._update_ocurred_at()

    def _update(self):
        map_keys = {
            "event_name": "title",
            "summary": "description",
            "policy": "rule",
            "event_id": "event_key",
        }
        for k, v in map_keys.items():
            item = self.alert.get(k, None)
            if item:
                self.event_dict[v] = item
            else:
                print(f"Fail to get key: {k}")
        # if helath_rule exist
        if "incident_id" in self.alert:
            self.event_dict["event_key"] = self.alert.get("incident_id")

    def _update_severity(self):
        severity = self.alert.get("severity", "INFO")
        if severity == "WARN":
            severity = "WARNING"
        self.event_dict["severity"] = severity

    def _update_additional(self):
        additional = {}
        map_keys = {"event_deep_link": "url", "app_name": "application"}

        for k, v in map_keys.items():
            item = self.alert.get(k, None)
            if item:
                additional[v] = item
            else:
                print(f"Fail to get key: {k}")
        return additional

    def _update_ocurred_at(self):
        date_string = self.alert.get("event_time", None)
        if date_string is None:
            datetimeobj = datetime.utcnow()
        else:
            format_string = "%a %b %d %H:%M:%S %Z %Y"
            datetimeobj = datetime.strptime(date_string, format_string)
        return datetimeobj

    def get_event_dict(self):
        return self.event_dict
