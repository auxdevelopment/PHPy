"""

Config object
has attributes from the config file at config/config.conf

"""


class Config():
  
  def __init__(self):
    self.configFilePath = "config/config.conf"  

    self.host = getHost()
    self.port = getPort()
    self.root = getRoot()
    
  def getHost():
    pass
