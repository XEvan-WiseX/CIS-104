str = 'X-DSPAM-Confidence:0.8475'

reference_point = str.find(":")

floating_var = float(str[reference_point+1:])

print(floating_var)