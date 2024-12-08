# import sys.path to add packages directory to path variable
from sys import path
path.append('..\\packages')

# import FunI() from iota nested in extra package
# Add type: ignore to skip problem detection for that line.
import extra.iota # type: ignore
print(extra.iota.FunI())

# import extra.good.best.sigma, extra.good.best.tau # type: ignore
# print(extra.good.best.sigma.FunS())
# print(extra.good.best.tau.FunT())

# from extra.good.best.sigma import FunS # type: ignore
# from extra.good.best.tau import FunT # type: ignore
# print(FunS())
# print(FunT())

import extra.good.best.sigma as sig # type: ignore
import extra.good.best.tau as tau # type: ignore
print(sig.FunS())
print(tau.FunT())