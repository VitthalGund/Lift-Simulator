class Lift:
    def __init__(self, total_floors):
        # Initialize a Lift object with its current floor, state, and total number of floors in the building
        self.current_floor = 0
        self.state = "CLOSE"
        self.total_floors = total_floors

    def move(self, destination_floor):
        # Move the lift to the destination floor
        if self.current_floor < destination_floor:
            # If the destination is above the current floor, move up
            self.state = "CLOSE"
            self.current_floor = destination_floor
        elif self.current_floor > destination_floor:
            # If the destination is below the current floor, move down
            self.state = "CLOSE"
            self.current_floor = destination_floor
        else:
            # If the lift is already at the destination floor, open the door
            self.state = "OPEN"

class LiftController:
    def __init__(self, num_lifts, num_floors):
        # Initialize a LiftController object with the given number of lifts and floors in the building
        self.lifts = [Lift(num_floors) for _ in range(num_lifts)]

    def process_request(self, starting_floor, destination_floor):
        # Process a lift request and return the time taken for the lift to reach the destination
        best_lift = None
        best_time = float('inf')

        # Find the best lift to handle the request based on the shortest time to reach the destination
        for lift in self.lifts:
            if lift.state == "CLOSE":
                time = abs(lift.current_floor - starting_floor) + abs(starting_floor - destination_floor) + 2
                if time < best_time:
                    best_time = time
                    best_lift = lift

        # If a suitable lift is found, move it to the destination floor and return the time taken
        if best_lift:
            best_lift.move(destination_floor)
            return best_time
        else:
            # If no lift is available, return None
            return None

def print_status(time, lifts):
    # Print the status of all lifts at the current time
    print("Time =", time)
    for i, lift in enumerate(lifts):
        print(f"LIFT {i+1} -- > {lift.current_floor} ({lift.state})")

def main():
    # Main function to run the lift simulation
    num_lifts = int(input("Enter the number of lifts: "))
    num_floors = int(input("Enter the number of floors: "))
    controller = LiftController(num_lifts, num_floors)

    print("Enter requests in the format 'starting_floor,destination_floor', or 'q' to quit: ")
    time = 0
    while True:
        # Display the current status and prompt for input
        print_status(time, controller.lifts)
        request = input("Enter request (starting_floor, destination_floor): ").strip()
        if request.lower() == 'q':
            # Quit the program if 'q' is entered
            break
        try:
            # Process the lift request
            starting_floor, destination_floor = map(int, request.split(','))
            if starting_floor < 0 or starting_floor >= num_floors or destination_floor < 0 or destination_floor >= num_floors:
                print("Invalid floor number. Please enter a valid floor number.")
                continue
            time_taken = controller.process_request(starting_floor, destination_floor)
            if time_taken:
                # Print the time taken for the lift to reach the destination
                print(f"LIFT will take {time_taken} seconds to reach the destination.")
            else:
                # If no lift is available, display a message
                print("All lifts are busy at the moment. Please try again later.")
        except ValueError:
            # Handle invalid input
            print("Invalid input. Please enter starting and destination floors separated by comma.")

        time += 1

if __name__ == "__main__":
    main()
