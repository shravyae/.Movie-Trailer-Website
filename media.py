import webbrowser

class Movie():
    def __init__(self, movie_title, release_date, poster_image, trailer_youtube, duration_time, movie_rating):
        self.title = movie_title
        self.release = release_date
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.duration = duration_time
        self.rating = movie_rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_image(self):
        webbrowser.open(self.poster_image_url)
        
        
        
