import requests
import sqlite3

# OpenSky API URL for real-time flight data
API_URL = "https://opensky-network.org/api/states/all"

def fetch_flight_data():
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()
        flights = data.get("states", [])  # Extract flights

        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()

        for flight in flights[:20]:  # Fetch only first 20 for simplicity
            callsign = flight[1]  # Flight number
            origin_country = flight[2]
            longitude = flight[5]
            latitude = flight[6]
            velocity = flight[9]

            if callsign and latitude and longitude:
                cursor.execute("INSERT OR IGNORE INTO Flights (flight_number, departure_airport, arrival_airport, departure_time, arrival_time, status, delay_minutes) VALUES (?, ?, ?, ?, ?, ?, ?)",
                               (callsign, "UNKNOWN", "UNKNOWN", "N/A", "N/A", "In Air", 0))

        conn.commit()
        conn.close()
        print("Real-time flight data fetched successfully.")

    else:
        print("Failed to fetch flight data:", response.status_code)

if __name__ == "__main__":
    fetch_flight_data()
