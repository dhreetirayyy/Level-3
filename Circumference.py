import math

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference
if __name__ == "__main__":
    while True:
        try:
            user_input = input("Enter the radius of the circle (or 'quit' to exit): ")

            if user_input.lower() == 'quit':
                print("Exiting the program.")
                break
            radius = float(user_input)
            if radius < 0:
                print("Radius cannot be negative. Please enter a non-negative number.")
                continue 

           
            calculated_circumference = calculate_circumference(radius)

            print(f"For a circle with radius {radius}, the circumference is: {calculated_circumference:.2f}")

        except ValueError:
            # Handle cases where the user input is not a valid number
            print("Invalid input. Please enter a numerical value for the radius.")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

