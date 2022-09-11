'''
List [1,2,"a", 3.14]

List Comprehensions:

        [expr for val in collection ]

        [expr for val in collection if <test> ]

        [expr for val in collection if <test1> and <test2> ]

        [expr for val1 in collection1 and val2 in collecton2 ]
'''
squares = []
for i in range(1,101):
    squares.append(i**2)
print(squares)

# List Comprehension Implementation
print('List Comprehensions Implementation')

squares2 = [i**2 for i in range(1,101)]

print(squares2)

movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story", "Gone With the Wind", "Citizen Kane",
"It's a Wonderful Life", "The Wizard of Oz", "Gattaca", "Rear Window", "Ghostbusters", "To Kill A Mockingbird", "Good Will Hunting",
"2001: A Space Odyssey", " Raiders of the Lost Ark", "Groundhog Day", "CLose Encounters of the Third Kind"]
print(movies)
print("\nMovie title Starts With G :\n")

gmovies = []

for title in movies:
    if title.startswith("G"):
        gmovies.append(title)
print(gmovies)

#List Comprehension Implementation
print('\nMovie title Starts With "G": (List Comprehensions Implementation)\n')

gmovies2 = [title for title in movies if title.startswith("G")]
print(gmovies2)
print("****************************************")
movies3 = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("It's A Wonderful Life", 1946),
("Gattaca", 1997), ("No Country for Old Men", 2007), ("Rear Window", 1954), ("The Lord of the Rings: The Followship of the Ring", 2001),
("Groundhog Day", 1993), ("CLose Encounters of the Third Kind", 1977), ("The Royal Tenenbaums", 2001),
("The Aviator", 2004), ("Raiders of the Lost Ark", 1981)]

print(movies3)
print("list of Movie titles Released earlier than year 2000: \n")
movie_title_year = [title for (title,year) in movies3 if year < 2000]

print(movie_title_year)

print("List Comprehensions can be Used in Scalar Multiplication: i.e 4* [2, -1, 3]")

v = [2, -1, 3]

y = [4*i for i in v ]

print(y)

#Example of List Comprehensions using Cartesian Product
''' if A and B are sets,
then the Cartesian Product
is the set of pairs (a,b) where 'a' is in A and 'b' is in B.

A X B = {(a,b) | a E A, b E B}

Example:

A = {1,3}
B = {x,y}

A X B = { (1,x),(1,y),(3,x),(3,y) }
'''
A = [1,3,5,7,9]
B = [2,4,6,8]

cartesian_product = [(a,b) for a in A for b in B]

print(cartesian_product)
