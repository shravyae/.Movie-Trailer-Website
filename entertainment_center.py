
import fresh_tomatoes
import media   
''' This is entertainment_center.py file that we run and execute. we have 
imported the fresh_tomatoes.py that generates the required html file for this 
project which is given by the Udacity team and also imported media.py that 
has the data structure we need to build the dictionary of movies we want 
to display with its trailer. '''

a =  media.Movie("Spider-Man: Homecoming",
                        "2017",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1_SY1000_CR0,0,658,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=xrzXIaTt99U",
                        "2h 13min",
                        media.Movie.VALID_RATINGS[2])

b =  media.Movie("Logan",
                        "2017",
                        "http://t1.gstatic.com/images?q=tbn:ANd9GcRPoMqL1vglrh7OF_69pT8gYMYnYaq1r7WfPMcD587V9uOR_hW2",
                        "https://www.youtube.com/watch?v=ny3hScFgCIQ",
                        "2h 17min",
                        media.Movie.VALID_RATINGS[3])
c = media.Movie("Valerian",
                        "2017",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMDAxNDUyNV5BMl5BanBnXkFtZTgwOTc3MzcxMjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=NNrK7xVG3PM",
                        "2h 17min",
                        media.Movie.VALID_RATINGS[2])

d =  media.Movie("Kidnap",
                        "2017",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTcyNDgyODEzOV5BMl5BanBnXkFtZTgwMTI4MTA2MjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=R-Ht8VRPRvU",
                        "1h 34min ",
                        media.Movie.VALID_RATINGS[5])
e =  media.Movie("Dunkirk",
                        "2017",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BN2YyZjQ0NTEtNzU5MS00NGZkLTg0MTEtYzJmMWY3MWRhZjM2XkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=F-eMt3SrfFU",
                        "1h 46min",
                        media.Movie.VALID_RATINGS[2])

f =  media.Movie("The Shawshank Redemption",
                        "1994",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco",
                        "2h 22min",
                        media.Movie.VALID_RATINGS[3])

g =  media.Movie("A Serbian Film",
                        "2010",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNmEyODc1M2YtZDFiNS00YmQxLWEwY2YtMTQwNTk1NzUyYTBlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
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
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNjUyNzQ2MTg3Ml5BMl5BanBnXkFtZTgwNzE4NDM3MTI@._V1_SY1000_CR0,0,631,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=euz-KBBfAAo",
                        "1h 30min",
                        media.Movie.VALID_RATINGS[1])

j =  media.Movie("Hacksaw Ridge",
                        "2016",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQ1NjM3MTUxNV5BMl5BanBnXkFtZTgwMDc5MTY5OTE@._V1_SY1000_CR0,0,647,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=s2-1hz1juBI",
                        " 2h 19min",
                        media.Movie.VALID_RATINGS[3])

k =  media.Movie("Rogue One",
                        "2016",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwMzMxODIzOV5BMl5BanBnXkFtZTgwNzg3OTAzMDI@._V1_SY1000_SX675_AL_.jpg",
                        "https://www.youtube.com/watch?v=4fE_yHEerok",
                        "2h 13min",
                        media.Movie.VALID_RATINGS[2])

l = media.Movie("Split",
                        "2016",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BZTJiNGM2NjItNDRiYy00ZjY0LTgwNTItZDBmZGRlODQ4YThkL2ltYWdlXkEyXkFqcGdeQXVyMjY5ODI4NDk@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=ROVc_47FUD8",
                        "1h 57min",
                        media.Movie.VALID_RATINGS[2])

m =  media.Movie("Doctor Strange",
                        "2016",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNjgwNzAzNjk1Nl5BMl5BanBnXkFtZTgwMzQ2NjI1OTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=kNdM7b1Lm04",
                        "1h 55min",
                        media.Movie.VALID_RATINGS[2])

n =  media.Movie("Passengers",
                        "2016",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk4MjU3MDIzOF5BMl5BanBnXkFtZTgwMjM2MzY2MDI@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=7BWWWQzTpNU",
                        "1h 56min",
                        media.Movie.VALID_RATINGS[2])

o =  media.Movie("Deadpool",
                        "2016",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUzMjQ5Mzc3M15BMl5BanBnXkFtZTgwNDExMjE3NzE@._V1_SY1000_SX686_AL_.jpg",
                        "https://www.youtube.com/watch?v=ONHBaC-pfsk",
                        "1h 48min",
                        media.Movie.VALID_RATINGS[3])

''' Here we are going to put the above data into an array and trying to open it
 with the help of fresh_tomatoes.py file provided '''
movies = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
fresh_tomatoes.open_movies_page(movies)


