# You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising. 
# The list is ordered according to who signed up first.
# Your task is to return one of the following strings:
# < firstName here >, < country here > of the first Python developer who has signed up; or
# There will be no Python developers if no Python developer has signed up.

from platform import python_branch


list1 = [
  { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
  { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
  { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }
]
list3 = [
  { "first_name": "Sofia", "last_name": "P.", "country": "Italy", "continent": "Europe", "age": 41, "language": "Clojure" },
  { "first_name": "Jayden", "last_name": "P.", "country": "Jamaica", "continent": "Americas", "age": 42, "language": "JavaScript" },
  { "first_name": "Sou", "last_name": "B.", "country": "Japan", "continent": "Asia", "age": 43, "language": "Python" },
  { "first_name": "Rimas", "last_name": "C.", "country": "Jordan", "continent": "Asia", "age": 44, "language": "Java" }
]
list = list3 + list1
language = "Python"

def findAdmin(list, language):
    fn = ''
    country = ''
    
    for dev in list:
      if dev['language'] == language:
        fn = dev['first_name']
        country = dev['country']
        return fn + ', ' + country
        break

    return 'There will be no Python developers'

print(findAdmin(list, language))
