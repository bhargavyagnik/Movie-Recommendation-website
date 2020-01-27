import mysql.connector as m

#movie Table
moviee=[(1,"Sawshank Redemption","Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.","1999-10-14",142,"R",9.3),
        (2,"The Godfather","The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.","1972-08-24",175,"X",9.2),
        (3,"The Dark Knight","When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham. The Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.","2008-07-24",152,"12A",9),
        (4,"Angry Men","A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence.","1957-04-10",96,"U",8.9),
        (5,"Schindlers List","In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.","1994-02-18",195,"15",8.9),
        (6,"The Lord of the Rings","Gandalf and Aragorn lead the World of Men against Saurons army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.","2003-12-17",201,"12A",8.9),
        (7,"Pulp fiction","The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.","1994-10-21",154,"18",8.9),
        (8,"Joker","A gritty character study of Arthur Fleck, a man disregarded by society.","2019-10-04",122,"15",8.8),
        (9,"The Good, the Bad and the Ugly","A bounty hunting scam joins two men in an uneasy alliance against a third in a race to find a fortune in gold buried in a remote cemetery.","1968-08-09",161,"X",8.8),
        (10,"Fight Club","An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.","1999-11-12",139,"18",8.8),
        (11,"Forrest Gump","The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate, and other history unfold through the perspective of an Alabama man with an IQ of 75.","1994-10-07",142,"12A",8.8),
        (12,"Inception","A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.","2010-07-16",148,"12A",8.8),
        (13,"The Matrix","A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.","1999-06-11",136,"15",8.7),
        (14,"Goodfellas","The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen Hill and his mob partners Jimmy Conway and Tommy DeVito in the Italian-American crime syndicate.","1990-10-26",146,"18",8.7),
        (15,"Seven","Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives.","1996-01-05",127,"18",8.6)
        ]

