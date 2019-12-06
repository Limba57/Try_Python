def print_people(*people):
    for person in people:
        print("this person is", person)


print_people("seb", "kathia", "arthur", "limba")

print("------")

print_people("arthur")

print("-----")

print_people(12, True, "kathia", 3.2, 3.2 + 2.8)
