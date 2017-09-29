import Media
import webbrowser
import fresh_tomatoes
toy_story = Media.Movie("Toy Story", "Astory about toys.", 
	'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
	'https://www.youtube.com/watch?v=4KPTXpQehio')

Friday13th = Media.Movie("Friday the 13th: The Final Chapter", "Killer cool dude goes on camp rampage one last time. Or so they think. ^-^",
	'http://img.moviepostershop.com/friday-the-13th-part-4---the-final-chapter-movie-poster-1984-1020776601.jpg',
	'https://www.youtube.com/watch?v=zBme5lOcZF4'
	)
aNES = Media.Movie("A Nightmare on Elm Street", "You can run, but you can't hide, bitch!",
	"https://www.movieposter.com/posters/archive/main/97/MPW-48795",
	"https://www.youtube.com/watch?v=ZuYoEtEI_go")
TCM = Media.Movie("A Texas Chainsaw Massacre", "REEEEEEEEEEEEEEEEEEE",
	"https://images-na.ssl-images-amazon.com/images/I/51uBhqYdUZL._SY300_.jpg",
	"https://www.youtube.com/watch?v=Vs3981DoINw")
#Friday13th.show_trailer()
Default = Media.Movie("Default","Desc","Picture","Trailer")
movies = [toy_story,Friday13th,aNES, TCM]

fresh_tomatoes.open_movies_page(movies)