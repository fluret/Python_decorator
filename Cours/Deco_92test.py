import pint
import math

def volume(radius, height) -> "cm^3":
    return math.pi * radius**2 * height

ureg = pint.UnitRegistry()
# vol = volume(3, 5) * ureg("cm^3")
unit = volume.__annotations__['return']
vol = volume(3, 5) * ureg(unit)


print(vol)

print(vol.to("cubic inches"))

print(vol.to("gallons").m)