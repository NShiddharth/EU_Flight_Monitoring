import sqlite3

def create_database():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()

    # Create Airports table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Airports (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        iata_code TEXT UNIQUE NOT NULL,
                        icao_code TEXT UNIQUE NOT NULL,
                        country TEXT NOT NULL,
                        city TEXT NOT NULL,
                        latitude REAL NOT NULL,
                        longitude REAL NOT NULL)''')

    # Create Flights table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Flights (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        flight_number TEXT UNIQUE NOT NULL,
                        departure_airport TEXT NOT NULL,
                        arrival_airport TEXT NOT NULL,
                        departure_time TEXT NOT NULL,
                        arrival_time TEXT NOT NULL,
                        status TEXT NOT NULL,
                        delay_minutes INTEGER,
                        FOREIGN KEY (departure_airport) REFERENCES Airports(iata_code),
                        FOREIGN KEY (arrival_airport) REFERENCES Airports(iata_code))''')

    conn.commit()
    conn.close()
    print("Database and tables created successfully.")

if __name__ == "__main__":
    create_database()
