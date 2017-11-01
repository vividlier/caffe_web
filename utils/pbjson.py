#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import os
import inspect
import simplejson
from google.protobuf.descriptor import FieldDescriptor as FD

def dict_parser(*argv, **kwargs):
    """
    
    Arguments:
    - `*argv`:
    """
    msg = argv[0]
    obj = argv[1]
    name = argv[2]
    _t = kwargs.get('repeated', 0) and 'repeated' or 'required'
    if name and (_t != 'repeated'):
        msg = getattr(msg, name)
    ks = obj.keys()
    
    for idx, k in enumerate(ks):
        _par(msg, obj[k], k)

def list_parser(*argv, **kwargs):
    """
    
    Arguments:
    - `*argv`:
    """
    msg = argv[0]
    obj = argv[1]
    name = argv[2]
    if not obj:
        return
    _rp = kwargs.get('repeated', 0) and 'repeated' or 'required'
    if name:
        if _rp == 'repeated':
            name = '%s_node' % (name, )
    _m = getattr(msg, name)
    for o in obj:
        if isinstance(o, (dict, list)):
            _m = getattr(msg, name).add()
            _par(_m, o, name, repeated=1)
        else:
            _m.append(o)

def other_parser(*argv, **kwargs):
    """
    
    Arguments:
    - `*argv`:
    """
    msg = argv[0]
    obj = argv[1]
    name = argv[2].lower()
    if obj is None:
        obj = ''
    if name:
        setattr(msg, name, obj)
    else:
        msg = obj

def get_parser(obj):
    """
    
    Arguments:
    - `obj`:
    """
    _t = type(obj)
    _tn = 'other'
    if _t is dict:
        _tn = 'dict'
    elif _t is list:
        _tn = 'list'
    _f = '%s_parser' % (_tn, )
    _m = sys.modules[__name__]
    for _n, _func in  inspect.getmembers(_m):
        if _n == _f:
            return _func
    return None

def _par(*argv, **kwargs):
    """
    
    Arguments:
    - `obj`:
    """
    msg = argv[0]
    obj = argv[1]
    name = argv[2]
    _f = get_parser(obj)
    return _f(msg, obj, name, **kwargs)

def pb2dict(obj):
    """
    Takes a ProtoBuf Message obj and convertes it to a dict.
    """
    adict = {}
    if not obj.IsInitialized():
        return None
    for field in obj.DESCRIPTOR.fields:
        if not getattr(obj, field.name):
            continue
        if not field.label == FD.LABEL_REPEATED:
            if not field.type == FD.TYPE_MESSAGE:
                adict[field.name] = getattr(obj, field.name)
            else:
                value = pb2dict(getattr(obj, field.name))
                if value:
                    adict[field.name] = value
        else:
            if field.type == FD.TYPE_MESSAGE:
                adict[field.name] = \
                    [pb2dict(v) for v in getattr(obj, field.name)]
            else:
                adict[field.name] = [v for v in getattr(obj, field.name)]
    return adict

def json2pb(obj, string):
    instance = obj()
    _par(instance, string, '') 
    return instance

def pb2json(obj):
    """
    Takes a ProtoBuf Message obj and convertes it to a json string.
    """
    return simplejson.dumps(pb2dict(obj), sort_keys=True, indent=4)


