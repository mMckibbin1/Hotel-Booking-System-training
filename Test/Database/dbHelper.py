import datetime
import sqlite3
from Events import Conference, Wedding, Party
import constances

dbconn = sqlite3.connect('Database\events.db')


##set up sqlite
def connect():
    db = dbconn
    cursor = db.cursor()
    ##Create a table if none exists
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS weddingTable(Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Guests INTEGER, Name TEXT, Address TEXT, Phone TEXT, Room TEXT, EventDate TEXT, BookingDate TEXT, Band TEXT, BandPrice INTEGER, Bedrooms INTEGER)")
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
        wedding = Wedding.Wedding(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[10], row[9],
                                  row[0])

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
        conference = Conference.Conference(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                           row[10], row[0])

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


##### Insert #####
# Wedding
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


# Party
def insertParty(party):
    conn = dbconn
    with conn:
        cursor = conn.cursor()
        conn.execute(
            'INSERT INTO partyTable(Guests, Name, Address, Phone, Room, EventDate, BookingDate, Band, BandPrice) VALUES(?, ?, ?, ?, ?, ?, ?, ?,?)',
            (party.noGuests, party.nameOfContact, party.address, party.contactNo, party.eventRoomNo,
             party.dateOfEvent, party.dateOfBooking,
             party.bandName, party.bandPrice))


# Conference
def insertConference(conference):
    conn = dbconn
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO conferenceTable(Guests, Name, Address, Phone, Room, EventDate, BookingDate, CompanyName, Days, ProjectRequired) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?,?)",
            (
                conference.noGuests, conference.nameOfContact, conference.address, conference.contactNo,
                conference.eventRoomNo, conference.dateOfEvent, conference.dateOfBooking,
                conference.companyName, conference.noOfDays, conference.projectorRequired
            ))
        conn.commit()
        cursor.close()


##### Delete #####
def deleteBooking(ID, Type):
    db = dbconn
    cursor = db.cursor()

    # global
    Table = None

    # if statement - checks the type of event
    if Type == "Wedding":
        # sets table to delete booking from
        Table = "weddingTable"
    elif Type == "Party":
        Table = "partyTable"
    elif Type == "Conference":
        Table = "conferenceTable"

    # deletes the booking from the table
    cursor.execute("DELETE FROM " + Table + " WHERE Id=" + str(ID))

    dbconn.commit()


###### Search #####
def search(EventsList, StartDate, EndDate):
    db = dbconn
    cursor = db.cursor()
    Date = None
    if StartDate != "" and EndDate != "":
        Date = " Where date(EventDate) between date('{}') and date('{}')".format(StartDate, EndDate)
    elif StartDate != "":
        Date = " Where date(EventDate) >= date('{}')".format(StartDate)
    elif EndDate != "":
        Date = " Where date(EventDate) =< date('{}')".format(EndDate)
    else:
        Date = ""

    weddinglist = []
    partylist = []
    conferencelist = []

    for string in EventsList:
        query = "select * from " + string + Date
        cursor.execute(query)
        if string == "weddingTable":
            for row in cursor.fetchall():
                wedding = Wedding.Wedding(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[10],
                                          row[9], row[0])
                weddinglist.append(wedding)
        if string == "conferenceTable":
            for row in cursor.fetchall():
                conference = Conference.Conference(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                                   row[9],
                                                   row[10], row[0])
                conferencelist.append(conference)
        if string == "partyTable":
            for row in cursor.fetchall():
                party = Party.Party(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[0])
                partylist.append(party)

    cursor.close()

    return weddinglist + partylist + conferencelist


##### Update #####
# Conference
def updateConference(conference):
    conn = dbconn
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE conferenceTable SET Guests=?, Name=?, Address=?, Phone=?, Room=?, EventDate=?, BookingDate=?, CompanyName=?, Days=?, ProjectRequired=?  WHERE ID=? ",
            (
                conference.noGuests, conference.nameOfContact, conference.address, conference.contactNo,
                conference.eventRoomNo, conference.dateOfEvent,
                conference.dateOfBooking, conference.companyName, conference.noOfDays, conference.projectorRequired,
                conference.ID
            ))
        conn.commit()
        cursor.close()


