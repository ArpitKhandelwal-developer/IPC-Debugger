# utils.py
import time
import json


def trace_event(trace_list, etype, label=None, meta=None):
    if meta is None:
        meta = {}
    e = {
        'id': int(time.time() * 1000000),  # microsecond event id
        'time': time.time(),
        'type': etype,
        'label': label,
        'meta': meta
    }
    try:
        trace_list.append(e)
    except Exception:
        # fallback if manager list fails
        pass
