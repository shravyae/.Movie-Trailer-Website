import webbrowser

class Movie():
        VALID_RATINGS = ["G","PG","PG-13","R","NC-17","Unrated"]

        def __init__(self, movie_title, release_date, poster_image, trailer_youtube, duration_time,VALID_RATINGS):
                self.title = movie_title
                self.release = release_date
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube
                self.duration = duration_time
                self.ratings = VALID_RATINGS
        
        def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)

        def show_image(self):
                webbrowser.open(self.poster_image_url)
                
