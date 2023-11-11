import requests
from pyfiglet import Figlet
import folium

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        #print(response)
        data = {
            '[IP]': response.get('query', 'N/A'),
            '[Country]': response.get('country', 'N/A'),
            '[Region Name]': response.get('regionName', 'N/A'),
            '[Region Code]': response.get('regionCode', 'N/A'),
            '[City]': response.get('city', 'N/A'),
            '[Zip Code]': response.get('zip', 'N/A'),
            '[Lat]': response.get('lat', 'N/A'),
            '[Lon]': response.get('lon', 'N/A'),
            '[Timezone]': response.get('timezone', 'N/A'),
            '[ISP]': response.get('isp', 'N/A'),
            '[Org]': response.get('org', 'N/A'),
            '[AS]': response.get('as', 'N/A'),
            '[AS Name]': response.get('asname', 'N/A'),
            '[Hostname]': response.get('hostname', 'N/A'),
        }
        for key, value in data.items():
            print(f'{key}: {value}')

            area = folium.Map(location=[response.get('lat'), response.get('lon')], zoom_start=10)
            area.save(f'{response.get("query", "N/A")}_{response.get("city", "N/A")}.html')

    except requests.exceptions.ConnectionError:
        print('Connection Error')

def main():
    previous = Figlet(font='slant')
    print(previous.renderText('IP Location'))
    ip = input('Enter IP: ')
    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()