# Wedding
def updateWedding(wedding):
    conn = dbconn
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE weddingTable SET Guests=?, Name=?, Address=?, Phone=?, Room=?, EventDate=?, BookingDate=?, Band=?, bandPrice=?, Bedrooms=?  WHERE ID=? ",
            (
                wedding.noGuests, wedding.nameOfContact, wedding.address, wedding.contactNo, wedding.eventRoomNo,
                wedding.dateOfEvent, wedding.dateOfBooking,
                wedding.bandName, wedding.bandPrice, wedding.noBedroomsReserved, wedding.ID
            ))
        conn.commit()
        cursor.close()


# Party
def updateParty(party):
    conn = dbconn
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE partyTable SET Guests=?, Name=?, Address=?, Phone=?, Room=?, EventDate=?, BookingDate=?, Band=?, BandPrice=?  WHERE ID=? ",
            (
                party.noGuests, party.nameOfContact, party.address, party.contactNo, party.eventRoomNo,
                party.dateOfEvent, party.dateOfBooking, party.bandName, party.bandPrice, party.ID
            ))
        conn.commit()
        cursor.close()


##### Validation #####
def date_conflict(table_name, date, room):
    conn = dbconn
    cursor = conn.cursor()
    query = "SELECT * FROM {} WHERE date(EventDate) = date('{}') AND Room = '{}'".format(table_name, date, room)
    cursor.execute(query)

    if len(cursor.fetchall()) > 0:
        cursor.close()
        return True
    else:
        cursor.close()
        return False

def date_conflict_update(table_name, date, room,id):
    conn = dbconn
    cursor = conn.cursor()
    query = "SELECT * FROM {} WHERE date(EventDate) = date('{}') AND Room = '{}' AND Id != {}".format(table_name, date,
                                                                                                     room, id)
    cursor.execute(query)

    if len(cursor.fetchall()) > 0:
        cursor.close()
        return True
    else:
        cursor.close()
        return False


def con_date_conflict(table_name, start_date, duration, room):

    duration = int(duration) - 1
    date_1 = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = date_1 + datetime.timedelta(duration)
    conn = dbconn
    cursor = conn.cursor()
    cursor.execute("select *, date(EventDate, '+'||(Days - 1)||' days') as endDate from {} where endDate BETWEEN date('{}') and date('{}') and Room = '{}'".format(table_name, start_date, end_date, room))

    if len(cursor.fetchall()) > 0:
        cursor.close()
        return True
    else:
        cursor.close()
        return False


def con_date_conflict_update(table_name, start_date, duration, room, id):

    duration = int(duration) - 1
    date_1 = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = date_1 + datetime.timedelta(duration)
    conn = dbconn
    cursor = conn.cursor()
    cursor.execute("select *, date(EventDate, '+'||(Days - 1)||' days') as endDate from {} where endDate BETWEEN date('{}') and date('{}') and Room = '{}' and Id != {}".format(table_name, start_date, end_date, room,id))

    if len(cursor.fetchall()) > 0:
        cursor.close()
        return True
    else:
        cursor.close()
        return False


def rooms_in_use(event_type,date, number_of_days = 1):
    date_1 = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    conn = dbconn
    cursor = conn.cursor()

    wedding_party_query = "SELECT Room FROM {} WHERE date(EventDate) = date('{}')".format(event_type, date)

    conference_query = ("""select Room, date(EventDate, '+'||(Days - 1)||' days') as endDate 
            from conferenceTable where date(EventDate) BETWEEN date('{startDate}') and date('{endDate}') or
            endDate BETWEEN date('{startDate}') and date('{endDate}')""".format(startDate=date_1,
                                                                                endDate=date_1 + datetime.timedelta
                                                                                (days=number_of_days -1)))


    unavailable_rooms = []
    available_rooms = []
    #room_options = []


    if event_type == "weddingTable":
        room_options = constances.WEDDING_ROOM_OPTION
        cursor.execute(wedding_party_query)
    elif event_type == "partyTable":
        room_options = constances.PARTY_ROOM_OPTIONS
        cursor.execute(wedding_party_query)
    else:
        room_options = constances.CONFERENCE_ROOM_OPTIONS
        cursor.execute(conference_query)

    for row in cursor.fetchall():
        unavailable_rooms.append(row[0])

    for room in room_options:
        if room not in unavailable_rooms:
            available_rooms.append(room)

    cursor.close()
    return available_rooms