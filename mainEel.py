import eel
from Scheduler import *
eel.init("www")
eel.start("index.html", options={'mode': 'default'}, suppress_error=True)