actorr=[
    ("Tim Robbins","Male"),
    ("Morgan Freeman","Male"),
    ("Bob Gutton","Male"),
    ("Marlon Brando","Male"),
    ("Al Pacino", "Male"),
    ("James Cann", "Male"),
    ("Christian Bale", "Male"),
    ("Heath Ledger", "Male"),
    ("Aaron Eckhart", "Male"),
    ("Henry Fonda", "Male"),
    ("Lee J Cobb", "Male"),
    ("Martin Balsam", "Male"),
    ("Liam Neeson", "Male"),
    ("Ralph Fiennes", "Male"),
    ("Ben Kinglsey", "Male"),
    ("Elijah Wood", "Male"),
    ("Viggo Mortensen", "Male"),
    ("Ian Mckellen", "Male"),
    ("John Travolta", "Male"),
    ("Uma Thurman", "Female"),
    ("Samuel Jackson", "Male"),
    ("Joaquin Phoenix", "Male"),
    ("Robert De Niro", "Male"),
    ("Zazie Beetz", "Female"),
    ("Clint Eastwood", "Male"),
    ("Eli Wallach", "Male"),
    ("Lee Van Cleef", "Male"),
    ("Brad Pitt", "Male"),
    ("Edward Norton", "Male"),
    ("Meat Loaf", "Male"),
    ("Tom Hanks", "Male"),
    ("Robin Wright", "Male"),
    ("Gary Sinise", "Male"),
    ("Leonardo Di Caprio", "Male"),
    ("Joseph Gordon Levitt", "Male"),
    ("Ellen Page", "Female"),
    ("Keanu Reaves", "Male"),
    ("Lawrence Fishburne", "Male"),
    ("Carrie Anne Moss", "Female"),
    ("Ray Liotta", "Male"),
    ("Joe Pesci", "Male"),
    ("Kevin Spacey", "Male")
]
acts=[
    (1,1),
    (1,2),
    (1,3),
    (2,4),
    (2,5),
    (2,6),
    (3,7),
    (3,8),
    (3,9),
    (4,10),
    (4,11),
    (4,12),
    (5,13),
    (5,14),
    (5,15),
    (6,16),
    (6,17),
    (6,18),
    (7,19),
    (7,20),
    (7,21),
    (8,22),
    (8,23),
    (8,24),
    (9,25),
    (9,26),
    (9,27),
    (10,28),
    (10,29),
    (10,30),
    (11,31),
    (11,32),
    (11,33),
    (12,34),
    (12,35),
    (12,36),
    (13,37),
    (13,38),
    (13,39),
    (14,23),
    (14,40),
    (14,41),
    (15,2),
    (15,28),
    (15,42)

]
movie_img=[
    (1,"1.jpg"),
    (2,"2.jpg"),
    (3, "3.jpg"),
    (4, "4.jpg"),
    (5,"5.jpg"),
    (6, "6.jpg"),
    (7, "7.jpg"),
    (8, "8.jpg"),
    (9, "9.jpg"),
    (10, "10.jpg"),
    (11, "11.jpg"),
    (12, "12.jpg"),
    (13, "13.jpg"),
    (14, "14.jpg"),
    (15, "15.jpg"),
]
directorr=[
    (1,"Frank Daramont"),
    (2,"Francis Ford Coppola"),
    (3, "Christopher Nolan"),
    (4, "Sidney Lumet"),
    (5, "Steven Spielberg"),
    (6, "Peter Jackson"),
    (7, "Quenten Tarantinno"),
    (8, "Todd Philips"),
    (9, "Sergio Leone"),
    (10, "David Fincher"),
    (11, "Robert Zemeckis"),
    (12, "Lana Wachowski"),
    (13, "Nicholas Pegi"),
    (14, "Andrew Kevin Walker")
]
directss=[
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
    (11, 11),
    (3, 12),
    (12,13),
    (13, 14),
    (14, 15)
]
writer=[
    (1,"Stephen King "),
    (2,"Frank Daramont"),
    (3,"Mario Puzo"),
    (4,"Francis Ford Coppola"),
    (5,"Jonathan Nolan"),
    (6,"Christopher Nolan"),
    (7,"Reginald Rose"),
    (8,"Thomas Keneally"),
    (9,"Steven Zaillian"),
    (10,"J.R.R Tolkein"),
    (11,"Fran Walsh"),
    (12,"Quentin Terentino"),
    (13,"Roger Avary"),
    (14,"Todd Philips"),
    (15,"Scott Silver"),
    (16,"Sergio Leone"),
    (17,"Luciano Vincezoni"),
    (18,"Chuck Palahnuik"),
    (19,"Jim Uhis"),
    (20,"Winston Groom"),
    (21,"Eric Roth"),
    (22,"Lana Wachowshki"),
    (23,"Lily Wachowshki"),
    (24,"Nichilas Pegii"),
    (25,"david Fincher"),

]
writes=[
    (1,1),
    (1,2),
    (2,3),
    (2,4),
    (3, 5),
    (3, 6),
    (4, 7),
    (5, 8),
    (5, 9),
    (6, 10),
    (6, 12),
    (7,12),
    (7, 13),
    (8, 14),
    (8, 15),
    (9, 16),
    (9, 17),
    (10, 18),
    (10, 19),
    (11, 20),
    (11, 21),
    (12, 6),
    (13, 22),
    (13, 23),
    (14, 24),
    (15, 25)
]
rating=[
    (1,9.5,1),
    (2,9.4,2),
    (3,9.2,3),
    (4, 9.0, 4),
    (5, 8.8, 5),
    (6, 9.2, 6),
    (7, 9.0, 7),
    (8, 9.4, 8),
    (9, 8.9, 9),
    (10, 9.2, 10),
    (11, 9.0, 11),
    (12, 9.2, 12),
    (13, 8.9, 13),
    (14, 9.0, 14),
    (15, 8.7, 15)
]
review=[
    (1,"Amazing Movie with an equally amazing suspense", 1),
    (2,"An Iconic Film",2),
    (3, "The Batman of our dreams! So much more than a comic book movie", 3),
    (4, "Good script, great dialogs and a set of actors who would be the envy of the world", 4),
    (5, "Schindler's List Is The Greatest Film About The Holocaust", 5),
    (6, "Not only the best of the Lord of the Rings series, but sets a new standard of epic filmmaking.", 6),
    (7, "It's Wild, It's Chaotic, It's Pulp Fiction!!!", 7),
    (8, "As a viewer that actually went to TIFF and witnessed this film and didn't want to believe the hype, it is an absolute MASTERPIECE and Phoenix is a certified legend.", 8),
    (9, "Brutal, brilliant, and one of the best Westerns ever made", 9),
    (10, "a dangerously brilliant film that entertains as well as enlightens.", 10),
    (11, "Let's see the world through the eyes of Forrest Gump", 11),
    (12, "Insanely Brilliant ! Nolan has outdone himself !!", 12),
    (13, "Immensely entertaining, intriguingly philosophical and just about one of the best films ever made!", 13),
    (14, "In one word: perfection", 14),
    (15, "Se7en is well crafted and ingeniously clever, making it one of the greatest films of the 90s", 15),
]
config = {
    'user': 'bhargav',
    'password': '12345',
    'database':'imdb'
}
mydb=m.connect(**config)

