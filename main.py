import swapi
def get_film_info(id):
    film = swapi.get_film(film_id)
    characters = film.get_characters().items
    vehicles = film.get_vehicles().items
    starships = film.get_starships().items
    species = film.get_species().items

    print(f'Фільм: {film.title}')

    print(f"Персонажі: ")
    for index, character in enumerate(characters, 1):
        print(f'{index}.  {character.name} з планети {character.get_homeworld().name}')

    print(f"Транспортні засоби: ")

    for index, vehicle in enumerate(vehicles, 1):
        print(f'{index}.  {vehicle.name}')

    print(f"Космічні кораблі: ")
    for index, starship in enumerate(starships, 1):
        print(f'{index}.  {starship.name}')

    print(f"Види істот: ")
    for index, specie in enumerate(species, 1):
        print(f'{index}.  {specie.name}')

if __name__ == '__main__':
    print("1:'A New Hope', 2:'The Empire Strikes Back', 3:'Return of the Jedi', 4:'The Phantom Menace', 5:'Attack of the Clones', 6:'Revenge of the Sith'.")
    film_id = input("Введіть ідентифікатор фільму: ")
    get_film_info(film_id)
