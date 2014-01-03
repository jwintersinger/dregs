# From http://stackoverflow.com/a/14620633/1691611
class AttrDict(dict):
  '''
  Permit access to dictionary keys as attributes (i.e., d['k'] can be accessed as d.k).
  '''
  def __init__(self, *args, **kwargs):
    super(AttrDict, self).__init__(*args, **kwargs)
    self.__dict__ = self
