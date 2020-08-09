books = [
            {
                'title':'pride and prejudice',
                'authors':
                    [{
                        'name':'Jane Austen',
                        'birth_year':1775
                    }],
                'pub_year':1813
            },
            {
                'title':'pride and prejudice and zombies',
                'authors':
                        [
                            {
                                'name':'Jane Austen',
                                'birth_year':1775,
                            },
                            {
                                'name':'Seth_graham_smith',
                                'birth_year':1976
                            }
                        ],
                'pubyear':2009
            }
        ]
print("pride and prejudice was written by jane austen in 1813")
print(books[0]["title"]+"was written by"+books[0]["authors"][0]["name"]+" in "+str(books[0]["pub_year"]))
print(f"title is {books[0]["title"]}")
#print( books[0]["title"]+" was written by "+books[0]["authors"]["name"]+" in "+books[0]["pub_year"])
print("pride and prejudice and zombies was written by seth graham-smith in 2009")
print(books[1]["title"]+" was written by"+books[1]["authors"][1]["name"]+" in "+str(books[1]["pubyear"]))