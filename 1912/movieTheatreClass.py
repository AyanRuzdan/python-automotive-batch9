class MovieTicket:
    # Class-level set to track booked seats per movie
    booked_seats = set()  # stores tuples: (movie_name, seat_number)

    def __init__(self, movie_name, seat_number, price):
        self.movie_name = movie_name
        self.seat_number = seat_number
        self.price = price
        self.is_booked = False

    def book_ticket(self):
        try:
            ticket = (self.movie_name, self.seat_number)

            # Prevent double booking
            if ticket in MovieTicket.booked_seats:
                raise ValueError(
                    f"Seat {self.seat_number} for '{self.movie_name}' is already booked"
                )

            self.is_booked = True
            MovieTicket.booked_seats.add(ticket)
            print(f"Ticket booked successfully for seat {self.seat_number}")

        except ValueError as e:
            print("Booking error:", e)

    def cancel_ticket(self):
        try:
            ticket = (self.movie_name, self.seat_number)

            if not self.is_booked:
                raise ValueError("Ticket is not booked yet")

            self.is_booked = False
            MovieTicket.booked_seats.remove(ticket)
            print(f"Ticket for seat {self.seat_number} cancelled successfully")

        except ValueError as e:
            print("Cancellation error:", e)

    def display_ticket_details(self):
        print("-----TICKET DETAILS-----")
        print("Movie:", self.movie_name)
        print("Seat Number:", self.seat_number)
        print("Price:", self.price)
        print("Status:", "Booked" if self.is_booked else "Available")


# Test Case 1: Booking a ticket successfully
ticket1 = MovieTicket("Dhurandhar", "A10", 350)
ticket1.display_ticket_details()
ticket1.book_ticket()
ticket1.display_ticket_details()

# Test Case 2: Attempt double booking of same seat for same movie
ticket2 = MovieTicket("Dhurandhar", "A10", 350) 
ticket2.book_ticket()  # should raise error

# Test Case 3: Booking same seat but for a different movie (allowed)
ticket3 = MovieTicket("Thamma", "A10", 400)
ticket3.book_ticket()
ticket3.display_ticket_details()

# Test Case 4: Cancel ticket and rebook
ticket1.cancel_ticket()
ticket2.book_ticket()  # now should work
ticket2.display_ticket_details()
