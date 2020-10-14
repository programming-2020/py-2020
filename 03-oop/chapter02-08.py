# Multiple inheritance - The diamond problem

from packages.pack08.subclass_bad import SubClassBad
from packages.pack08.subclass import SubClass

bad = SubClassBad()
bad.callMe()
print()
subclass = SubClass()
