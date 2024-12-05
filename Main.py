class Park:
    """
    Represents a Park containing multiple rides and other features.

    Attributes:
        name (str): The name of the park.
        location (str): The location of the park.
        operating_hours (str): The operating hours of the park.
        current_visitors (int): The number of visitors currently in the park.
        attractions (list): List of general attractions.
        events (list): List of ongoing events.
        services (list): List of services offered.
        ride_list (list[Ride]): List of rides in the park (composition relationship).
    """

    def __init__(self, name, location, operating_hours, current_visitors, attractions=None, events=None, services=None):
        """
        Initializes a new Park object.

        Args:
            name (str): Name of the park.
            location (str): Location of the park.
            operating_hours (str): Operating hours of the park.
            current_visitors (int): Current number of visitors in the park.
            attractions (list): Optional list of attractions.
            events (list): Optional list of events.
            services (list): Optional list of services.
        """
        self.__name = name
        self.__location = location
        self.__operating_hours = operating_hours
        self.__current_visitors = current_visitors
        self.__attractions = attractions if attractions else []
        self.__events = events if events else []
        self.__services = services if services else []
        self.__ride_list = []  # Composition: List of Ride objects

    # Setters
    def set_name(self, name: str):
        self.__name = name

    def set_location(self, location: str):
        self.__location = location

    def set_operating_hours(self, operating_hours: str):
        self.__operating_hours = operating_hours

    def set_current_visitors(self, current_visitors: int):
        self.__current_visitors = current_visitors

    def set_attractions(self, attractions: list):
        self.__attractions = attractions

    def set_events(self, events: list):
        self.__events = events

    def set_services(self, services: list):
        self.__services = services

    # Getters
    def get_name(self) -> str:
        return self.__name

    def get_location(self) -> str:
        return self.__location

    def get_operating_hours(self) -> str:
        return self.__operating_hours

    def get_current_visitors(self) -> int:
        return self.__current_visitors

    def get_attractions(self) -> list:
        return self.__attractions

    def get_events(self) -> list:
        return self.__events

    def get_services(self) -> list:
        return self.__services

    def get_ride_list(self) -> list:
        return self.__ride_list

    # Relationship Management
    def add_ride(self, ride):
        """
        Adds a Ride object to the park's ride list.
        """
        self.__ride_list.append(ride)

    def remove_ride(self, ride):
        """
        Removes a Ride object from the park's ride list.
        """
        if ride in self.__ride_list:
            self.__ride_list.remove(ride)

    # Operational Methods
    def check_capacity(self) -> int:
        """
        Calculates the total capacity of all rides in the park.
        Returns:
            int: Total capacity of all rides.
        """
        return sum(ride.get_capacity() for ride in self.__ride_list)

    def update_operating_hours(self, hours: str):
        """
        Updates the operating hours of the park.

        Args:
            hours (str): New operating hours for the park.
        """
        self.__operating_hours = hours


class Ride:
    """
    Represents a Ride within the park.

    Attributes:
        name (str): The name of the ride.
        type (str): The type of ride (e.g., Thrill, Family).
        min_height (str): Minimum height required to ride.
        max_height (str): Maximum height allowed on the ride.
        duration (str): Duration of the ride.
        capacity (int): Maximum capacity of the ride.
        status (str): Current operational status of the ride (e.g., Open, Closed).
        active_tickets (list[Ticket]): List of active tickets for the ride.
    """

    def __init__(self, name, ride_type, min_height, max_height, duration, capacity, status):
        """
        Initializes a new Ride object.

        Args:
            name (str): The name of the ride.
            ride_type (str): The type of ride (e.g., Thrill, Family).
            min_height (str): Minimum height required for the ride.
            max_height (str): Maximum height allowed for the ride.
            duration (str): Duration of the ride.
            capacity (int): Maximum capacity of the ride.
            status (str): The current status of the ride (e.g., Open, Closed).
        """
        self.__name = name
        self.__type = ride_type
        self.__min_height = min_height
        self.__max_height = max_height
        self.__duration = duration
        self.__capacity = capacity
        self.__status = status
        self.__active_tickets = []  # List of associated Ticket objects

    # Setters
    def set_name(self, name: str):
        self.__name = name

    def set_type(self, ride_type: str):
        self.__type = ride_type

    def set_min_height(self, min_height: str):
        self.__min_height = min_height

    def set_max_height(self, max_height: str):
        self.__max_height = max_height

    def set_duration(self, duration: str):
        self.__duration = duration

    def set_capacity(self, capacity: int):
        self.__capacity = capacity

    def set_status(self, status: str):
        self.__status = status

    # Getters
    def get_name(self) -> str:
        return self.__name

    def get_type(self) -> str:
        return self.__type

    def get_min_height(self) -> str:
        return self.__min_height

    def get_max_height(self) -> str:
        return self.__max_height

    def get_duration(self) -> str:
        return self.__duration

    def get_capacity(self) -> int:
        return self.__capacity

    def get_status(self) -> str:
        return self.__status

    def get_active_tickets(self) -> list:
        return self.__active_tickets

    # Behavioral Methods
    def check_status(self) -> str:
        """
        Returns the current operational status of the ride.
        """
        return f"The current status of the ride '{self.__name}' is: {self.__status}."

    def add_active_ticket(self, ticket):
        """
        Adds a Ticket object to the active tickets list.

        Args:
            ticket (Ticket): The ticket to be added.
        """
        self.__active_tickets.append(ticket)

    def reset_ride(self) -> str:
        """
        Resets the ride by clearing active tickets and setting the status to 'Closed'.
        """
        self.__active_tickets.clear()
        self.__status = "Closed"
        return f"The ride '{self.__name}' has been reset. All active tickets are cleared, and the status is now 'Closed'."


