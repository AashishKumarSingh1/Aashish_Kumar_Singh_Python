class Vehicle:
    def __init__(self, vehicle_id, make, model, rental_rate):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.rental_rate = rental_rate
    
    def __str__(self):
        return f"{self.make} {self.model} (ID: {self.vehicle_id})"


class Car(Vehicle):
    def __init__(self, vehicle_id, make, model, rental_rate, num_doors, num_passengers):
        super().__init__(vehicle_id, make, model, rental_rate)
        self.num_doors = num_doors
        self.num_passengers = num_passengers


class Bike(Vehicle):
    def __init__(self, vehicle_id, make, model, rental_rate, bike_type):
        super().__init__(vehicle_id, make, model, rental_rate)
        self.bike_type = bike_type


class Rental:
    def __init__(self):
        self.rentals = []
    
    def check_availability(self, vehicle_id):
        for rental in self.rentals:
            if rental['vehicle'].vehicle_id == vehicle_id:
                return False
        return True
    
    def book_rental(self, vehicle, rental_period):
        if self.check_availability(vehicle.vehicle_id):
            total_cost = self.calculate_rental_cost(vehicle.rental_rate, rental_period)
            self.rentals.append({
                'vehicle': vehicle,
                'rental_period': rental_period,
                'total_cost': total_cost
            })
            return True
        else:
            return False
    
    def calculate_rental_cost(self, rental_rate, rental_period):
        return rental_rate * rental_period


if __name__ == "__main__":

    car1 = Car("C001", "Toyota", "Camry", 50.0, 4, 5)
    bike1 = Bike("B001", "Trek", "Mountain Bike", 20.0, "Mountain Bike")

    rental_manager = Rental()

    if rental_manager.book_rental(car1, 7):  # Rental period of 7 days
        print(f"Rental booked: {car1}")
    else:
        print(f"{car1} is not available for rental.")

    if rental_manager.book_rental(bike1, 3):  # Rental period of 3 days
        print(f"Rental booked: {bike1}")
    else:
        print(f"{bike1} is not available for rental.")

    print("\nCurrent Rentals:")
    for idx, rental in enumerate(rental_manager.rentals, start=1):
        print(f"Rental {idx}: {rental['vehicle']} | Rental Period: {rental['rental_period']} days | Total Cost: ${rental['total_cost']}")
