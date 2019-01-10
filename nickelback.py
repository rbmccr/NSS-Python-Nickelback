# 1. Define a set that contains tuples. Each tuple should contain two strings:
  # The name of an artist
  # A song by that artist
# Make sure that some of the songs are from the band Nickelback. You can see a list of their greatest hits on Amazon.
music = {
  ('Nickelback', 'How You Remind Me'),
  ('Will.i.am', 'That Power'),
  ('Miles Davis', 'Stella by Starlight'),
  ('Nickelback', 'Animals'),
  ('Muse','Supermassive Black Hole')
}

# 2. Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.
actual_music = {song for song in music if song[0] != 'Nickelback'}

print(actual_music)
# PRINT RESULT: {('Miles Davis', 'Stella by Starlight'), ('Muse', 'Supermassive Black Hole'), ('Will.i.am', 'That Power')}