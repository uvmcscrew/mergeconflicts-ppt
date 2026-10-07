years = 0
resource = 1.0

rate = 1.028

thresh = 5

print(f"{resource} (yr = {years})")

while resource < thresh:
    resource *= rate
    years += 1
    print(f"{resource} (yr = {years})")



print(years)