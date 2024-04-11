# 🏢 Lift Simulator

Lift Simulator is a Python program that simulates the operation of lifts in a building. 🛗 It allows users to input lift requests and observes how the lifts move to fulfill those requests over time. 🕰️

## 🚀 Features

- Simulates the movement of multiple lifts in a building with multiple floors.
- Handles lift requests from users and moves lifts accordingly.
- Provides a user-friendly interface for inputting lift requests and viewing the status of lifts.

## 📝 Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/VitthalGund/Lift-Simulator.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd lift-simulator
    ```

3. **Run the program:**

    ```bash
    python main.py
    ```

4. **Follow the on-screen prompts to input lift requests.**

## 📋 Input Format

- Enter the number of lifts and the number of floors in the building.
- Enter lift requests in the format `starting_floor,destination_floor`.
- Type `q` to quit the program.

## 💡 Example

```plaintext
Enter the number of lifts: 2
Enter the number of floors: 10

Time = 0
LIFT 1 -- > 0 (OPEN), LIFT 2 -- > 0 (CLOSE)

Enter request (starting_floor, destination_floor): 0,7
LIFT will take 9 seconds to reach the destination.

Time = 1
LIFT 1 -- > 0 (CLOSE), LIFT 2 -- > 1 (CLOSE)

Enter request (starting_floor, destination_floor): 3,0
LIFT will take 8 seconds to reach the destination.

Time = 2
LIFT 1 -- > 1 (CLOSE), LIFT 2 -- > 2 (CLOSE)

Enter request (starting_floor, destination_floor): 4,6
LIFT will take 1 seconds to reach the destination.

Time = 3
LIFT 1 -- > 2 (CLOSE), LIFT 2 -- > 3 (OPEN)

Enter request (starting_floor, destination_floor): q
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
