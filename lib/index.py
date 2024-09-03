# Manipulating Class Attributes From Instance Methods
class Album:

    album_count = 0

    def __init__(self, date):
        Album.album_count += 1
        self.release_date = date


date = "3/09/2024"
one = Album(date)
two = Album(date)
three = Album(date)

print(Album.album_count)
# 3


# Defining a Class method
class Album:

    album_count = 0

    def __init__(self, date):
        self.increase_album_count()
        self.release_date = date

    @classmethod
    def increase_album_count(cls, increment=1):
        cls.album_count += increment

album1 = Album('2023-01-01')
album2 = Album('2024-01-01')
album3 = Album('2025-01-01')

# Output the total number of albums created
print(Album.album_count)  # Output: 3        



# Class Constants


class Album:

    GENRES = ["Hip-Hop", "Pop", "Jazz"]
    album_count = 0

    def __init__(self, genre, date):
        if self.check_genre(genre):
            self.increase_album_count()
            self.genre = genre
            self.release_date = date

    @classmethod
    def check_genre(cls, genre):
        return genre in cls.GENRES

    @classmethod
    def increase_album_count(cls, increment=1):
        cls.album_count += increment

print(Album.GENRES)   #  ["Hip-Hop", "Pop", "Jazz"]

Album.GENRES = "not a list anymore"
print(Album.GENRES)   # "not a list anymore"
