class ModelMixin:
    def to_dict(self):
        data = {}
        for field in self._meta.fields:
            k = field.name 
            v = self.__dict__[k]
            data[k] = v
        return data
        