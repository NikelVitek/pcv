import physics

weight_earth = physics.weight_on_surface(10, "Earth")
weight_moon = physics.weight_on_surface(10, "Moon")
time_to_travel = physics.time_to_travel_distance(100000)
speed_of_sound = physics.speed_of_sound_in_air(25)

print(f"Weight on Earth: {weight_earth} N")
print(f"Weight on the Moon: {weight_moon} N")
print(f"Time to travel 100,000 meters at the speed of light: {time_to_travel} seconds")
print(f"Speed of sound in air at 25°C: {speed_of_sound} m/s")