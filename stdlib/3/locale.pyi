# Stubs for locale (Python 3.4)
#
# NOTE: This stub is based on a stub automatically generated by stubgen.

from _locale import *

def format(percent, value, grouping=..., monetary=..., *additional): ...
def format_string(f, val, grouping=...): ...
def currency(val, symbol=..., grouping=..., international=...): ...
def str(val): ...
def atof(string, func=...): ...
def atoi(str): ...
def normalize(localename): ...
def getdefaultlocale(envvars=...): ...
def getlocale(category=...): ...
def resetlocale(category=...): ...
def getpreferredencoding(do_setlocale=...): ...
