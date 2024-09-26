# import sys.path to add packages directory to path variable
from sys import path
path.append('..\\packages')

# import FunI() from iota nested in extra package
import extra.iota
print(extra.iota.FunI())