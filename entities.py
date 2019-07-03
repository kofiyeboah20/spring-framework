class UserTrip:

    def __init__(self, set_off_place, set_off_time, destination, luggage, number_of_travelers):
        self.set_off_place = set_off_place
        self.set_off_time = set_off_time
        self.destination = destination
        self.luggage = luggage
        self.number_of_travelers = number_of_travelers


class Ticket:

    def __init__(self, ticket_name, bus_id, user_trip):
        self.ticket_name = ticket_name
        self.bus_id = bus_id
        self.user_trip = user_trip


class Bus:

    def __init__(self, number_of_seats, number_plate, agency, journey):
        self.number_of_seats = number_of_seats
        self.number_plate = number_plate
        self.agency = agency
        self.journey = journey


class BusAgency:

    def __init__(self, name, contact_address):
        self.name = name
        self.contact_address = phone_number


class Journey:
    
    def __init__(self, station, set_off_point, destination, set_off_time, journey_hours, allow_luggage, bus_stops, price, trip_completed):
        self.station = station_name
        self.set_off_point = journey_start_point
        self.destination = destination
        self.set_off_time = journey_start_time
        self.journey_hours = journey_time
        self.allow_luggage = allow_luggage
        self.bus_stops = bus_stops
        self.price = price
        self.trip_completed = trip_completed


class Bus_Stop:

	def __init__(self, name, location):
		self.name = name
		self.location = location
