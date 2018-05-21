from PyQt4.QtCore import QDate, QDateTime, QTime
import sqlalchemy.types as types


class QDateType(types.TypeDecorator):
    impl = types.Date

    def process_bind_param(self, value, dialect):
        if value and isinstance(value, QDate):
            return value.toPyDate()

    def process_result_value(self, value, dialect):
        return QDate.fromString(value.isoformat(), 'yyyy-MM-dd')


class QDateTimeType(types.TypeDecorator):
    impl = types.DateTime

    def process_bind_param(self, value, dialect):
        if value and isinstance(value, QDateTime):
            return value.toPyDateTime()

    def process_result_value(self, value, dialect):
        if value:
            return QDateTime.fromString(value.isoformat(), 'yyyy-MM-ddTHH:mm:ss')
        else:
            return None


class QTimeType(types.TypeDecorator):
    impl = types.Time

    def process_bind_param(self, value, dialect):
        if value and isinstance(value, QTime):
            return value.toPyTime()

    def process_result_value(self, value, dialect):
        return QTime.fromString(value().isoformat(), 'HH:mm:ss')
