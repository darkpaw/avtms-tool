# FIELDS – TRAINING ORGANISATION (NAT00010) FILE POSITION LENGTH TYPE

NAT00010 = [
    # ["Training organisation identifier", 1, 10, 'A'],

    ["10toi", "Training organisation identifier", 1, 10, 'A'],
    ["10ton", "Training organisation name", 11, 100, 'A'],
    ["10toti", "Training organisation type identifier", 111, 2, 'N'],
    ["10afl", "Address first line", 113, 50, 'A'],
    ["10asl", "Address second line", 163, 50, 'A'],
    ["10slt", "Address location – suburb, locality or town", 213, 50, 'A'],
    ["10pc", "Postcode", 263, 4, 'A'],
    ["10si", "State identifier", 267, 2, 'N'],

    # Record length for national data collection: 268
    # Not National?
    # Contact name 269 60 A
    # Telephone number 329 20 A
    # Facsimile number 349 20 A
    # Email address 369 80 A
    # Carriage return/line feed (ASCII 13/10): 2

]

# Record length for national data collection: 180
# Carriage return/line feed (ASCII 13/10): 2
