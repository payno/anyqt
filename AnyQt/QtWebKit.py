from . import _api

# Names imported from Qt4's QtWebKit module
__Qt4_QtWebKit = [
    'QWebDatabase',
    'QWebElement',
    'QWebElementCollection',
    'QWebHistory',
    'QWebHistoryInterface',
    'QWebHistoryItem',
    'QWebPluginFactory',
    'QWebSecurityOrigin',
    'QWebSettings',
    'qWebKitMajorVersion',
    'qWebKitMinorVersion',
    'qWebKitVersion'
]

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtWebKit import *
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtWebKit import *
