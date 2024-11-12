import requests

APIkey="0916e4edf2e0dd2f5e96f27ff3eaae0d"

def get_data(place, days, kind):
    url= f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response = requests.get(url)
    data = response.json()
    filtered_data=data["list"][:days*8]
    if kind == "Temperature":
        return [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        return [dict["weather"][0]["main"] for dict in filtered_data]

if __name__=="__main__":
    print(get_data("Tokyo",2, "Temperature"))
    print(get_data("Tokyo", 2, "Sky"))



