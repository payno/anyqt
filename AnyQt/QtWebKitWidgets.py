from . import _api

# Names imported from Qt4's QtWebKit module
__Qt4_QtWebKit = [
    'QGraphicsWebView',
    'QWebFrame',
    'QWebHitTestResult',
    'QWebInspector',
    'QWebPage',
    'QWebView',
]

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtWebKitWidgets import *