class Ticket:
        """
        Represents a Ticket for a specific ride or park admission.

        Attributes:
            ticket_type (str): The type of ticket (e.g., VIP, Regular).
            description (str): A description of the ticket.
            price (float): The price of the ticket.
            validity (str): The validity of the ticket (e.g., "1 day").
            discount (float): Discount applied to the ticket price (percentage).
            limitations (str): Any limitations associated with the ticket.
            visit_date (str): The date the ticket is valid for (e.g., "YYYY-MM-DD").
        """

        def __init__(self, ticket_type, description, price, validity, discount, limitations, visit_date):
            """
            Initializes a new Ticket object.

            Args:
                ticket_type (str): The type of ticket (e.g., VIP, Regular).
                description (str): A description of the ticket.
                price (float): The price of the ticket.
                validity (str): The validity of the ticket.
                discount (float): Discount applied to the price.
                limitations (str): Limitations associated with the ticket.
                visit_date (str): The valid date for the ticket.
            """
            self.__ticket_type = ticket_type
            self.__description = description
            self.__price = float(price)
            self.__validity = validity
            self.__discount = float(discount)
            self.__limitations = limitations
            self.__visit_date = visit_date

        # Setters
        def set_ticket_type(self, ticket_type: str):
            self.__ticket_type = ticket_type

        def set_description(self, description: str):
            self.__description = description

        def set_price(self, price: float):
            self.__price = price

        def set_validity(self, validity: str):
            self.__validity = validity

        def set_discount(self, discount: float):
            self.__discount = discount

        def set_limitations(self, limitations: str):
            self.__limitations = limitations

        def set_visit_date(self, visit_date: str):
            self.__visit_date = visit_date

        # Getters
        def get_ticket_type(self) -> str:
            return self.__ticket_type

        def get_description(self) -> str:
            return self.__description

        def get_price(self) -> float:
            return self.__price

        def get_validity(self) -> str:
            return self.__validity

        def get_discount(self) -> float:
            return self.__discount

        def get_limitations(self) -> str:
            return self.__limitations

        def get_visit_date(self) -> str:
            return self.__visit_date

        # Behavioral Methods
        def apply_discount(self) -> float:
            """
            Applies the discount to the ticket price.
            Returns the new price after applying the discount.
            """
            self.__price = self.__price - (self.__price * self.__discount / 100)
            return round(self.__price, 2)

        def describe_ticket(self) -> str:
            """
            Returns a detailed description of the ticket.
            """
            return (
                f"Ticket Type: {self.__ticket_type}\n"
                f"Description: {self.__description}\n"
                f"Price: ${self.__price:.2f}\n"
                f"Discount: {self.__discount}%\n"
                f"Validity: {self.__validity}\n"
                f"Limitations: {self.__limitations}\n"
                f"Visit Date: {self.__visit_date}"
            )

