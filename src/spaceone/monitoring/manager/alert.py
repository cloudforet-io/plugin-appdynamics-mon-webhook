import time
from datetime import datetime

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
            "displayName": "title",
            "eventMessage": "summary",
            "event_tier_name": "rule",
            "guid": "event_key"
        }
        for k, v in map_keys.items():
            item = self.alert.get(k, None)
            if item:
                self.event_dict[v] = item
            else:
                print(f"Fail to get key: {k}")

    def _update_severity(self):
        severity = self.alert.get("severity","INFO")
        if severity == "WARN":
            severity = "WARNING"
        self.event_dict["severity"] = severity

    def _update_additional(self):
        additional = {}
        map_keys = {
            "deepLink": "url"
        }

        for k, v in map_keys.items():
            item = self.alert.get(k, None)
            if item:
                additional[v] = item
            else:
                print(f"Fail to get key: {k}")
        return additional

    def _update_ocurred_at(self):
        date_string = self.alert.get("eventTime", None)
        if date_string == None:
            datetimeobj = datetime.utcnow()
        else:
            format_string = "%a %b %d %H:%M:%S %Z %Y"
            datetimeobj = datetime.strptime(date_string, format_string)
        return datetimeobj

    def get_event_dict(self):
        return self.event_dict


