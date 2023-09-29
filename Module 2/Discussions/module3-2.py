def add_character(player_name, character_name, character_class, character_race, character_level, characters=[]):
  table = 0
  if character_level < 4:
    table = 1
    if len([character for character in characters if character['Character level'] < 4]) >= 6:
      print('Not enough seats available for low level characters')
      return characters
  elif len([character for character in characters if character['Character level'] > 3]) >= 6:
    print('Not enough seats available for high level characters')
    return characters
  else:
    table = 2
  
  character_dict = {
    'Name': player_name,
    'Character name': character_name,
    'Character class': character_class,
    'Character race': character_race,
    'Character level': character_level,
    'Table': table
  }
  
  characters.append(character_dict)
  return characters

def get_character_from_user():
  print('Enter player name: ')
  player_name = input()
  print('Enter character name: ')
  character_name = input()
  print('Enter character class: ')
  character_class = input()
  print('Enter character race: ')
  character_race = input()
  character_level = 0
  while character_level < 1 or character_level > 20:
    try:
      print('Enter character level: ')
      character_level = input()
      character_level = int(character_level)
    except ValueError:
      print('Invalid character level entered')
      character_level = 0
  return add_character(player_name, character_name, character_race, character_class, character_level)
  
def print_characters(characters):
  # get the number of tables using set
  tables = set([character['Table'] for character in characters])
  
  characters.sort(key=lambda x: x['Name'])
  for table in range(1, len(tables) + 1):
    print(f'Table {table}:')
    for character in characters:
      if character['Table'] == table:
        print(f'{character["Name"]}: {character["Character name"]} - {character["Character class"]} - {character["Character level"]}')
    print()
  

characters = get_character_from_user()
characters = add_character('Miles E', 'Sliv', 'Paladin', 'Dragonborn', 3)
characters = add_character('Vik E', 'Helena', 'Paladin', 'Aasamir', 3)
characters = add_character('Jeff E', 'Grog', 'Bard', 'Dragonborn', 5)
characters = add_character('Toby D', 'Tav', 'Wizard', 'Tiefling', 1)
characters = add_character('Jerry F', 'Sophos', 'Sorceror', 'High Elf', 4)
characters = add_character('Toby D', 'Tav', 'Wizard', 'Gnome', 5)
characters = add_character('Shelly C', 'Fili', 'Wizard', 'Halfling', 2)
characters = add_character('David B', 'Padme', 'Wizard', 'Halfling', 6)
characters = add_character('Henry L', 'Sal', 'Wizard', 'Human', 7)
characters = add_character('Frank C', 'Sly', 'Rogue', 'Drow Elf', 2)
characters = add_character('Debra Z', 'Fairbow', 'Ranger', 'Wood Elf', 1)
characters = add_character('Sherry L', 'Taffy', 'Bard', 'Tiefling', 3)
characters = add_character('Diane O', 'Peanut', 'Barbarian', 'Gnome', 4)
print_characters(characters)