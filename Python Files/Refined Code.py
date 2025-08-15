def check_alarm():
    driv = int(input("Is the driver present? (1/0): "))
    pass_ = int(input("Is the passenger present? (1/0): "))
    ign = int(input("Is the ignition on? (1/0): "))
    belt_d_bar = int(input("Is the driver belt unfastened? (1/0): "))
    belt_p_bar = int(input("Is the passenger belt unfastened? (1/0): "))

    if ign == 1 and ((driv == 1 and belt_d_bar == 1) or (pass_ == 1 and belt_p_bar == 1)):
        return 0  # Alarm ON
    else:
        return 1  # Alarm OFF
alarm = check_alarm()
print("ALARM =", alarm)
