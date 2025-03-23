import sqlite3

def insert_sample_data():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()

    # Insert German Airports
    airports = [
        ("Frankfurt Airport", "FRA", "EDDF", "Germany", "Frankfurt", 50.033333, 8.570556),
        ("Munich Airport", "MUC", "EDDM", "Germany", "Munich", 48.353889, 11.786111),
        ("Berlin Brandenburg Airport", "BER", "EDDB", "Germany", "Berlin", 52.366667, 13.503333),
        ("Hamburg Airport", "HAM", "EDDH", "Germany", "Hamburg", 53.630389, 9.988228),
        ("Düsseldorf Airport", "DUS", "EDDL", "Germany", "Düsseldorf", 51.289444, 6.766667),
    ]

    cursor.executemany("INSERT INTO Airports (name, iata_code, icao_code, country, city, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?)", airports)

    # Insert Sample Flights (some with delays)
    flights = [
        ("LH123", "FRA", "MUC", "2025-03-23 08:00:00", "2025-03-23 09:00:00", "On Time", 0),
        ("LH456", "MUC", "BER", "2025-03-23 10:00:00", "2025-03-23 11:30:00", "Delayed", 90),
        ("LH789", "BER", "HAM", "2025-03-23 12:00:00", "2025-03-23 13:00:00", "On Time", 0),
        ("LH101", "HAM", "DUS", "2025-03-23 14:00:00", "2025-03-23 15:15:00", "Delayed", 75),
        ("LH202", "DUS", "FRA", "2025-03-23 16:00:00", "2025-03-23 17:00:00", "On Time", 0),
        ("LH303", "MUC", "FRA", "2025-03-23 18:00:00", "2025-03-23 19:00:00", "On Time", 0),
        ("LH404", "BER", "MUC", "2025-03-23 20:00:00", "2025-03-23 21:00:00", "Delayed", 120),
        ("LH505", "HAM", "BER", "2025-03-23 22:00:00", "2025-03-23 23:30:00", "On Time", 0),
        ("LH606", "DUS", "MUC", "2025-03-23 06:00:00", "2025-03-23 07:15:00", "On Time", 0),
        ("LH707", "FRA", "HAM", "2025-03-23 08:30:00", "2025-03-23 09:45:00", "Delayed", 135),
    ]

    cursor.executemany("INSERT INTO Flights (flight_number, departure_airport, arrival_airport, departure_time, arrival_time, status, delay_minutes) VALUES (?, ?, ?, ?, ?, ?, ?)", flights)

    conn.commit()
    conn.close()
    print("Sample data inserted successfully.")

if __name__ == "__main__":
    insert_sample_data()
