import sqlite3

def get_flights_by_airport(iata_code):
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Flights WHERE departure_airport = ?", (iata_code,))
    flights = cursor.fetchall()
    conn.close()
    return flights

def get_delayed_flights():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Flights WHERE delay_minutes > 120")
    delayed_flights = cursor.fetchall()
    conn.close()
    return delayed_flights

def get_flight_by_number(flight_number):
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Flights WHERE flight_number = ?", (flight_number,))
    flight = cursor.fetchone()
    conn.close()
    return flight

if __name__ == "__main__":
    print("Flights from Frankfurt (FRA):", get_flights_by_airport("FRA"))
    print("Flights delayed over 2 hours:", get_delayed_flights())
    print("Details of flight LH404:", get_flight_by_number("LH404"))
