from datetime import datetime

class Person(object):
	def __init__(self, params):
		self.id: str # https://stackoverflow.com/questions/1210458/how-can-i-generate-a-unique-id-in-python
		self.names: list # List of Names
		self.gender: str # enum Male / Female
		self.spoken_languages: list # List of spoken languages: https://www.loc.gov/standards/iso639-2/php/code_list.php

		self.birth_date: datetime # YYYY-MM-DDThh:mm:ssTZD https://www.w3.org/TR/NOTE-datetime
		self.birth_location: Location
		self.death_date: datetime # yyyy-MM-dd HH:mm:ss
		self.death_location: Location

		self.biography: str # Markdown

		self.buried: list # List of [{ Location, Datetime }, { Location, Datetime }]

		self.canonization: list # List of Canonization 
		self.shrines: Location
		self.feast_date: list # List of datetime
		self.patron: list # List of patrons Ex. [Youth, Students, Gamers, Information Technology, Internet, Computer Programmers]
		self.images: list # List of Images
		self.vocation: str # https://www.religiousministries.com/catholic-vocations/vocations-in-the-church/


class Location(object):
	def __init__(self, params):
		self.name: str
		self.position: self.Position
		self.address: str
		self.postal_code: int
		self.country_code: str
		# TODO https://ux.shopify.com/designing-address-forms-for-everyone-everywhere-f481f6baf513
		# Interesting results close by: https://read.acloud.guru/location-based-search-results-with-dynamodb-and-geohash-267727e5d54f
	

	class Position(object):
		def __init__(self, latitude: str, longitude: str):
		  self.latitude = latitude
		  self.longitude = longitude



class Canonization(object):
	def __init__(self, params):
		self.stage: str  # ["Servent of God", "Venerable", "Blessed", "Saint"]
		self.location: Location
		self.canonization_date: datetime
		self.celebrant: str
		self.date: datetime # yyyy-MM-dd HH:mm:ss


class Images(object):
	def __init__(self, params):
		self.name: str
		self.file: str

class Name(object):
	def __init__(self, params):
		#TODO  How do we compile this information into a readable formatted name? 
		self.type: str # Enum: "birth_name", "nickname", "vocation_name", "alternative_spelling"
		self.language: str # https://www.loc.gov/standards/iso639-2/php/code_list.php
		self.title: str # Optional, https://en.wikipedia.org/wiki/Hierarchy_of_the_Catholic_Church

		self.first: str
		self.middle: list # Optional: List of strings
		self.last: str # Either Optional, or have this be last name or location.
		self.suffix: str # Optional, Jr, Sr, II, III, etc.
		self.posthumous: str # Optional, Example: "The Great"


class Documents(object):
	# Just a list of ideas for documents
	# If translation is not from Vatican, have it listed as "Unofficial" translation.
		

# TODO, If a saint quotes scripture, it would be great to also have a bible that could reference what saints have talked about in these scriptures and what views they held and the time period in which they held these views... 
# This needs more thoughts and guidance from a priest, but this would enable users to see how saints / tradition held their views on these scriptures...