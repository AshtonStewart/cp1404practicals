"""
started 11:28
"""


from guitar import Guitar
def test_guitar():

    given_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    made_up_guitar = Guitar("Ashton Bok", 2023, 99999999)

    guitar_list = [given_guitar, made_up_guitar]

    #print(guitar_list[0].get_age())
    for guitars in guitar_list:
        print(f"{guitars.name} ({guitars.get_age()}) : ${guitars.cost}")
        print(f"Is {guitars.name} vintage?: {guitars.is_vintage()}")
        #age = get_age(Guitars[1])
        #print(guitars)

test_guitar()