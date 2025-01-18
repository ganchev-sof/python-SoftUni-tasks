length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

aquarium = length * width * height
aquarium_in_liters = aquarium / 1000
needed_liters = aquarium_in_liters * (1 - percent)

print(needed_liters)
