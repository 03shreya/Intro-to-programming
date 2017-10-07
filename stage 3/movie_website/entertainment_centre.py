import fresh_tomatoes
import media

Ratatouille = media.Movie("Ratatouille","A story about a rat , who soon discovers his inner talents.",
                          "http://www.canmag.com/images/front/movies2007/ratatouilleposter5.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

Harry_Potter = media.Movie("Harry Potter" ,"A film based on a hidden magical world.",
                           "http://harrypotterfanzone.com/wp-content/2015/07/prisoner-of-azkaban-theatrical-poster-2.jpg",
                           "https://www.youtube.com/watch?v=L8-e_VdwAME")

The_lord_of_the_rings = media.Movie("The Lord of the rings","It is a film series consisting of three high fantasy adventure films directed by Peter Jackson.",
                                    "http://www.impawards.com/2001/posters/lord_of_the_rings_the_fellowship_of_the_ring_ver4.jpg",
                                    "https://youtu.be/V75dMMIW2B4")
Gravity = media.Movie("Gravity","It is a science fiction.","http://www.impawards.com/2013/posters/gravity.jpg","https://youtu.be/OiTiKOy59o4")


The_Vow = media.Movie("The Vow" , " The Vow is a 2012 American romantic drama film" ,
                      "https://upload.wikimedia.org/wikipedia/en/c/c2/The_Vow_Poster.jpg",
                      "https://www.youtube.com/watch?v=tdF01cA7jOE")

Inception = media.Movie("Inception","Inception is a 2010 science fiction heist thriller film",
                        "http://www.impawards.com/2010/posters/inception.jpg",
                        "https://youtu.be/8hP9D6kZseM" )


#print(Harry_Potter.storyline)

#Ratatouille.show_trailer()

movies = [Ratatouille,Harry_Potter,The_lord_of_the_rings,Gravity ,The_Vow , Inception]

fresh_tomatoes.open_movies_page(movies)
