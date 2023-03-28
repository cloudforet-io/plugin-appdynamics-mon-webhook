import logging
from spaceone.core.manager import BaseManager
from spaceone.monitoring.manager.alert import Alert

from spaceone.monitoring.model.event_response_model import EventModel
from spaceone.monitoring.error.event import ERROR_CHECK_VALIDITY

_LOGGER = logging.getLogger(__name__)
_EXCEPTION_TO_PASS = ["Test notification"]


class EventManager(BaseManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def parse(self, raw_data):
        results = []
        events = raw_data.get("events", [])
        for event in events:
            inst = Alert(event)
            event_dict = inst.get_event_dict()
            event_vo = self._check_validity(event_dict)
            results.append(event_vo)
        _LOGGER.debug(f"[EventManager] parse Event : {event_dict}")

        return results

    @staticmethod
    def _check_validity(event_dict):
        try:
            event_result_model = EventModel(event_dict, strict=False)
            event_result_model.validate()
            event_result_model_primitive = event_result_model.to_native()
            return event_result_model_primitive

        except Exception as e:
            raise ERROR_CHECK_VALIDITY(field=e)
