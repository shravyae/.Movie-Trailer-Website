
import fresh_tomatoes
import media   
''' This is entertainment_center.py file that we run and execute. we have 
imported the fresh_tomatoes.py that generates the required html file for this 
project which is given by the Udacity team and also imported media.py that 
has the data structure we need to build the dictionary of movies we want 
to display with its trailer. '''

a =  media.Movie("Spider-Man: Homecoming",
        "2017",
        "https://goo.gl/78krq4",
        "https://www.youtube.com/watch?v=xrzXIaTt99U",
        "2h 13min",
        media.Movie.VALID_RATINGS[2])

b =  media.Movie("Logan",
        "2017",
        "https://goo.gl/4cIIi1",
        "https://www.youtube.com/watch?v=ny3hScFgCIQ",
        "2h 17min",
        media.Movie.VALID_RATINGS[3])

c = media.Movie("Valerian",
        "2017",
        "https://goo.gl/zKknm3",
        "https://www.youtube.com/watch?v=NNrK7xVG3PM",
        "2h 17min",
        media.Movie.VALID_RATINGS[2])

d =  media.Movie("Kidnap",
        "2017",
        "https://goo.gl/UJb5u4",
        "https://www.youtube.com/watch?v=R-Ht8VRPRvU",
        "1h 34min ",
        media.Movie.VALID_RATINGS[5])

e =  media.Movie("Dunkirk",
        "2017",
        "https://goo.gl/DTwdhc",
        "https://www.youtube.com/watch?v=F-eMt3SrfFU",
        "1h 46min",
        media.Movie.VALID_RATINGS[2])

f =  media.Movie("The Shawshank Redemption",
        "1994",
        "https://goo.gl/YE6aaG",
        "https://www.youtube.com/watch?v=6hB3S9bIaco",
        "2h 22min",
        media.Movie.VALID_RATINGS[3])

g =  media.Movie("A Serbian Film",
        "2010",
        "https://goo.gl/B5bRUi",
        "https://www.youtube.com/watch?v=lwNLxAKS-Dw",
        "1h 44min ",
        media.Movie.VALID_RATINGS[4])

h = media.Movie("The Godfather",
        "1972",
        "http://bit.ly/2tYBove",
        "https://www.youtube.com/watch?v=sY1S34973zA",
        "2h 55min",
        media.Movie.VALID_RATINGS[3])

i =  media.Movie("Despicable Me 3",
        "2017",
        "https://goo.gl/g5nkte",
        "https://www.youtube.com/watch?v=euz-KBBfAAo",
        "1h 30min",
        media.Movie.VALID_RATINGS[1])

j =  media.Movie("Hacksaw Ridge",
        "2016",
        "https://goo.gl/FJpdtt",
        "https://www.youtube.com/watch?v=s2-1hz1juBI",
        "2h 19min",
        media.Movie.VALID_RATINGS[3])

k =  media.Movie("Rogue One",
        "2016",
        "https://goo.gl/DLCsd8",
        "https://www.youtube.com/watch?v=4fE_yHEerok",
        "2h 13min",
        media.Movie.VALID_RATINGS[2])

l = media.Movie("Split",
        "2016",
        "https://goo.gl/LL50l7",
        "https://www.youtube.com/watch?v=ROVc_47FUD8",
        "1h 57min",
        media.Movie.VALID_RATINGS[2])

m =  media.Movie("Doctor Strange",
        "2016",
        "https://goo.gl/ymzi6p",
        "https://www.youtube.com/watch?v=kNdM7b1Lm04",
        "1h 55min",
        media.Movie.VALID_RATINGS[2])

n =  media.Movie("Passengers",
        "2016",
        "https://goo.gl/YngVGQ",
        "https://www.youtube.com/watch?v=7BWWWQzTpNU",
        "1h 56min",
        media.Movie.VALID_RATINGS[2])

o =  media.Movie("Deadpool",
        "2016",
        "https://goo.gl/7hxDpD",
        "https://www.youtube.com/watch?v=ONHBaC-pfsk",
        "1h 48min",
        media.Movie.VALID_RATINGS[3])

''' Here we are going to put the above data into an array and trying to open 
it with the help of fresh_tomatoes.py file provided '''
movies = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
fresh_tomatoes.open_movies_page(movies)


