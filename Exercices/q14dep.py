@check_for_pluto(check=False)
def my_func(planet):
    print(f"Hello, {planet}!")

my_func("World")
my_func("Pluto")

@check_for_pluto(check=True)
def my_func(planet):
    print(f"Hello, {planet}!")

my_func("World")
my_func("Pluto")
my_func("Earth")
my_func("mini")