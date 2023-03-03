# import module
import json

# Data to be written
data = {
	"mydata": {
		"name": "damini khatik",
		"age": 22,
		"Place": "warora",
         "student at":"bit",
         "year":"final year",
		"Blood group": "O+"
  
	}
}

# Serializing json and
# Writing json file
with open( "data.json" , "w" ) as write:
	json.dump( data , write )
print(data)
