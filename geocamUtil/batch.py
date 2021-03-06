# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

from collections import deque


class BatchProcessor(object):
    def __init__(self, func, n):
        self.func = func
        self.n = n
        self.queue = deque()

    def add(self, elt):
        self.queue.append(elt)
        if len(self.queue) >= self.n:
            self.flush()

    def flush(self):
        self.func(self.queue)
        self.queue.clear()
