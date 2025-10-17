olympic_2016 = {
    'Archery', 'Athletics', 'Badminton', 'Basketball', 'Boxing', 'Canoeing',
    'Cycling', 'Diving', 'Equestrian', 'Fencing', 'Football', 'Golf',
    'Gymnastics', 'Handball', 'Hockey', 'Judo', 'Modern Pentathlon', 'Rowing',
    'Rugby Sevens', 'Sailing', 'Shooting', 'Swimming', 'Synchronized Swimming',
    'Table Tennis', 'Taekwondo', 'Tennis', 'Triathlon', 'Volleyball', 'Water Polo',
    'Weightlifting', 'Wrestling'
}
print("olympic 2016:",olympic_2016)

olympic_2022 = {
    'Alpine Skiing', 'Biathlon', 'Bobsleigh', 'Cross-Country Skiing', 'Curling',
    'Figure Skating', 'Freestyle Skiing', 'Ice Hockey', 'Luge', 'Nordic Combined',
    'Short Track Speed Skating', 'Skeleton', 'Ski Jumping', 'Snowboarding',
    'Speed Skating'
}
print("olympic 2022:",olympic_2022 )

unique_games=olympic_2016.union(olympic_2022)
print("unique games:",unique_games)

common_games=olympic_2016.intersection(olympic_2022)
print("common games:",common_games)

droped_games=olympic_2022.difference(olympic_2016)
print("droped games:",droped_games)



