# -*- coding: utf-8 -*-

"""
zang.helpers
~~~~~~~~~~~~~~
This module contians the helpers.
"""

import sys
from enum import Enum
from datetime import datetime, date
from dateutil.parser import parse as parse_datetime
from zang.exceptions.zang_exception import ZangException

if sys.version_info > (3, 0):
    str_classes = (str, bytes)


def is_collection(obj):
    """Tests if an object is a collection."""

    col = getattr(obj, '__getitem__', False)
    val = False if (not col) else True

    if isinstance(obj, str):
        val = False

    return val


# from kennethreitz/python-github3
def to_python(
        obj,
        in_dict,
        str_keys=None,
        date_keys=None,
        int_keys=None,
        real_keys=None,
        object_map=None,
        array_map=None,
        bool_keys=None,
        dict_keys=None,
        enums=None,
        **kwargs):
    """Extends a given object for API Consumption.
    :param obj: Object to extend.
    :param in_dict: Dict to extract data from.
    :param string_keys: List of in_dict keys that will be extracted as strings.
    :param date_keys: List of in_dict keys that will be extrad as datetimes.
    :param object_map: Dict of {key, obj} map, for nested object results.
    :param array_map: Dict of {key, obj} map, for nested object results.
    :param bool_keys: List of in_dict keys that will be extracted as bools
    :param dict_keys: Dict of {key, obj} map, for nested object results.
    :param enums: Dict of {key, `Enum`} map, that will be extracted as `Enum`

    """

    d = dict()

    if str_keys:
        for in_key in str_keys:
            private_name = '_' + in_key
            d[private_name] = in_dict.get(in_key)

    if date_keys:
        for in_key in date_keys:
            private_name = '_' + in_key
            in_date = in_dict.get(in_key)
            if in_date is not None:
                try:
                    out_date = parse_datetime(in_date)
                except TypeError as e:
                    raise ZangException(e)
                    out_date = None
                d[private_name] = out_date
            else:
                d[private_name] = None

    if int_keys:
        for in_key in int_keys:
            private_name = '_' + in_key
            in_int = in_dict.get(in_key)
            if in_int is not None and in_int != '':
                try:
                    out_int = int(in_int)
                except ValueError as e:
                    raise ZangException(e)
                    out_int = None
                d[private_name] = out_int
            else:
                d[private_name] = None

    if real_keys:
        for in_key in real_keys:
            if (in_dict is not None) and (in_dict.get(in_key) is not None):
                private_name = '_' + in_key
                d[private_name] = float(in_dict.get(in_key))

    if bool_keys:
        for in_key in bool_keys:
            if in_dict.get(in_key) is not None:
                private_name = '_' + in_key
                value = in_dict.get(in_key)
                if isinstance(value, str_classes):
                    value = value.lower() == 'true'
                d[private_name] = value

    # ENUMS

    if enums:
        for in_key in enums:
            class_ = enums[in_key]
            if (in_dict is not None) and (in_dict.get(in_key) is not None):
                private_name = '_' + in_key
                dictValue = in_dict.get(in_key)
                try:
                    value = class_(dictValue)
                except Exception as e:
                    try:
                        value = class_(dictValue.title())
                    except Exception as e:
                        value = class_(dictValue.capitalize())
                d[private_name] = value

    # LISTS

    if dict_keys:
        for in_key in dict_keys:
            if in_dict.get(in_key) is not None:
                private_name = '_' + in_key
                d[private_name] = dict(in_dict.get(in_key))

    if object_map:
        for (k, v) in object_map.items():
            if in_dict.get(k):
                private_name = '_' + k
                d[private_name] = v.new_from_dict(in_dict.get(k))

    if array_map:
        for (k, v) in array_map.items():
            if in_dict.get(k):
                private_name = '_' + k
                d[private_name] = [v.new_from_dict(i) for i in in_dict.get(k)]

    obj.__dict__.update(d)
    obj.__dict__.update(kwargs)

    # Save the dictionary, for write comparisons.
    # obj._cache = d
    # obj.__cache = in_dict

    return obj


# from kennethreitz/python-github3
def to_api(in_dict, int_keys=None, date_keys=None, bool_keys=None):
    """Extends a given object for API Production."""

    # Cast all int_keys to int()
    if int_keys:
        for in_key in int_keys:
            if (in_key in in_dict) and (in_dict.get(in_key, None) is not None):
                in_dict[in_key] = int(in_dict[in_key])

    # Cast all date_keys to datetime.isoformat
    if date_keys:
        for in_key in date_keys:
            if (in_key in in_dict) and (in_dict.get(in_key, None) is not None):

                _from = in_dict[in_key]

                if isinstance(_from, str_classes):
                    dtime = parse_datetime(_from)

                elif isinstance(_from, datetime):
                    dtime = _from

                in_dict[in_key] = dtime.isoformat()

            elif (in_key in in_dict) and in_dict.get(in_key, None) is None:
                del in_dict[in_key]

    # Remove all Nones
    for k, v in in_dict.items():
        if v is None:
            del in_dict[k]

    return in_dict


def flatDict(dict_):
    """
    Returns a dictionary containing the non-none elements.

    :param dict_: Dictionary containing elements with `None` as value
    :type dict_: dict

    :return: Dictionary without non-none elements
    :rtype: dict
    """
    dict__ = {}
    for key in dict_.keys():
        value = dict_[key]
        if value is not None:
            if isinstance(value, Enum):
                value = value.value
            elif isinstance(value, date):
                value = str(value)
            dict__[key] = value
    return dict__
