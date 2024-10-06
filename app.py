from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/ipinfo', methods=['GET'])
def get_ip_info():
    url = 'https://ipapi.co/json/'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        ipv4 = data.get('ip')
        ipv6 = data.get('ip') if ':' in data.get('ip') else None
        city = data.get('city')
        isp = data.get('org')
        asn = data.get('asn')
        geolocation = f"{data.get('latitude')}, {data.get('longitude')}"
        country_code = data.get('country_code')

        return jsonify({
            "ipv4": ipv4,
            "ipv6": ipv6,
            "city": city,
            "isp": isp,
            "asn": asn,
            "geolocation": geolocation,
            "country_code": country_code
        })
    
    except requests.RequestException as e:
        return jsonify({"error": f"Error fetching IP information: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
