from sqlalchemy.ext.declarative import declared_attr


class BaseMixin:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
