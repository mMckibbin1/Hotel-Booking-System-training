import sqlite3
from Events import Conference, Wedding, Party

dbconn = sqlite3.connect('Database\events.db')

##set up sqlite
def connect():
    db = dbconn
    cursor = db.cursor()
    ##Create a table if none exists
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS weddingTable(Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Guests INTEGER, Name TEXT, Address TEXT, Phone TEXT, Room TEXT, EventDate TEXT, BookingDate TEXT, Band TEXT, BandPrice INTEGER, Bedrooms REAL)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS partyTable(Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Guests INTEGER, Name TEXT, Address TEXT, Phone TEXT, Room TEXT, EventDate TEXT, BookingDate TEXT, Band TEXT, BandPrice INTEGER)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS conferenceTable(Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Guests INTEGER, Name TEXT, Address TEXT, Phone TEXT, Room TEXT, EventDate TEXT, BookingDate TEXT, CompanyName TEXT, Days INTEGER, ProjectRequired INTEGER)")
    db.commit()
    cursor.close()

def read_wedding_db():
    db = dbconn
    cursor = db.cursor()
    cursor.execute('SELECT * FROM weddingTable')
    list = []
    for row in cursor.fetchall():
        wedding = Wedding.Wedding(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[10], row[9], row[0])

        list.append(wedding)

    cursor.close()
    return list

def read_party_db():
    db = dbconn
    cursor = db.cursor()
    cursor.execute('SELECT * FROM partyTable')
    list = []
    for row in cursor.fetchall():
        party = Party.Party(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[0])

        list.append(party)

    cursor.close()
    return list

def read_conference_db():
    db = dbconn
    cursor = db.cursor()
    cursor.execute('SELECT * FROM conferenceTable')
    list = []
    for row in cursor.fetchall():
        conference = Conference.Conference(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[0])

        list.append(conference)

    cursor.close()
    return list


def read_all_from_db():
    list = []
    listdbWedding = []
    listdbParty = []
    listdbConference = []

    listdbWedding.append(read_wedding_db())
    listdbParty.append(read_party_db())
    listdbConference.append(read_conference_db())

    return listdbWedding + listdbParty + listdbConference


def insertwedding(wedding):
    conn = dbconn
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO weddingTable(Guests, Name, Address, Phone, Room, EventDate, BookingDate, Band, bandPrice, Bedrooms ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?,?)',
            (wedding.noGuests, wedding.nameOfContact, wedding.address, wedding.contactNo, wedding.eventRoomNo,
             wedding.dateOfEvent, wedding.dateOfBooking,
             wedding.bandName, wedding.bandPrice, wedding.noBedroomsReserved))
        conn.commit()
        cursor.close()



def insertParty(party):
    conn = dbconn
    with conn:
        cursor = conn.cursor()
        conn.execute(
            'INSERT INTO partyTable(Guests, Name, Address, Phone, Room, EventDate, BookingDate, Band, BandPrice) VALUES(?, ?, ?, ?, ?, ?, ?, ?,?)',
            (party.noGuests, party.nameOfContact, party.address, party.contactNo, party.eventRoomNo,
             party.dateOfEvent, party.dateOfBooking,
             party.bandName,party.bandPrice))

def insertConference(conference):
    conn = dbconn
    with conn:
        cursor = conn.cursor()
        cursor.execute(
        "INSERT INTO conferenceTable(Guests, Name, Address, Phone, Room, EventDate, BookingDate, CompanyName, Days, ProjectRequired) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?,?)",
        (
            conference.noGuests, conference.nameOfContact, conference.address, conference.contactNo, conference.eventRoomNo, conference.dateOfEvent, conference.dateOfBooking,
            conference.companyName, conference.noOfDays, conference.projectorRequired
        ))
        conn.commit()
        cursor.close()