import requests

APIkey="0916e4edf2e0dd2f5e96f27ff3eaae0d"

def get_data(place, days):
    url= f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response = requests.get(url)
    data = response.json()
    filtered_data=data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__=="__main__":
    print(get_data("Tokyo",2))



