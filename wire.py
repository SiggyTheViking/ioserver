#!/usr/bin/env python

import json

obj = {
    "cmd":"say_it",
    "args":["hello","world"]}

def say(args_array):
    print ' '.join(args_array)


dispatch_object = {
    "say_it":say
}

msg_string = json.dumps(obj)

print msg_string

print "imagine sending that over the wire..."

new_obj = json.loads(msg_string)

if dispatch_object.has_key(new_obj['cmd']):
    dispatch_object[new_obj['cmd']](new_obj['args'])