mycursor=mydb.cursor()
#mycursor.executemany("insert into movie values (%s,%s,%s,%s,%s,%s,%s,%s)",moviee)
#mycursor.executemany("insert into actor(Actor_name,Gender) values (%s,%s)",actorr)
#mycursor.executemany("insert into acts(Movie_id,Actor_id) values (%s,%s)",acts)
#mycursor.executemany("insert into director values (%s,%s)",directorr)
#mycursor.executemany("insert into directs values (%s,%s)",directss)
#mycursor.executemany("insert into writer values (%s,%s)",writer)
#mycursor.executemany("insert into writes values (%s,%s)",writes)
#mycursor.executemany("insert into rating values (%s,%s,%s)",rating)
#mycursor.executemany("insert into reviews values (%s,%s,%s)",review)
#mydb.commit()
#print("1 record inserted, ID:", mycursor.lastrowid)

def  getmoviedetails():
    mycursor.execute("select * from movie")
    myresult = mycursor.fetchall()
    print(myresult)
    return myresult

def getmovietitle():
    mycursor.execute("select movie.movie_title from movie")
    myresult = mycursor.fetchall()
    return myresult

def getmovie_page(movi_id):
    mycursor.execute("select * from movie where movie_id=%s",[movi_id])
    movie = mycursor.fetchall()
    return movie

def getactors(name):
    mycursor.execute("select actor_name from actor join acts on actor.actor_id=acts.actor_id join movie on movie.movie_id=acts.movie_id where movie.movie_title=%s group by actor.actor_id;", [name])
    actor = mycursor.fetchall()
    print(actor)
    return actor
def getwriter(name):
    mycursor.execute("select writer_name from writer join writes on writer.writer_id=writes.writer_id join movie on movie.movie_id=writes.movie_id where movie.movie_title=%s group by writer.writer_id;",[name])
    writer = mycursor.fetchall()
    print(writer)
    return writer
def getdirector(name):
    mycursor.execute("select director_name from director join directs on director.director_id=directs.director_id join movie on movie.movie_id=directs.movie_id where movie.movie_title=%s group by director.director_id;",[name])
    director = mycursor.fetchall()
    print(director)
    return director
def getratings(name):
    mycursor.execute("select rating.rating_score from rating join movie on movie.movie_id=rating.movie_id where movie_title=%s group by rating.rating_id",[name])
    rating= mycursor.fetchall()
    print(rating)
    return rating
def getreviews(name):
    mycursor.execute(
        "select reviews.review from reviews join movie on movie.movie_id=reviews.movie_id where movie_title=%s group by reviews.review_id",
        [name])
    review = mycursor.fetchall()
    print(review)
    return review
def moviegenre(name):
    mycursor.execute(
        "select genre.name from genre join gen on gen.genre_id=genre.genre_id join movie on movie.movie_id=gen.movie_id where movie.movie_title=%s group by genre.genre_id",
        [name])
    genre = mycursor.fetchall()
    print(genre)
    return genre

m=getmovie_page(2)
a=getactors(m[0][1])
b=getwriter(m[0][1])
c=getdirector(m[0][1])
d=getratings(m[0][1])
e=getreviews(m[0][1])
f=moviegenre(m[0][1])