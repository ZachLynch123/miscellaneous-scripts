import Media
import webbrowser
import fresh_tomatoes
Up_movie = Media.Movie("UP", "about a house that flies", 
	'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRj-LAdP8F_hChDCTvNFr_8E-WHtw_4h1D2n3IK1mu34BtDMdA',
	'https://youtu.be/pkqzFUhGPJg?t=5s')

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
Saving_Private_Ryan = Media.Movie("Saving Private Ryan", "boom boom nazi killing",
	"http://is5.mzstatic.com/image/thumb/Video/v4/66/83/44/668344c7-a8fa-107c-72f9-b1fdceb226c6/source/1200x630bb.jpg",
	"https://www.youtube.com/watch?v=RYID71hYHzg")
nb4c = Media.Movie("Nightmare Before Christmas", "bone daddy?",
	"https://fanart.tv/fanart/movies/9479/movieposter/the-nightmare-before-christmas-54ebd7ec25354.jpg",
	"https://www.youtube.com/watch?v=8qrB9I3DM80")

movies = [Up_movie,Friday13th,aNES, TCM,Saving_Private_Ryan,nb4c]
print(Media.Movie.RATING)
print(Media.Movie.__module__)

#fresh_tomatoes.open_movies_page(movies)