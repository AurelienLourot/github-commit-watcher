#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

import encoding

class Timestamp:
    fields = (("YYYY", "year"  ),
              ("MM"  , "month" ),
              ("DD"  , "day"   ),
              ("hh"  , "hour"  ),
              ("mm"  , "minute"),
              ("ss"  , "second"))

    def __init__(self, obj=None):
        """Builds from 'obj' having the members 'fields' or being a dictionary with these fields.
           Builds from current UTC time if no 'obj' provided.
        """
        now = datetime.datetime.utcnow()
        self.data = {}
        for field in self.fields:
            if obj is not None:
                if isinstance(obj, dict):
                    self.data[field[0]] = obj[field[0]]
                else:
                    self.data[field[0]] = getattr(obj, field[0])
            else:
                self.data[field[0]] = getattr(now, field[1])

    def __unicode__(self):
        return unicode(self.to_datetime())

    def __str__(self):
        return unicode(self).encode(encoding.preferred)

    def __eq__(self, other):
        for field in self.fields:
            if self.data[field[0]] != other.data[field[0]]:
                return False
        return True

    def to_datetime(self):
        try:
            args = []
            for field in self.fields:
                args.append(int(self.data[field[0]]))
            return datetime.datetime(*args)
        except ValueError as e:
            e.args += ("Timestamp malformed?",)
            raise
