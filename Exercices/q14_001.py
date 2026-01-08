def check_for_pluto(check=True):
    def my_validator(func):
        def my_wrapper(world):
            liste = ["pluto", "mini", "donald"]
            print(f"Entering {func.__name__} with {world} argument and check={check}")
            if (check and world.lower() in liste):
                print("arg is not a planet!")
            else:
                return func(world)
        return my_wrapper
    return my_validator

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