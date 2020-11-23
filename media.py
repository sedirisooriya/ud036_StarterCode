#import webbrowser module
import webbrowser

class Movie():
    #init function
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #function to play movie trailer video
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
