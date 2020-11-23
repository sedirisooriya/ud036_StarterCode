# import media and fresh_tomatoes
import media
import fresh_tomatoes

#generate movie instances from movie class
wonder_woman = media.Movie("Wonder Woman",
                        "Princess Diana of an all-female Amazonian race rescues US pilot Steve. Upon learning of a war, she ventures into the world of men to stop Ares, the god of war, from destroying mankind.",
                        "https://movieposters2.com/images/1483556-b.jpg",
                        "https://www.youtube.com/watch?v=INLzqh7rZ-U")

baby_driver = media.Movie("Baby Driver",
                     "Doc forces Baby, a former getaway driver, to partake in a heist, threatening to hurt his girlfriend if he refuses. But the plan goes awry when their arms dealers turn out to be undercover officers.",
                     "https://m.media-amazon.com/images/M/MV5BMjM3MjQ1MzkxNl5BMl5BanBnXkFtZTgwODk1ODgyMjI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=z2z857RSfhk")

oceans_eight = media.Movie("Ocean's 8",
                     "Debbie Ocean is released from jail after serving a prison sentence. She assembles a special crew of seven women to steal a diamond necklace, worth 150 million dollars, from the Met Gala.",
                     "https://images-na.ssl-images-amazon.com/images/I/516LaSCAUlL._AC_.jpg",
                     "https://www.youtube.com/watch?v=n5LoVcVsiSQ")

secret_life_of_pets = media.Movie("The Secret Life of Pets 2",
                        "At a farm, Max meets the sheepdog Rooster who tries to help him overcome his fears. Back home, Gidget loses Max's favourite toy.",
                        "https://moviereviewmom.com/wp-content/uploads/2019/05/The-Secret-Life-oF-Pets-2-movie-poster.jpg",
                        "https://www.youtube.com/watch?v=mYocfuqu2A8")

joker = media.Movie("Joker",
                     "Arthur Fleck, a party clown, leads an impoverished life with his ailing mother. However, when society shuns him and brands him as a freak, he decides to embrace the life of crime and chaos.",
                     "https://images-na.ssl-images-amazon.com/images/I/61c8%2Bf32PJL._AC_SY879_.jpg",
                     "https://www.youtube.com/watch?v=zAGVQLHvwOY")

monte_carlo = media.Movie("Monte Carlo",
                     "Grace, who is vacationing in Paris with her best friend and stepsister, is mistaken for a British heiress. The three women are whisked away to Monte Carlo, where they discover royalty and romance.",
                     "https://images-na.ssl-images-amazon.com/images/I/719eSDhsSJL._AC_SL1500_.jpg",
                     "https://www.youtube.com/watch?v=cH8JJvmeggk")

#add movies to a movie list
movies = [wonder_woman, baby_driver, oceans_eight, secret_life_of_pets, joker, monte_carlo]

#push movies list to open_movies_page to load website
fresh_tomatoes.open_movies_page(movies)
