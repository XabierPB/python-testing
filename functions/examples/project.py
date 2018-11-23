

class Project(object):
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def __repr__(self):
        return "Project '%s from %s to %s" % (self.name, self.start.isoformat(), self.end.isoformat())

