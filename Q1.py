products = [" LAPTOP ", "phone ", " Tablet", "CAMERA "]

cleaned = list(map(lambda s: s.strip().title(), products))

print(cleaned)