greets = '  Hello Bob   '
print(greets)
greets.lstrip()
print(greets)
greets.rstrip()
print(greets)
greets.strip()
print(greets)

#updated code

greets = '   Hello Bob   '
print(f"Original: '{greets}'")

# These return new strings, so we print the result directly:
print(f"Left strip: '{greets.lstrip()}'")
print(f"Right strip: '{greets.rstrip()}'")
print(f"Full strip: '{greets.strip()}'")
