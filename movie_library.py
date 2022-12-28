import random
from datetime import date
from datetime import datetime


class Movies():

    def __init__(self, title, year, genre, impressions):
        self.title = title
        self.year = year
        self.genre = genre
        self.impressions = impressions

        # Variables
        self.current_impressions = 0

    def inc_impressions(self, step = 1):
       self.current_impressions += step

    def __repr__(self) -> str:
        
        return f"Movies(title = {self.title} year = {self.year} genre = {self.genre} impressions = {self.impressions})"

    def __str__(self) -> str:
        return f'{self.title} {self.year} '

    def play(self):
        self.impressions += 1
        

        

class Series(Movies):
    def __init__(self, season_number, episode_number, *args, **kwargs):
       super().__init__(*args, **kwargs)

       self.season_number = season_number
       self.episode_number = episode_number

    def __repr__(self) -> str:
        
        return f"Series(title = {self.title} year = {self.year} genre = {self.genre} season_number = {self.season_number} episode_number = {self.episode_number}  impressions = {self.impressions})"

    def __str__(self) -> str:
        return f'{self.title} {self.year} {self.genre} {self.season_number} {self.episode_number} {self.impressions} '




def times_10():         # uruchamia 10 razy funkcję generate_views
    counter = 0
    while counter < 10:
        generate_views()
        counter += 1


    
def generate_views():          # generuje wyświetlenia (1 - 100) dla losowo wybranego elementu z biblioteki (content)
   
    num = random.randint(0,len(content) - 1)

    content[num].current_impressions = 0
   
    

    views = random.randint(1, 100)

    content[num].inc_impressions(views)
    content[num].impressions += content[num].current_impressions





def top_titles(content_type):           # funkcja sortuje wg wyświetleń od najmniejszego do największego
    top_movies = []
    top_series = []


    by_impressions = sorted(content, key=lambda item: item.impressions)
    by_impressions = by_impressions[::-1]

    if content_type == 'm':
        print("Najpopularniejsze filmy: ")
        for item in by_impressions:
            if isinstance(item, Series) == False:
                top_movies.append(item)

        return top_movies

    if content_type == 's':
        print("Najpopularniejsze seriale: ")
        for item in by_impressions:
            if isinstance(item, Series) == True:
                top_series.append(item)
        return top_series        




def get_movies():
    movies = []
    for item in content:
        if isinstance(item, Series) == False:
            movies.append(item)


    movies_sorted = sorted(movies, key=lambda m: m.title)

    return movies_sorted
    

def get_series():
    series = []
    for item in content:
        if isinstance(item, Series) == True:
            series.append(item)

    series_sorted = sorted(series, key=lambda s: s.title)


    return series_sorted

def search(my_title):           # wyszukuje film lub serial po jego tytule.
    for item in content:
        if item.title == my_title:
            print(item)
            break
                
        else:
            print("Tego tytułu nie ma w bibliotece filmów i seriali")
            break
                
        


test_movie = Movies(title = 'Desperado',  year = '1995', genre = 'akcja', impressions = 0)
test_series = Series(title = 'McGywer', year = '1986', genre = 'akcja', impressions = 0, season_number = '3', episode_number = '10')


content = []
content.append(Movies(title = 'Desperado',  year = '1995', genre = 'action', impressions = 0))
content.append(Series(title = 'McGywer', year = '1986', genre = 'action', impressions = 0, season_number = '3', episode_number = '10'))
content.append(Movies(title = 'The Shawshank Redemption', year = '1994', genre = 'action', impressions = 0))   
content.append(Movies(title = 'The Godfather', year = '1972', genre = 'action', impressions = 0))   
content.append(Movies(title = 'The Dark Knight', year = '2008', genre = 'action', impressions = 0)) 
content.append(Movies(title = 'The Godfather Part II', year = '1974', genre = 'action', impressions = 0)) 
content.append(Movies(title = 'Schindlers List', year = '1993', genre = 'action', impressions = 0)) 
content.append(Movies(title = 'The Lord of the Rings: The Return of the King', year = '2003', genre = 'action', impressions = 0)) 
content.append(Movies(title = 'Pulp Fiction', year = '1994', genre = 'action', impressions = 0)) 
content.append(Series(title = 'Shooter', year = '2021', genre = 'action', impressions = 0, season_number = '3', episode_number = '5'))
content.append(Series(title = 'Friends', year = '1990', genre = 'comedy', impressions = 0, season_number = '10', episode_number = '8'))
content.append(Series(title = 'Suits', year = '2020', genre = 'Comedy drama', impressions = 0, season_number = '4', episode_number = '7'))
content.append(Series(title = 'S.W.A.T.', year = '2002', genre = 'Black story', impressions = 0, season_number = '4', episode_number = '5'))
content.append(Series(title = 'Narcos', year = '2018', genre = 'Drama', impressions = 0, season_number = '3', episode_number = '4'))
content.append(Series(title = 'The Witcher', year = ' 2020', genre = 'Fantasy', impressions = 0, season_number = '2', episode_number = '12'))
content.append(Series(title = 'El Chapo', year = '2016', genre = 'Thriller', impressions = 0, season_number = '3', episode_number = '10'))


