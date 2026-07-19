class Car:
    """
    Car નામની Class
    Class એ Object બનાવવા માટેનું Blueprint (નમૂનો) છે.
    """

    # Constructor Method
    # જ્યારે નવું Object બનાવીએ ત્યારે આ Method આપમેળે ચાલે છે.
    def __init__(self, brand, model, year, color):

        # Object ના Attributes (ગુણધર્મો) Initialize કરીએ છીએ.
        self.brand = brand      # Car ની કંપની (Brand)
        self.model = model      # Car નો Model
        self.year = year        # Car નું Manufacturing Year
        self.color = color      # Car નો Color

        # શરૂઆતમાં Car બંધ હશે એટલે Engine Running નહીં હોય.
        self.is_running = False

    # ==========================
    # Engine Start કરવાનો Method
    # ==========================
    def start_engine(self):

        # જો Engine બંધ હોય તો જ Start કરવો.
        if not self.is_running:
            self.is_running = True   # Engine ચાલુ થયો.

            print(f"The engine of the {self.color} {self.brand} {self.model} has started. Vroom!")

        # જો પહેલાથી ચાલુ હોય તો Message બતાવવો.
        else:
            print(f"The engine of the {self.brand} is already running.")

    # ==========================
    # Engine Stop કરવાનો Method
    # ==========================
    def stop_engine(self):

        # જો Engine ચાલુ હોય તો જ બંધ કરવો.
        if self.is_running:
            self.is_running = False  # Engine બંધ થયો.

            print(f"The engine of the {self.brand} {self.model} has been turned off.")

        # જો પહેલાથી બંધ હોય તો Message બતાવવો.
        else:
            print(f"The engine of the {self.brand} is already off.")

    # ==========================
    # Car ની માહિતી બતાવવાનો Method
    # ==========================
    def display_info(self):

        print("\n--- Car Details ---")

        # Car ની માહિતી Print કરીએ છીએ.
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")

        # Ternary Operator
        # જો Engine ચાલુ હોય તો Running નહીં તો Stopped બતાવવું.
        status = "Running" if self.is_running else "Stopped"

        print(f"Status: {status}")

        print("-" * 19)


# ==========================
# Main Function
# Program અહીંથી શરૂ થશે.
# ==========================
def main():

    print("=== Python OOP Practical Demonstration ===")

    # Car ના બે અલગ અલગ Objects બનાવીએ છીએ.
    car1 = Car("Tesla", "Model S", 2024, "Red")
    car2 = Car("Ford", "Mustang", 1969, "Black")

    # ==========================
    # Car 1 સાથે કામ
    # ==========================
    print("\n[Interacting with Car 1]")

    car1.display_info()     # Car ની માહિતી બતાવો.
    car1.start_engine()     # Engine ચાલુ કરો.
    car1.display_info()     # ફરી માહિતી બતાવો.

    # ==========================
    # Car 2 સાથે કામ
    # ==========================
    print("\n[Interacting with Car 2]")

    car2.display_info()     # માહિતી બતાવો.
    car2.start_engine()     # Engine ચાલુ કરો.
    car2.stop_engine()      # Engine બંધ કરો.


# ==========================
# Program Entry Point
# જો આ File સીધી Run થાય તો main() Function ચાલશે.
# ==========================
if __name__ == "__main__":
    main()
