# Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = int(input("Enter distance in km: "))

if distance < 3:
    print("Take a walk")
elif distance >= 3 and distance < 15:
    print("Book a bike")
else:
    print("Prefer a car")