from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to EU Flight Monitoring API"}

@app.get("/flights")
def get_all_flights():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Flights")
    flights = cursor.fetchall()
    conn.close()
    return {"flights": flights}

@app.get("/real-time-flights")
def get_live_flights():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Flights WHERE status = 'In Air'")
    live_flights = cursor.fetchall()
    conn.close()
    return {"real_time_flights": live_flights}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
