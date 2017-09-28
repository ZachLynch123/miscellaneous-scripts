import Media
import webbrowser

toy_story = Media.Movie("Toy Story", "Astory about toys.", 
	'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
	'https://www.youtube.com/watch?v=4KPTXpQehio')

Friday13th = Media.Movie("Friday the 13th: The Final Chapter", "Killer cool dude goes on camp rampage one last time. Or so they think. ^-^",
	'http://img.moviepostershop.com/friday-the-13th-part-4---the-final-chapter-movie-poster-1984-1020776601.jpg',
	'https://www.youtube.com/watch?v=zBme5lOcZF4'
	)
Friday13th.show_trailer()