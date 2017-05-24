import media
import webbrowser
import fresh_tomatoes
bahubali = media.Movie("Bahubali: The Beginning",
                       "A very powerful warrior who fights his enemies for saving his village",
                       "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",
                       "https://www.youtube.com/watch?v=sOEg_YZQsTI")
#print(bahubali.story)
dangal = media.Movie("Dangal",
                     "An old man who teaches wrestling to few girls.",
                     "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")
#Dangal.show_trailor()
fan = media.Movie("Fan",
                  "A fan's obsession of his idol Shah Rukh Khan",
                  "https://upload.wikimedia.org/wikipedia/en/a/a3/Fan-First-Look.jpg",
                  "https://www.youtube.com/watch?v=nkS_Ar0Yad0")
borat = media.Movie("Borat",
                    "A journalist travelling through United States recording real life interactions with Americans",
                    "https://upload.wikimedia.org/wikipedia/en/3/39/Borat_ver2.jpg",
                    "https://www.youtube.com/watch?v=vlnUa_dNsRQ")
kaabil = media.Movie("Kaabil",
                     "A crime drama film featuring a love affair between two blind people",
                     "https://upload.wikimedia.org/wikipedia/en/c/ce/Kaabil_Movie_Poster.jpg",
                     "https://www.youtube.com/watch?v=nubDFeiUAsI")
raees = media.Movie("Raees",
                    "An action crime thriller film based on the life of a gangster/criminal",
                    "https://upload.wikimedia.org/wikipedia/en/2/2b/Raees_Poster.jpg",
                    "https://www.youtube.com/watch?v=J7_1MU3gDk0")
movies = [bahubali,dangal,fan,borat,kaabil,raees]
fresh_tomatoes.open_movies_page(movies)
