#8-6
def city_country(city, country):
    print("_________________________________________________________________"
    +"\n" + '"' + city.title(), country.title() + '"')
    print("_________________________________________________________________")

city_country("San Antonio","USA")
city_country("paris","france")
city_country("Meconos","greece")

#8-7
def make_album(artist, album):
    music_album = {'artist':artist,'album':album}
    return music_album
    
music = make_album('Nirvana','In Uetero')
print(music)
music_1 = make_album('Sublime','40 oz to Freedom')
print(music_1)
music_2 = make_album('Prince','Purple Rain')
print(music_2)

#8-8
def make_album2():
    
    while True:
        artist_name = input("\nEnter an artist name: \nEnter 'q' anytime to " +
        "quit ")
        if(artist_name == 'q'):
            break
        album_name = input("Enter an album from artist: \nEnter 'q' anytime " +
        "quit ")
        if(album_name == 'q'):
            break
        else:
            music_album2 = {'artist':artist_name.title(),'album':album_name.title()}
            return music_album2
    
music_4 = make_album2()
print(music_4)
while music_4:
    music_4 = make_album2()
    print(music_4)
