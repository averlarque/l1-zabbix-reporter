from pyzabbix import ZabbixAPI
from datetime import datetime


def generator(items):
    for i in items:
        yield i


# noinspection PyTypeChecker
class ZabbixApi:
    def __init__(self, url, user, password):
        self.zabbix = ZabbixAPI(url, user=user, password=password)

    @staticmethod
    def datetime_to_unix_time(dt):
        epoch = datetime.utcfromtimestamp(0)
        return str(int((dt - epoch).total_seconds()))

    @staticmethod
    def unix_time_to_datetime(ut):
        return datetime.fromtimestamp(float(ut))

    @staticmethod
    def convert_time(dt, tz=3):
        """
		Zabbix API принимает данные текущего времени как UTC, однако возвращает данные
		в UTC +3 (по времени, установленного на сервере) и 3 часа теряются.
		Этим методом мы отнимаем 3 часа и получаем якобы указанный результат.
		"""
        dt_hour = dt.hour
        if dt_hour < 3:
            tz_time = dt.replace(day=dt.day - 1, hour=(dt_hour - tz) + 24)
        else:
            tz_time = dt.replace(hour=dt_hour - tz)
        return tz_time

    def get_events_by_time(self, time_from, time_till=datetime.now()):
        converted_unix_time_from = self.datetime_to_unix_time(self.convert_time(time_from))
        converted_unix_time_till = self.datetime_to_unix_time(self.convert_time(time_till))
        result = self.zabbix.do_request('event.get', {'output': 'extend', 'source': 0, 'value': 1,
                                                      'time_from': converted_unix_time_from,
                                                      'time_till': converted_unix_time_till})
        return result

    def get_alert_by_event(self, eventid):
        result = self.zabbix.do_request('alert.get', {'output': 'extend', 'eventids': eventid, 'limit': 1})
        return result
