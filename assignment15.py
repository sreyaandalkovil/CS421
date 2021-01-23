class moviecollection:
    def __innit__(self, list_of_movies):
        self.list_of_movies=list_of_movies
        
    def __repr__(self):  
       return 'SILC(list_of_movies=%s)' % (self.list_of_movies)
    
    def __str__(self):  
       return 'SILC(list_of_movies=%s)' % (self.list_of_movies)
       
    
    def count_songs(self): 
        total = 0
        for movie_songs in self.list_of_movies:
            count = len(cs_class.list_of_songs)
            total = total + count
        return total
        
class movies:
    def __init__(self, list_of_songs):
        self.list_of_songs = list_of_songs
      
    def __repr__(self):  
       return 'movies(list_of_songs=%s)' % (self.list_of_songs)
    
    def __str__(self):  
       return 'movies(list_of_songs=%s)' % (self.list_of_songs)
       
       
class song:
    def __init__(self, name, genre, singer):
        self.name = name
        self.genre = genre
        self.singer = singer
  
    def __repr__(self):  
       return 'song(name=%s, genre=%s, singer=%s)' % (self.name, self.genre, self.singer)
    
    def __str__(self):   
       return 'song(name=%s, genre=%s, singer=%s)' % (self.name, self.genre, self.singer)
       
       
class people:
    def __init__(self, gender, age, name):
        self.gender = gender
        self.age = age
        self.name = name
  
    def __repr__(self):  
       return 'people(gender=%s, age=%s, name=%s)' % (self.gender, self.age, self.name)
    
    def __str__(self):  
       return 'people(gender=%s, age=%s, name=%s)' % (self.gender, self.age, self.name)



song_1= song("let it go", "pop", "idina menzel")
song_2 = song("do you want to build a snowman", "pop", "kristen bell")
song_3= song( "mother knows bestr", "pop", "donna murphy")


person_1= people("female", "unknown", "elsa")
person_2= people("female", "18", "anna")
person_3= people("female", "18", "repunzel")

frozen_people = [person_1, person_2]
frozen_movie = movies(frozen_people)

tangled_people = [person_3]
tangled_movie = movies(tangled_people)

list_of_movies = [tangled_movie, frozen_movie]
disneymovies = moviecollection(list_of_movies)

total_count_of_songs = disneymovies.count_songs()
print("All Movies --> ", disneymovies)
print("Total Count of Songs ", total_count_of_songs)
