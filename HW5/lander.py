# CS-171-A Prof Mark Boady
# Homework 5
# Cameron Kelliher
# 12/5/17

T = 0.1
levelIDX = 1
levels = [
    ('Moon', -1.622, 150),
    ('Earth', -9.81, 5000),
    ('Pluto', -0.42, 100),
    ('Neptune', -14.07, 7000),
    ('Uranus', -10.67, 10000),
    ('Saturn', -11.08, 12000),
    ('Jupiter', -25.95, 25000),
    ('Mars', -3.77, 5000),
    ('Venus', -8.87, 10000),
    ('Mercury', -3.59, 5000),
    ('Sun', -274.13, 250000)
]

def ask_fuel(current_fuel):
    while True:
        fuel = input('Enter units of fuel to use:\n')
        try:
            fuel = int(fuel)

            if fuel < 0:
                print('Please enter a positive value')
                continue

            if current_fuel < fuel:
                print('Not enough fuel, please enter a value less than %d units' % current_fuel)
                continue

            return fuel
        except:
            print('Please enter an integer')

def play_level(name, G, F):
    A = 50
    V = 0
    s = 0

    print('Landing on the %s' % name)
    print('Gravity is %f m/s^2' % G)
    print('Initial Altitude: %d meters' % A)
    print('Initial Velocity: %f m/s' % V)
    print('Burning a unit of fuel causes a 0.10 m/s slowdown')
    print('Initial Fuel Level: %d units' % F)
    print('\nGO')

    while A > 0:
        entered_fuel = ask_fuel(F)

        F = F - entered_fuel
        V = V + G + T * entered_fuel
        A = A + V
        s = s + 1

        print('After %d seconds Altitude is %f meters, velocity is %f m/s.' % (s, A if A > 0 else 0, V))
        print('Remaining Fuel: %d units.' % F)

    if -2 < V < 2:
        print('Landed Successfully')
        return True
    else:
        print('Crashed!')
        return False


print('Welcome to Lunar Lander Game.')

while True:
    next_level_input = input('Do you want to play level %d? (yes/no)\n' % levelIDX)

    if next_level_input == 'no':
        break

    level = levels[levelIDX - 1]
    success = play_level(level[0], level[1], level[2])
    if success:
        levelIDX = levelIDX + 1

print('You made it past %d levels.' % (levelIDX - 1))
print('Thanks for playing.')