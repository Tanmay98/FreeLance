import requests

def sw_vehicle_search(cargo_capacity, max_speed, cost):
    output = []
    url = 'https://swapi.dev/api/vehicles/'
    
    while(url != None):
        resp = requests.get(url)
        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))

        data = resp.json()
        vechiles_data = data["results"]
        for vech in vechiles_data:
            cargo_cap = vech["cargo_capacity"]
            speedofvech = vech["max_atmosphering_speed"]
            costofvech = vech["cost_in_credits"]
            if (cargo_cap != 'none' and cargo_cap != 'unknown'):
                cargo_cap = int(cargo_cap)
            if (speedofvech != 'none' and speedofvech != 'unknown'):
                speedofvech = int(speedofvech)
            if (costofvech != 'none' and costofvech != 'unknown'):
                costofvech = int(costofvech)
            

            if (cargo_capacity == cargo_cap and max_speed >= speedofvech and cost <= costofvech):
                output.append(str(vech["name"]))
        
        url = data["next"]
    return output


def starship_piloted_species(starship: str):
	#this is similar to above, follow the same steps like above

def cat_language(breed, language):
    url = 'https://api.thecatapi.com/v1/breeds/search?q='+str(breed)
    resp = requests.get(url)
    if resp.status_code != 200:
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))

    data = resp.json()
    country_origin = data[0]["origin"]
    
    url2 = 'https://restcountries.eu/rest/v2/name/'+str(country_origin)
    resp2 = requests.get(url2)
    if resp2.status_code != 200:
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    
    data2 = resp2.json()
    lang_code = data2[0]["languages"][0]["iso639_1"]
    
    if language == lang_code:
        return True
    else: return False

