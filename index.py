from swimming import Catfish, ClownFish, StringRay, Mallard, Goldfish
from walking import Donkey, Goat, Llama, MiniHorse, Sheep
from slithering import BlackMamba, BrownSnake, Copperhead, RatSnake, Viper
from attractions import PettingZoo, SnakePit, Wetlands
from datetime import date

# Create instances of attractions
varmint_village = PettingZoo("Varmint Village")
slither_inn = SnakePit("Slither Inn")
wetlands_reserve = Wetlands("Wetlands Reserve")

# Create instances of animals
joe = BlackMamba("Joe", "Dendroaspis polylepis", "lizards")
oprah = BrownSnake("Oprah", "Pseudonaja textilis", "spiders")
dory = Copperhead("Dory", "Agkistrodon laticinctus", "frogs")
simon = RatSnake("Simon", "Pantherophis obsoletus", "mice")
devin = Viper("Devin", "Vipera berus", "rabbits")
jason = Catfish("Jason", "Pylodictis olivaris)", "shrimp")
marlin = ClownFish("Marlin", "Premnas biaculeatus", "zooplankton")
mary = Goldfish("Mary", "Ovis aries", "peas")
barry = Mallard("Barry", "Anas platyrhynchos", "popcorn")
michael = StringRay("Michael", "Carassius auratus", "squid")
jake = Donkey("Jake", "Equus africanus asinus", "morning", "straw")
kevin = Goat("Kevin", "Capra aegagrus hircus", "morning", "apples")
jane = Llama("Jane", "Lama glama", "midday", "hay")
mary = Sheep("Mary", "Ovis aries", "afternoon", "grass")
john = MiniHorse("John", "Equus ferus caballus", "midday", "carrots")


# Add animals to their respective attractions
slither_inn.add_animal(joe)
slither_inn.add_animal(oprah)
slither_inn.add_animal(dory)
slither_inn.add_animal(simon)
slither_inn.add_animal(devin)
wetlands_reserve.add_animal(jason)
wetlands_reserve.add_animal(marlin)
wetlands_reserve.add_animal(mary)
wetlands_reserve.add_animal(barry)
wetlands_reserve.add_animal(michael)
varmint_village.add_animal(jake)
varmint_village.add_animal(kevin)
varmint_village.add_animal(jane)
varmint_village.add_animal(mary)
varmint_village.add_animal(john)


# Output a report
def print_attraction_report(attraction):
    print(f"{attraction.attraction_name} is where you'll find {attraction.description}, like:")
    for animal in attraction.animals:
        print(f"   * {animal.name} the {animal.species}")

print_attraction_report(varmint_village)
print_attraction_report(slither_inn)
print_attraction_report(wetlands_reserve)