# Wygeneruje odtworzenia treści za pomocą funkcji generate_views.

print("-----------------------")
print()
print("Biblioteka filmów.")

times_10()
now = datetime.now()
print("Najpopularniejsze filmy i seriale dnia: ", now.strftime("%d/%m/%Y"))
print()
print()


# lista w której umieszczam obiekty posortowane wg wyświetleń od największego do najmniejszego




print()
for item in top_titles('s')[0:3]:         # Wyświetlam wybraną ilość (w tym wyp. 3) filmów ('m') lub seriali  ('s') o największej oglądalności
    print(item)


print()
print()
print("Drukuje filmy alfabetycznie: ")
print()

for item in get_movies():
    print(item)



print()
print()
print("Drukuje seriale alfabetycznie: ")
print()

for item in get_series():
    print(item)


print()
print()
print("Sprawdzam czy tytuł jest w bibliotece filmów i seriali.")
print()


search('Desperado')
search('O dwóch takich, co ukradli Księżyc')



'''
Filmy i seriale mają metodę play, która zwiększa liczbę odtworzeń danego tytułu o 1.                                                                    --> zrobione

Po wyświetleniu serialu jako string pokazują się informacje o konkretnym odcinku, np.: “The Simpsons S01E05” (gdzie po S pokazany jest                  --> nie kapuje jak zrobić
numer sezonu w notacji dwucyfrowej, natomiast po E - numer odcinka, również w zapisie dwucyfrowym).

Po wyświetleniu filmu jako __string__ widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”.                                                            --> zrobione

Przechowuje filmy i seriale w jednej liście.                                                                                                            --> zrobione







Dodatkowo:

Napisz funkcje get_movies oraz get_series, które będą filtrować listę i zwracać odpowiednio tylko                                                       --> zrobione
filmy oraz tylko seriale. Posortuj listę wynikową alfabetycznie.

Napisz funkcję search, która wyszukuje film lub serial po jego tytule.                                                                                  --> zrobione

Napisz funkcję generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.         --> zrobione

Napisz funkcję, która uruchomi generate_views 10 razy.                                                                                                  --> zrobione

Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych tytułów z biblioteki.                                                       --> zrobione

Dla chętnych: dodaj do funkcji parametr content_type,                                                                                                   --> zrobione
którym wybierzesz czy mają zostać pokazane filmy, czy seriale.







Niech program po uruchomieniu działa w następujący sposób:

Wyświetli na konsoli komunikat Biblioteka filmów.                                   --> zrobione

Wypełni bibliotekę treścią.                                                         --> zrobione

Wygeneruje odtworzenia treści za pomocą funkcji generate_views.                     --> zrobione

Wyświetli na konsoli komunikat Najpopularniejsze filmy i seriale dnia <data>,       --> zrobione
gdzie <data> to bieżąca data w formacie DD.MM.RRRR.

Wyświetli listę top 3 najpopularniejszych tytułów.                                  --> zrobione





Zadania dla chętnych:
Napisz funkcję, która za pomocą pętli dodaje pełne sezony seriali do biblioteki. Funkcja powinna przyjmować parametry takie jak: 
tytuł serialu, rok wydania, gatunek, numer sezonu, liczba odcinków do dodania.

Do klasy reprezentującej serial, dopisz funkcję zewnętrzną, która wyświetla liczbę odcinków danego serialu dostępnych w bibliotece.


Parametr to zmienna wymieniona w nawiasach w definicji funkcji.
Argument to wartość, która jest wysyłana do funkcji w momencie jej wywołania.
'''