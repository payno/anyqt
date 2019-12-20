from . import _api

# Names imported from Qt4's QtGui module
__Qt4_QtGui = [
    'QMacPasteboardMime'
]

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtMacExtras import *