class Order:
    """
    Represents an Order containing tickets purchased by a customer.

    Attributes:
        customer (Customer): The customer who placed the order.
        ticket_list (list[Ticket]): List of Ticket objects in the order.
        quantity (int): Number of tickets in the order.
        total_price (float): Total price of the order.
        amount_paid (float): The amount paid by the customer.
        payment_type (str): Payment type (e.g., "CARD", "CASH").
        order_date (str): Date when the order was placed.
        order_id (str): Unique identifier for the order.
    """

    def __init__(self, customer, ticket_list, quantity, total_price, amount_paid, payment_type, order_date, order_id):
        """
        Initializes a new Order object.

        Args:
            customer (Customer): The customer who placed the order.
            ticket_list (list[Ticket]): List of tickets in the order.
            quantity (int): Number of tickets in the order.
            total_price (float): Total price of the order.
            amount_paid (float): Amount paid by the customer.
            payment_type (str): Payment method used for the order.
            order_date (str): Date of the order.
            order_id (str): Unique identifier for the order.
        """
        self.__customer = customer
        self.__ticket_list = ticket_list
        self.__quantity = quantity
        self.__total_price = total_price
        self.__amount_paid = amount_paid
        self.__payment_type = payment_type
        self.__order_date = order_date
        self.__order_id = order_id

    # Setters
    def set_customer(self, customer):
        self.__customer = customer

    def set_ticket_list(self, ticket_list: list):
        self.__ticket_list = ticket_list

    def set_quantity(self, quantity: int):
        self.__quantity = quantity

    def set_total_price(self, total_price: float):
        self.__total_price = total_price

    def set_amount_paid(self, amount_paid: float):
        self.__amount_paid = amount_paid

    def set_payment_type(self, payment_type: str):
        self.__payment_type = payment_type

    def set_order_date(self, order_date: str):
        self.__order_date = order_date

    def set_order_id(self, order_id: str):
        self.__order_id = order_id

    # Getters
    def get_customer(self):
        return self.__customer

    def get_ticket_list(self) -> list:
        return self.__ticket_list

    def get_quantity(self) -> int:
        return self.__quantity

    def get_total_price(self) -> float:
        return self.__total_price

    def get_amount_paid(self) -> float:
        return self.__amount_paid

    def get_payment_type(self) -> str:
        return self.__payment_type

    def get_order_date(self) -> str:
        return self.__order_date

    def get_order_id(self) -> str:
        return self.__order_id

    # Behavioral Methods
    def calculate_total_price(self) -> float:
        """
        Calculates the total price of all tickets in the order.
        """
        self._total_price = sum(ticket.get_price() for ticket in self.get_ticket_list())
        return round(self.__total_price, 2)

    def get_order_summary(self) -> str:
        """
        Generates a summary of the order details.
        """
        ticket_details = "\n".join([ticket.describe_ticket() for ticket in self.__ticket_list])
        return (
            f"Order ID: {self.__order_id}\n"
            f"Customer: {self.__customer.get_name()}\n"
            f"Order Date: {self.__order_date}\n"
            f"Payment Type: {self.__payment_type}\n"
            f"Quantity: {self.__quantity}\n"
            f"Total Price: ${self.__total_price:.2f}\n"
            f"Amount Paid: ${self.__amount_paid:.2f}\n"
            f"Tickets:\n{ticket_details}"
        )


class Account:
    """
    Represents a base Account for the system.

    Attributes:
        username (str): The username for the account.
        password (str): The password for the account.
        email (str): The email address associated with the account.
        age (str): The age of the account holder.
        status (str): The current status of the account (e.g., "Active", "Inactive").
    """

    def __init__(self, username, password, email, age, status):
        """
        Initializes a new Account object.

        Args:
            username (str): The username for the account.
            password (str): The password for the account.
            email (str): The email address for the account.
            age (str): The age of the account holder.
            status (str): The current status of the account.
        """
        self.__username = username
        self.__password = password
        self.__email = email
        self.__age = age
        self.__status = status

    # Setters
    def set_username(self, username: str):
        self.__username = username

    def set_password(self, password: str):
        self.__password = password

    def set_email(self, email: str):
        self.__email = email

    def set_age(self, age: str):
        self.__age = age

    def set_status(self, status: str):
        self.__status = status

    # Getters
    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password

    def get_email(self) -> str:
        return self.__email

    def get_age(self) -> str:
        return self.__age

    def get_status(self) -> str:
        return self.__status

    # Behavioral Methods
    def login(self, username: str, password: str) -> bool:
        """
        Logs into the account if the username and password match.

        Args:
            username (str): The username for login.
            password (str): The password for login.

        Returns:
            bool: True if login is successful, False otherwise.
        """
        return self._username == username and self._password == password

    def deactivate_account(self):
        """
        Deactivates the account by changing its status to 'Inactive'.
        """
        self.__status = "Inactive"


