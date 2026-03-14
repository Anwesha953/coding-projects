import pandas as pd
import random

movies = [
    "Avatar","Titanic","The Dark Knight","Inception","Interstellar","The Matrix","The Matrix Reloaded",
    "The Matrix Revolutions","The Avengers","Avengers: Age of Ultron","Avengers: Infinity War","Avengers: Endgame",
    "Iron Man","Iron Man 2","Iron Man 3","Thor","Thor: Ragnarok","Thor: Love and Thunder",
    "Captain America: The First Avenger","Captain America: Civil War","Doctor Strange","Doctor Strange in the Multiverse of Madness",
    "Guardians of the Galaxy","Guardians of the Galaxy Vol. 2","Black Panther","Black Panther: Wakanda Forever",
    "Spider-Man","Spider-Man 2","Spider-Man 3","Spider-Man: Homecoming","Spider-Man: Far From Home","Spider-Man: No Way Home",
    "Man of Steel","Batman v Superman","Justice League","Wonder Woman","Wonder Woman 1984",
    "The Flash","Aquaman","Shazam","The Dark Knight Rises","Batman Begins",
    "Star Wars","The Empire Strikes Back","Return of the Jedi","The Force Awakens","The Last Jedi","The Rise of Skywalker",
    "Rogue One","Solo","Jurassic Park","The Lost World: Jurassic Park","Jurassic World","Jurassic World: Fallen Kingdom","Jurassic World Dominion",
    "The Lion King","Frozen","Frozen II","Moana","Encanto","Coco","Toy Story","Toy Story 2","Toy Story 3","Toy Story 4",
    "Finding Nemo","Finding Dory","Inside Out","Up","Cars","Cars 2","Cars 3","Ratatouille",
    "The Incredibles","The Incredibles 2","Monsters, Inc.","Monsters University",
    "Harry Potter and the Sorcerer's Stone","Harry Potter and the Chamber of Secrets","Harry Potter and the Prisoner of Azkaban",
    "Harry Potter and the Goblet of Fire","Harry Potter and the Order of the Phoenix",
    "Harry Potter and the Half-Blood Prince","Harry Potter and the Deathly Hallows Part 1",
    "Harry Potter and the Deathly Hallows Part 2",
    "The Lord of the Rings: The Fellowship of the Ring","The Lord of the Rings: The Two Towers",
    "The Lord of the Rings: The Return of the King","The Hobbit: An Unexpected Journey",
    "The Hobbit: The Desolation of Smaug","The Hobbit: The Battle of the Five Armies",
    "Dune","Dune: Part Two","Blade Runner","Blade Runner 2049","The Martian","Gravity","Arrival",
    "Gladiator","The Prestige","The Departed","The Social Network","Fight Club","Forrest Gump",
    "The Shawshank Redemption","Pulp Fiction","Se7en","The Godfather","The Godfather Part II",
    "Mad Max: Fury Road","John Wick","John Wick: Chapter 2","John Wick: Chapter 3 – Parabellum","Mission: Impossible",
    "Mission: Impossible 2","Mission: Impossible III","Mission: Impossible – Ghost Protocol","Mission: Impossible – Rogue Nation",
    "Mission: Impossible – Fallout","Top Gun","Top Gun: Maverick","Pacific Rim","Transformers","Transformers: Revenge of the Fallen",
    "Transformers: Dark of the Moon","Transformers: Age of Extinction","Transformers: The Last Knight",
    "Pirates of the Caribbean: The Curse of the Black Pearl","Pirates of the Caribbean: Dead Man's Chest",
    "Pirates of the Caribbean: At World's End","Pirates of the Caribbean: On Stranger Tides",
    "Pirates of the Caribbean: Dead Men Tell No Tales","Shrek","Shrek 2","Shrek the Third","Kung Fu Panda",
    "Kung Fu Panda 2","Kung Fu Panda 3","How to Train Your Dragon","How to Train Your Dragon 2","How to Train Your Dragon: The Hidden World",
    "Minions","Despicable Me","Despicable Me 2","Despicable Me 3","Sing","Sing 2","Zootopia","Big Hero 6",
    "WALL-E","Soul","Luca","Turning Red","Elemental","The Batman","Joker","Suicide Squad","The Suicide Squad",
    "Deadpool","Deadpool 2","Logan","X-Men","X2","X-Men: The Last Stand","X-Men: First Class","Days of Future Past",
    "The Wolverine","Venom","Venom: Let There Be Carnage","Morbius","Fantastic Four","Fantastic Four: Rise of the Silver Surfer",
    "Doctor Dolittle","Jumanji","Jumanji: Welcome to the Jungle","Jumanji: The Next Level","Ready Player One",
    "Edge of Tomorrow","Elysium","I Am Legend","Oblivion","Minority Report","War of the Worlds","A Quiet Place",
    "A Quiet Place Part II","Bird Box","World War Z","I, Robot","Ex Machina","Her","Moon","Passengers",
    "No Time to Die","Skyfall","Spectre","Casino Royale","Quantum of Solace"
]

genres = [
    "Action", "Adventure", "Sci-Fi", "Drama", "Fantasy",
    "Animation", "Crime", "Thriller", "Comedy", "Romance"
]

data = []

for movie in movies:
    genre = " ".join(random.sample(genres, 2))
    data.append({
        "title": movie,
        "genre": genre
    })

df = pd.DataFrame(data)
df.to_csv("movies.csv", index=False)

print("movies.csv created successfully!")