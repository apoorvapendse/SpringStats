import math


diaToSult = {
    1.0: 1570,
    1.2: 1540,
    1.4: 1500,
    1.6: 1470,
    1.8: 1440,
    2.0: 1420,
    2.5: 1370,
    3.0: 1320,
    3.6: 1270,
    4.0: 1250,
    4.5: 1230,
    5.0: 1190,
    6.0: 1130,
    7.0: 1090,
    8.0: 1050,
}

load = float(input("Enter the load: "))
spring_index = float(input("Enter the spring index: "))
Nt = total_turns = float(input("Enter Total Turns: "))


if spring_index < 3 or spring_index > 15:
    print("Invalid spring index value, should lie between 3 and 15")
    print("exiting the program....")
    exit()
print(
    "Load Entered: "
    + str(load)
    + "\nSpring Index Entered: "
    + str(spring_index)
    + "\nTotal Turns Entered: "
    + str(Nt)
)

C = spring_index

wahls_factor = ((4 * C - 1) / (4 * C - 4)) + (0.615 / C)

print("Wahls Factor: " + str(wahls_factor))

K = wahls_factor
P = load

wire_dia = 0


permissible_stress = -99999999
induced_stress = -9999999999
sult = 0
for dia in diaToSult:
    sult = ultimate_tensile_stress = diaToSult[dia]
    induced_stress = Ti = K * ((8 * P * C) / (math.pi * pow(dia, 2)))
    permissible_stress = Tau = sult * 0.3
    print(
        "induced stress:"
        + str(induced_stress)
        + ", permissible_stress: "
        + str(permissible_stress)
    )
    if permissible_stress > induced_stress:
        wire_dia = dia
        break

if wire_dia == 0:
    print("Error: NO VALID DIAMETER FOUND")
    exit()


G = 81370
D = mean_diameter = C * wire_dia
Di = D - wire_dia
Do = D + wire_dia
solid_length = wire_dia * total_turns
total_gap = (total_turns - 1) * 0.5
N = active_turns = total_turns - 2
max_deflection = delta = (8 * P * pow(D, 3) * active_turns) / G * pow(wire_dia, 4)
free_length = solid_length + total_gap + delta
pitch_of_coil = free_length / (total_turns - 1)
stiffness = G * pow(wire_dia, 4) / 8 * active_turns * pow(D, 3)


print("Inner Diameter:" + str(Di) + "\n")
print("Mean Diameter:" + str(mean_diameter) + "\n")
print("Wahl Factor:" + str(wahls_factor) + "\n")
print("Material:patented and cold drawn steel wires grade 1" + "\n")
print("Sult:" + str(sult) + "\n")
print("Permissible Stress:" + str(permissible_stress) + "\n")
print("Induced Stres:" + str(induced_stress) + "\n")
print("Total Turns:" + str(total_turns) + "\n")
print("Active Turns:" + str(active_turns) + "\n")
print("Style of Contact:Squared" + "\n")
print("Solid Length:" + str(solid_length) + "\n")
print("Total gap:" + str(total_gap) + "\n")
print("Free Length:" + str(free_length) + "\n")
print("Pitch:" + str(pitch_of_coil) + "\n")
print("Stiffness:" + str(stiffness) + "\n")
print("Max Deflection:" + str(max_deflection) + "\n")
