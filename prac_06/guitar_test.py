"""
started 11:28
"""


from guitar import Guitar
def test_guitar():

    given_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    made_up_guitar = Guitar("Ashton Bok", 2023, 99999999)

    #print(guitar_list[0].get_age())

    print(f"{given_guitar.name} ({given_guitar.get_age()}) : ${given_guitar.cost}")
    print(f"Is {given_guitar.name} vintage?: {given_guitar.is_vintage()}")
    print(f"Expected True, got {given_guitar.is_vintage()}")

    print(f"{made_up_guitar.name} ({made_up_guitar.get_age()}) : ${made_up_guitar.cost}")
    print(f"Is {made_up_guitar.name} vintage?: {made_up_guitar.is_vintage()}")
    print(f"Expected False, got {made_up_guitar.is_vintage()}")


        #age = get_age(Guitars[1])
        #print(guitars)

test_guitar()