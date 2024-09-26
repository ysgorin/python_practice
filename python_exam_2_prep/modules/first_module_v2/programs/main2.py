# import sys.path to add packages directory to path variable
from sys import path
path.append('..\\packages')

# import FunI() from iota nested in extra package
# Add type: ignore to skip problem detection for that line.
import extra.iota # type: ignore
print(extra.iota.FunI())