from biletiniAl import biletiniAl
from eventMagScraper import eventMagScraper
serhat = eventMagScraper()
x = serhat.scrape_all(15)
print(x)
sinema = biletiniAl()
movies = sinema.scrape_cinema(15)
print(".......................................")
print(movies)

