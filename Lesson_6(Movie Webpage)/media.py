import webbrowser
class Movie():
    def __init__(self,movie_title,movie_story,movie_poster,youtube_url):
        self.title = movie_title
        self.story = movie_story
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = youtube_url

    def show_trailor(self):
        webbrowser.open(self.trailer_youtube_url)
        
