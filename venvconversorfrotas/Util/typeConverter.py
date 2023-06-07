from datetime import datetime, date

class TypeConverter:

    def to_string(self, value):
        return str(value)

    def to_integer(self, value):
        if value == '':
            return None
        return int(value)

    def to_float(self, value):
        if value == '':
            return None
        return float(value)

    def to_bool(self, value):
        return bool(value)

    def string_to_datetime(self, string_date_time, format='%Y-%m-%d %H:%M:%S'):
        if string_date_time == '':
            return None
        return datetime.strptime(string_date_time, format)

    def string_to_date(self, string_date, format='%d/%m/%Y'):
        if string_date == '':
            return None
        return datetime.strptime(string_date, format).date()

    def datetime_to_string(self, datetime_data, format='%Y-%m-%d %H:%M:%S'):
        return datetime_data.strftime(format)

    def datetime_to_date(self, datetime_data):
        return datetime_data.date()

    def date_to_datetime(self, date, hora=0, minuto=0, segundo=0):
        return datetime.combine(date, datetime.time(hour=hora, minute=minuto, second=segundo))