class Customer(Account):
    """
    Represents a Customer account.

    Attributes:
        name (str): The name of the customer.
        gender (str): The gender of the customer.
        phone_number (str): The phone number of the customer.
        credit_card_info (str): The credit card information of the customer.
        loyalty_points (float): The loyalty points of the customer.
        purchase_history (list): A list of past purchases.
    """

    def __init__(self, username, password, email, age, status, name, gender, phone_number, credit_card_info, loyalty_points, purchase_history=None):
        """
        Initializes a new Customer object.

        Args:
            username (str): Username for the account.
            password (str): Password for the account.
            email (str): Email address for the account.
            age (str): Age of the account holder.
            status (str): Status of the account.
            name (str): Name of the customer.
            gender (str): Gender of the customer.
            phone_number (str): Phone number of the customer.
            credit_card_info (str): Credit card details.
            loyalty_points (float): Loyalty points for the customer.
            purchase_history (list): List of past purchases.
        """
        super().__init__(username, password, email, age, status)
        self.__name = name
        self.__gender = gender
        self.__phone_number = phone_number
        self.__credit_card_info = credit_card_info
        self.__loyalty_points = float(loyalty_points)
        self.__purchase_history = purchase_history if purchase_history else []

    # Setters
    def set_name(self, name: str):
        self.__name = name

    def set_gender(self, gender: str):
        self.__gender = gender

    def set_phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    def set_credit_card_info(self, credit_card_info: str):
        self.__credit_card_info = credit_card_info

    def set_loyalty_points(self, loyalty_points: float):
        self.__loyalty_points = loyalty_points

    def set_purchase_history(self, purchase_history: list):
        self.__purchase_history = purchase_history

    # Getters
    def get_name(self) -> str:
        return self.__name

    def get_gender(self) -> str:
        return self.__gender

    def get_phone_number(self) -> str:
        return self.__phone_number

    def get_credit_card_info(self) -> str:
        return self.__credit_card_info

    def get_loyalty_points(self) -> float:
        return self.__loyalty_points

    def get_purchase_history(self) -> list:
        return self.__purchase_history

    # Behavioral Methods
    def add_purchase(self, purchase: dict):
        """
        Adds a purchase to the customer's purchase history.

        Args:
            purchase (dict): The purchase details to add.
        """
        self.__purchase_history.append(purchase)

    def redeem_loyalty_points(self, points: float):
        """
        Redeems loyalty points for the customer.

        Args:
            points (float): The number of points to redeem.
        """
        if points <= self.__loyalty_points:
            self.__loyalty_points -= points

    def display_order_history(self) -> str:
        """
        Displays the customer's purchase history.

        Returns:
            str: A formatted string of the purchase history.
        """
        return "\n".join([str(order) for order in self.__purchase_history])

class Admin(Account):
    """
    Represents an Admin account.

    Attributes:
        number_of_accounts_accessed (int): The number of accounts accessed by the admin.
        permission_list (list): The list of permissions assigned to the admin.
        role (str): The role of the admin (e.g., "Manager", "Super Admin").
        assigned_department (str): The department assigned to the admin.
        security_clearance_level (int): Security clearance level for the admin.
        is_super_admin (bool): Whether the admin is a super admin.
    """

    def __init__(self, username, password, email, age, status, number_of_accounts_accessed, permission_list, role, assigned_department, security_clearance_level, is_super_admin):
        """
        Initializes a new Admin object.

        Args:
            username (str): Username for the account.
            password (str): Password for the account.
            email (str): Email address for the account.
            age (str): Age of the account holder.
            status (str): Status of the account.
            number_of_accounts_accessed (int): Number of accounts accessed.
            permission_list (list): List of permissions assigned.
            role (str): Role of the admin.
            assigned_department (str): Admin's department.
            security_clearance_level (int): Security clearance level.
            is_super_admin (bool): Whether the admin is a super admin.
        """
        super().__init__(username, password, email, age, status)
        self.__number_of_accounts_accessed = number_of_accounts_accessed
        self.__permission_list = permission_list
        self.__role = role
        self.__assigned_department = assigned_department
        self.__security_clearance_level = security_clearance_level
        self.__is_super_admin = is_super_admin

    # Setters
    def set_number_of_accounts_accessed(self, number: int):
        self.__number_of_accounts_accessed = number

    def set_permission_list(self, permission_list: list):
        self.__permission_list = permission_list

    def set_role(self, role: str):
        self.__role = role

    def set_assigned_department(self, department: str):
        self.__assigned_department = department

    def set_security_clearance_level(self, level: int):
        self.__security_clearance_level = level

    def set_is_super_admin(self, is_super_admin: bool):
        self.__is_super_admin = is_super_admin

    # Getters
    def get_number_of_accounts_accessed(self) -> int:
        return self.__number_of_accounts_accessed

    def get_permission_list(self) -> list:
        return self.__permission_list

    def get_role(self) -> str:
        return self.__role

    def get_assigned_department(self) -> str:
        return self.__assigned_department

    def get_security_clearance_level(self) -> int:
        return self.__security_clearance_level

    def get_is_super_admin(self) -> bool:
        return self.__is_super_admin

    # Behavioral Methods
    def generate_report(self) -> str:
        """
        Generates an admin activity report.

        Returns:
            str: A summary of the admin's activity.
        """
        return (
            f"Admin Role: {self.__role}\n"
            f"Department: {self.__assigned_department}\n"
            f"Accounts Accessed: {self.__number_of_accounts_accessed}\n"
            f"Super Admin: {'Yes' if self.__is_super_admin else 'No'}"
        )







