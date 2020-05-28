import sys
import datetime
from zang.helpers.helpers import to_python
from enum import Enum

if sys.version_info > (3, 0):
    str = (str, bytes)


class BaseResource(object):

    _strs = []
    _ints = []
    _reals = []
    _dates = []
    _bools = []
    _dicts = []
    _map = {}
    _arrays = {}
    _enums = {}

    def __init__(self):
        self._bootstrap()
        super(BaseResource, self).__init__()

    def __str__(self):
        s = ''
        varNames = self._sortedVarsNames()
        for varName in varNames:
            value = vars(self)[varName]
            if value is not None:
                valueStr = self._valueString(value)
                s += varName[1:] + ': ' + valueStr + '\n'
        return s

    def _sortedVarsNames(self):
        """Return sorted self variable names"""
        keys = list(vars(self).keys())
        if sys.version_info >= (3, 0):
            keys = sorted(keys)
        else:
            keys.sort()
        return keys

    def _valueString(self, value):
        """If the value is not a primitive type, indent it's content"""
        valueStr = str(value)
        if not isinstance(
                value,
                (int, float, bool, str, datetime.datetime, Enum)):
            valueStr = '\n\t' + valueStr.replace('\n', '\n\t')
            if valueStr.count('\n') > 1:  # remove last \n\t
                valueStr = valueStr[:-2]
        return valueStr

    def _bootstrap(self):
        """Bootstraps the model object based on configured values."""
        for attr in self._keys():
            privateName = '_' + attr
            setattr(self, privateName, None)

    def _keys(self):
        return self._strs + self._ints + self._dates + self._bools + \
            list(self._map.keys()) + list(self._arrays.keys())

    @classmethod
    def new_from_dict(cls, d, **kwargs):

        d = to_python(
            obj=cls(),
            in_dict=d,
            str_keys=cls._strs,
            int_keys=cls._ints,
            real_keys=cls._reals,
            date_keys=cls._dates,
            bool_keys=cls._bools,
            dict_keys=cls._dicts,
            object_map=cls._map,
            array_map=cls._arrays,
            enums=cls._enums,
        )

        d.__dict__.update(kwargs)

        return d
