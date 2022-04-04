from buildingmotif import BuildingMOTIF, get_building_motif
from buildingmotif.singleton import SingletonNotInstantiatedException

try:
    get_building_motif()
except SingletonNotInstantiatedException:
    print("BuildingMOTIF not instantiated")
# Create a new singleton object
instance_1 = BuildingMOTIF(something="something")
print(f"instance string: {instance_1.something}") #prints "instance string: something"
# Create new object
instance_2 = BuildingMOTIF(something="something else")
print(f"instance string: {instance_2.something}") #prints "instance string: something", init is skipped as object already exists
# Create new object with new_instance flag
instance_3 = BuildingMOTIF(something="set", new_instance=True)
print(f"instance string: {instance_3.something}") #prints "instance string: set", a new instance is created
# Check global instance
print(f"instance string: {get_building_motif().something}") #prints "instance string: something", original instance is singelton
# Make instance 3 global
instance_3.make_global()
print(f"instance string: {get_building_motif().something}") #prints "instance string: set", global singelton is now instance_3

#instance = get_building_motif()
#print(instance.something)