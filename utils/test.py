import sys
import logging
import os
import time
import string
import pbjson
import simplejson
import caffe_pb2
from google.protobuf import text_format

def main():
    net = caffe_pb2.NetParameter()
    text_format.Merge(open("lenet.prototxt").read(), net)
    js = pbjson.pb2json(net)
    net = pbjson.json2pb(caffe_pb2.NetParameter, simplejson.loads(js))  
    print text_format.MessageToString(net)

if __name__  ==  "__main__":
    main()
