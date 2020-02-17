from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
	"""Zwraca stosowany przez Pygal dwuznakowy kod przypisany do danego państwa."""
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
	#Jeżeli państwo nie zostało znalezione, wartością zwrotną będzie None.
	return None

