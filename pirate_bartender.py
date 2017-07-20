import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def style(questions):
  """Ask user for flavor preferences"""
  prefs = {}
  for entry in questions:
    prefs[entry] = True if raw_input(questions[entry]+" ")[0].lower() == "y" else False
  return prefs


def mixer(prefs):
  """Build drink based upon user's flavor preferences"""
  drink = []
  for choice in prefs:
    if prefs[choice] == True:
      drink.append(random.choice(ingredients[choice]))
  return drink

if __name__ == '__main__':
  print "Arrr! I'm the Pirate Bartender"
  print "Answer me questions with 'y' or 'yes' and I'll mix ye a proper drink"
  prefs = style(questions)
  drink = mixer(prefs)
  if len(drink) > 0:
    ings = drink[0] 
    for ing in drink[1:-1]:
      print ing # debug
      ings += ", " + ing
    if len(drink) > 1:
      ings += ", and " + drink[len(drink) -1]
    print "Here's yer drink -- a mix o'{}".format(ings)
  else:
    print "Ye aint got taste buds? suit ye self then"
    