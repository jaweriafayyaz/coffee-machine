"""
GCU Coffee Machine Simulator
============================
A comprehensive coffee machine simulation built using Object-Oriented Programming principles.
This project demonstrates encapsulation, composition, and state management in Python.
"""

import time
class Drink:
    """
    Represents a coffee drink with its ingredients and pricing.
    
    This class encapsulates all drink-related data including required resources
    and cost information. It serves as a blueprint for different coffee types.
    """
    
    def __init__(self, name, water, milk, coffee, cost):
        """
        Initialize a new drink object.
        
        Args:
            name (str): The name of the drink (e.g., 'Espresso', 'Latte')
            water (int): Amount of water required in milliliters
            milk (int): Amount of milk required in milliliters  
            coffee (int): Amount of coffee required in grams
            cost (int): Price of the drink in Pakistani Rupees
        """
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost


class Order:
    """
    Represents a customer order with transaction details.
    
    This class captures order information for record-keeping and history tracking.
    Each order contains drink details, payment amount, and timestamp.
    """
    
    def __init__(self, drink_name, amount_paid):
        """
        Initialize a new order record.
        
        Args:
            drink_name (str): Name of the ordered drink
            amount_paid (int): Amount paid by customer
        """
        self.drink_name = drink_name
        self.amount_paid = amount_paid
        # Generate timestamp in DD-MM-YYYY HH:MM:SS format
        self.timestamp = time.strftime("%d-%m-%Y %H:%M:%S")


class CoffeeMachine:
    """
    Main coffee machine class that manages resources, orders, and user interactions.
    
    This class implements the core business logic of the coffee machine including:
    - Resource management (water, milk, coffee)
    - Menu management with drink options
    - Order processing and payment handling
    - Sales tracking and reporting
    - User interface and interaction flow
    """
    
    def __init__(self):
        """
        Initialize the coffee machine with default resources and menu.
        
        Sets up initial inventory levels, creates drink menu, and initializes
        tracking variables for sales and order history.
        """
        # Initial resource levels - can be refilled by maintenance
        self.resources = {
            'water': 1000,     # in milliliters
            'milk': 800,       # in milliliters  
            'coffee': 300      # in grams
        }
        
        # Menu dictionary containing all available drinks
        # Each drink is instantiated with specific resource requirements
        self.menu = {
            'espresso': Drink('Espresso', 50, 0, 18, 100),        # Strong, no milk
            'latte': Drink('Latte', 200, 150, 24, 200),           # Milky, smooth
            'cappuccino': Drink('Cappuccino', 250, 100, 24, 250)  # Balanced, foamy
        }
        
        # Financial tracking
        self.money_collected = 0  # Total revenue in Pakistani Rupees
        
        # Order history for customer service and analytics
        self.orders = []  # List to store Order objects

    def print_report(self):
        """
        Display comprehensive machine status report for administrators.
        
        Shows current resource levels, total sales, and order statistics.
        This method is protected by password authentication for security.
        """
        print("\n📊 GCU Coffee Machine Report:")
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml") 
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Total Sales: Rs {self.money_collected}")
        print("🧾 Total Orders:", len(self.orders))
        print()

    def check_resources(self, drink):
        """
        Verify if sufficient resources are available to make the requested drink.
        
        Args:
            drink (Drink): The drink object to check resources for
            
        Returns:
            bool: True if resources are sufficient, False otherwise
            
        This method implements resource validation logic and provides
        user-friendly error messages for insufficient ingredients.
        """
        # Check each resource requirement against current availability
        if self.resources['water'] < drink.water:
            print("❌ Not enough water.")
            return False
        if self.resources['milk'] < drink.milk:
            print("❌ Not enough milk.")
            return False
        if self.resources['coffee'] < drink.coffee:
            print("❌ Not enough coffee.")
            return False
        return True

    def make_drink(self, drink):
        """
        Process drink creation by updating resources and recording the transaction.
        
        Args:
            drink (Drink): The drink object to prepare
            
        This method handles the actual drink preparation process:
        1. Deducts required resources from inventory
        2. Records payment in sales tracking
        3. Creates order record for history
        4. Provides confirmation to customer
        """
        # Deduct resources used in drink preparation
        self.resources['water'] -= drink.water
        self.resources['milk'] -= drink.milk
        self.resources['coffee'] -= drink.coffee
        
        # Update financial records
        self.money_collected += drink.cost
        
        # Create and store order record for tracking
        self.orders.append(Order(drink.name, drink.cost))
        
        # Provide customer confirmation with friendly message
        print(f"✅ Here's your {drink.name}! Enjoy ☕\n")

    def show_order_history(self):
        """
        Display recent order history for customer reference.
        
        Shows the last 5 orders with timestamps and details.
        Helps customers track their purchases and assists with customer service.
        """
        # Handle empty order history gracefully
        if not self.orders:
            print("📭 No orders placed yet.\n")
            return
            
        print("📜 Order History (Last 5 orders):")
        # Display only the most recent 5 orders using list slicing
        for order in self.orders[-5:]:
            print(f"{order.timestamp} - {order.drink_name} - Rs {order.amount_paid}")
        print()

    def run(self):
        """
        Main application loop that handles user interactions.
        
        This method implements the primary user interface and control flow:
        - Displays welcome message and menu options
        - Processes user input and routes to appropriate functions
        - Handles payment processing with change calculation
        - Provides comprehensive error handling and input validation
        - Manages application lifecycle (start/exit)
        """
        print("👋 Welcome to GCU Coffee Machine!\n")
        
        # Main interaction loop - continues until user exits
        while True:
            # Get user choice with clear instructions
            choice = input("Enter drink name (espresso/latte/cappuccino), 'report', 'history', or 'exit': ").lower()

            # Handle application exit
            if choice == 'exit':
                print("👋 Thank you for visiting GCU Coffee Machine!")
                break
                
            # Handle admin report access with security
            elif choice == 'report':
                password = input("🔐 Enter admin password: ")
                # Simple password authentication (in production, use hashed passwords)
                if password == "gcuadmin":
                    self.print_report()
                else:
                    print("❌ Access denied.\n")
                    
            # Handle order history display
            elif choice == 'history':
                self.show_order_history()
                
            # Handle drink orders
            elif choice in self.menu:
                drink = self.menu[choice]  # Get drink object from menu
                
                # Verify sufficient resources before processing order
                if self.check_resources(drink):
                    print(f"💰 Please pay Rs {drink.cost}")
                    
                    # Payment processing with error handling
                    try:
                        amount = int(input("Enter amount: Rs "))
                    except ValueError:
                        # Handle non-numeric input gracefully
                        print("❌ Invalid input. Please enter a number.\n")
                        continue
                    
                    # Process payment and calculate change
                    if amount >= drink.cost:
                        change = amount - drink.cost
                        
                        # Return change if overpaid
                        if change > 0:
                            print(f"💸 Here is your change: Rs {change}")
                            
                        # Complete the order
                        self.make_drink(drink)
                    else:
                        # Handle insufficient payment
                        print("❌ Not enough money. Money refunded.\n")
                        
            # Handle invalid menu options
            else:
                print("⚠️ Invalid option. Try again.\n")


# Application entry point - ensures code runs only when script is executed directly
if __name__ == "__main__":
    # Create coffee machine instance and start the application
    machine = CoffeeMachine()
    machine.run()