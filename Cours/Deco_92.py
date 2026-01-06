import pint
from  volume import volume
ureg = pint.UnitRegistry()
unit = volume.__annotations__['return']
vol = volume(3, 5) * ureg(unit)

print(vol)

print(vol.to("cubic inches"))

print(vol.to("gallons"))

print(vol.to("gallons").m)