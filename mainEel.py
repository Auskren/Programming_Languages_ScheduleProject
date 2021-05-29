import eel

eel.init("www")
eel.start("index.html", options={'mode': 'electron'}, suppress_error=True)
