import media
import fresh_tomatoes

dil_to_pagal_hai = media.Movie("Dil to Pagal Hai",
                        "A story of love and dance",
                        "http://globoxrentals.com/site/wp-content/uploads/2014/09/dil-pagal-hai-movie-poster.jpg",
                        "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&sqi=2&ved=0CCcQtwIwAWoVChMIprPVqYafyAIVhhgeCh0CPAtZ&url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DBdhPleFcEJ0&usg=AFQjCNGOEpcPWpMWPRbmohrfSlOP99vleA&sig2=3MHcmMXfnlWp91IB9oXRyg&bvm=bv.103627116,d.dmo")
# print(dil_to_pagal_hai.storyline)

rab_ne_bana_di_jodi = media.Movie("Rab Ne Bana Di Jodi",
                                  "A story of a husband who disguises into the man his wife will love",
                                  "https://upload.wikimedia.org/wikipedia/en/a/ab/Rab_Ne_Bana_Di_Jodi.jpg",
                                  "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=4&ved=0CDYQtwIwA2oVChMI9JbDjYifyAIVBnYeCh1_bQOT&url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dr-v6Qdj5XEs&usg=AFQjCNHImp4zEo4M61db3gZfMa7hcP96oQ&sig2=2pKLU3zGwMPLRAM3S18stA&bvm=bv.103627116,d.dmo")
# print(rab_ne_bana_di_jodi.storyline)

vivah = media.Movie("Vivah",
                    "A story of love and arranged marriage, the old fashioned way",
                    "http://megasabi.com/explore/wp-content/uploads/2014/01/vivah.jpeg",
                    "https://www.youtube.com/watch?v=Kd4e9olBVYw")
# print(vivah.storyline)
# vivah.show_trailer()

yuva = media.Movie("Yuva",
                   "A story about love and politics",
                   "https://upload.wikimedia.org/wikipedia/en/2/21/Yuva_(movie_poster).jpg",
                   "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0CB8QyCkwAGoVChMIttXOmY6fyAIVkrIeCh38wQ5M&url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DkCW-EV0rv-I&usg=AFQjCNF1ictthrXVKr13QBKeXpV0Zlku4A&sig2=NiCCFv1VEE4NhgAfLfZh6Q&bvm=bv.103627116,d.dmo")
# print(yuva.storyline)


movies = [dil_to_pagal_hai, rab_ne_bana_di_jodi, vivah, yuva]

fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
