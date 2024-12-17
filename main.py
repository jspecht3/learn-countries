from lists import countries, asia, eu, af, na, sa, au, me, balkan
from game import skeleton

regions = [countries, asia, eu, af, na, sa, au, me, balkan]
region_names = ["countries", "asia", "eu",
                "af", "na", "sa", "au", "me", "balkan"]


def valid_gamemode(gamemode):
    """Checks if the user entered a valid gamemode"""
    while gamemode not in ["capital", "code"]:
        gamemode = input("  Enter a valid gamemode: ")


def valid_region(region):
    """Checks if the user entered a valid region"""
    in_names = region in region_names

    while not in_names:
        region = input("  Enter a valid region: ")
        in_names = region in region_names

    return region, region_names.index(region)


gamemode = input(
    "Welcome! Select a gamemode: capital, country (code).\n  Gamemode Selected: ")

valid_gamemode(gamemode)

region = input("\nSelect a region from the following:\n  countries, asia, europe (eu), africa (af), north america (na), south america (sa), oceania (au), middle east (me), or balkan.\n  Region Selected: ")

region, index = valid_region(region)

print(f'\n----- Beginning {region} Capital Quiz -----')

skeleton(gamemode, regions[index])
