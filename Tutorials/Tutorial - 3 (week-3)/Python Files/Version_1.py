# Get inputs
DRIV = int(input("Driver there? (1/0): "))
PASS = int(input("Passenger there? (1/0): "))
IGN = int(input("Ignition on? (1/0): "))
BELT_D_bar = int(input("Driver belt unfastened? (1/0): "))
BELT_P_bar = int(input("Passenger belt unfastened? (1/0): "))

# Check logic
if IGN == 1 and ((DRIV == 1 and BELT_D_bar == 1) or (PASS == 1 and BELT_P_bar == 1)):
    ALARM = 0  # ON
else:
    ALARM = 1  # OFF
print("ALARM =", ALARM)