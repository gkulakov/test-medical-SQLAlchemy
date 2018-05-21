
from PyQt4.QtCore import Qt
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from . import tables
from contextlib import contextmanager


class DataAccessLayer:

    def __init__(self):
        self.engine = None
        self.Session = None

    def connect(self):
        self.engine = create_engine('mysql+mysqlconnector://mis:pass@localhost/database?charset=utf8')
        self.Session = sessionmaker(bind=self.engine)

    @contextmanager
    def session_context(self):
        """Provide a transactional scope around a series of operations."""
        session = self.Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

dal = DataAccessLayer()