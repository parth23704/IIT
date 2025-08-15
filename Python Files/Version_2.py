def seatbelt_alarm(driv, pass_, ign, belt_d_bar, belt_p_bar):
    if ign == 1 and ((driv == 1 and belt_d_bar == 1) or (pass_ == 1 and belt_p_bar == 1)):
        return 0  # ON
    else:
        return 1  # OFF

# Test
print(seatbelt_alarm(1, 0, 1, 1, 0))  # Should be 0