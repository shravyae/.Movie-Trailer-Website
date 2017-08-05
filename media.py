import webbrowser

class Video():

        ''' This is an Array to store the ratings which are constant'''
        VALID_RATINGS = ["G","PG","PG-13","R","NC-17","Unrated"]

        ''' This is a data structure to store the basic information of the 
movies like its name, date of release, duration of the cinema and its rating'''
        def __init__(self, movie_title,
                release_date,
                duration_time,
                VALID_RATINGS):
                self.title = movie_title
                self.release = release_date
                self.duration = duration_time
                self.ratings = VALID_RATINGS

class Movie(Video):
        
        ''' In this class, we get the basic information from the Video Class and 
use it to add its art, video path and open them in a web browser accordingly'''
        def __init__(self, movie_title,
                release_date,
                poster_image, 
                trailer_youtube, 
                duration_time,
                VALID_RATINGS):
                Video.__init__(self,movie_title,
                        release_date,
                        duration_time,
                        VALID_RATINGS)
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube
        
        def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)

        def show_image(self):
                webbrowser.open(self.poster_image_url)
