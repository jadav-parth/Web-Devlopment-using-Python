class Car:
    """
    A class representing a Car. 
    This acts as a blueprint for creating individual car objects.
    """
    
    # The Constructor method initializes the attributes
    def __init__(self, brand, model, year, color):
        self.brand = brand        # Attribute: Brand of the car
        self.model = model        # Attribute: Model of the car
        self.year = year          # Attribute: Year of manufacture
        self.color = color        # Attribute: Color of the car
        self.is_running = False   # Attribute: Track if the car is turned on
        
    def start_engine(self):
        """Method to start the car engine."""
        if not self.is_running:
            self.is_running = True
            print(f"The engine of the {self.color} {self.brand} {self.model} has started. Vroom!")
        else:
            print(f"The engine of the {self.brand} is already running.")
            
    def stop_engine(self):
        """Method to stop the car engine."""
        if self.is_running:
            self.is_running = False
            print(f"The engine of the {self.brand} {self.model} has been turned off.")
        else:
            print(f"The engine of the {self.brand} is already off.")
            
    def display_info(self):
        """Method to display full details of the car."""
        print(f"\n--- Car Details ---")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year:  {self.year}")
        print(f"Color: {self.color}")
        status = "Running" if self.is_running else "Stopped"
        print(f"Status: {status}")
        print("-" * 19)


def main():
    print("=== Python OOP Practical Demonstration ===")
    
    car1 = Car("Tesla", "Model S", 2024, "Red")
    
    car2 = Car("Ford", "Mustang", 1969, "Black")
    
    print("\n[Interacting with Car 1]")
    car1.display_info()     # Accessing method
    car1.start_engine()     # Changing state via method
    car1.display_info()     # Showing updated state
    
    print("\n[Interacting with Car 2]")
    car2.display_info()
    car2.start_engine()
    car2.stop_engine()

if __name__ == "__main__":
    main()