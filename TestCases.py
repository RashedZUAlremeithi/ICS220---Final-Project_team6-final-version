from Main import *
from datetime import datetime

# Ticket Class Test
print("--- Ticket Class Test ---")
ticket1 = Ticket(
    ticket_type="VIP",
    description="Access to all rides",
    price=150.0,
    validity="1 day",
    discount=10.0,
    limitations="None",
    visit_date=datetime(2024, 12, 1)
)
# Accessing price via getter method
print("Original Price:", ticket1.get_price())
ticket1.apply_discount()  # Apply discount
# Accessing updated price via getter method
print("Price after applying discount:", ticket1.get_price())
print("Ticket Description:", ticket1.describe_ticket())

# Customer Class Test
print("--- Customer Class Test ---")
customer1 = Customer(
    username="customer1",
    password="pass456",
    email="customer1@example.com",
    age="30",
    status="Active",
    name="John Doe",
    gender="Male",
    phone_number="123-456-7890",
    credit_card_info="1234-5678-9012-3456",
    loyalty_points=200.5,
    purchase_history=[]
)
# Accessing the name and loyalty points via getter methods
print("Customer Name:", customer1.get_name())
print("Loyalty Points:", customer1.get_loyalty_points())
customer1.add_purchase({"item": "VIP Ticket", "price": 100})
customer1.redeem_loyalty_points(50)
# Accessing updated loyalty points via getter method
print("Loyalty Points after redemption:", customer1.get_loyalty_points())
print("Purchase History:", customer1.display_order_history())

# Admin Class Test
print("--- Admin Class Test ---")
admin1 = Admin(
    username="admin1",
    password="adminpass",
    email="admin1@example.com",
    age="35",
    status="Active",
    number_of_accounts_accessed=10,
    permission_list=["view_reports", "manage_users"],
    role="Super Admin",
    assigned_department="IT",
    security_clearance_level=5,
    is_super_admin=True
)
# Accessing admin role and permission list via getter methods
print("Admin Role:", admin1.get_role())
print("Permission List:", admin1.get_permission_list())
print("Generated Report:", admin1.generate_report())

# Ride Class Test
print("--- Ride Class Test ---")
ride1 = Ride(
    name="Roller Coaster",
    ride_type="Thrill",
    min_height="48 inches",
    max_height="78 inches",
    duration="2 minutes",
    capacity=20,
    status="Open"
)
# Accessing ride status via check_status method
print("Ride Status:", ride1.check_status())
ride1.reset_ride()  # Reset ride
# Accessing updated ride status via check_status method
print("Ride Status after reset:", ride1.check_status())

# Park Class Test
print("--- Park Class Test ---")
park1 = Park(
    name="Wonderland",
    location="Los Angeles, CA",
    operating_hours="9:00 AM - 10:00 PM",
    current_visitors=500,
    attractions=["Splash Zone", "Haunted House"],
    events=["Halloween Special"],
    services=["Food Court", "Gift Shop"]
)
# Accessing park name and location via getter methods
print("Park Name:", park1.get_name())
print("Park Location:", park1.get_location())
park1.add_ride(ride1)
# Accessing total ride capacity via check_capacity method
print("Total Ride Capacity:", park1.check_capacity())
park1.update_operating_hours("8:00 AM - 11:00 PM")
# Accessing updated operating hours via getter method
print("Updated Operating Hours:", park1.get_operating_hours())

# Order Class Test
print("--- Order Class Test ---")
order1 = Order(
    customer=customer1,
    ticket_list=[ticket1],
    quantity=2,
    total_price=0.0,  # Total price will be calculated later
    amount_paid=225.0,
    payment_type="CARD",
    order_date=datetime(2024, 12, 5).strftime("%Y-%m-%d"),
    order_id="ORD12345"
)

# Calculate total price of the order
order1.calculate_total_price()  # This will update the total price based on ticket prices

# Accessing order details via getters
print("Order ID:", order1.get_order_id())
print("Customer Name:", order1.get_customer().get_name())
print("Order Date:", order1.get_order_date())
print("Payment Type:", order1.get_payment_type())
print("Quantity of Tickets:", order1.get_quantity())
print("Total Price:", order1.get_total_price())
print("Amount Paid:", order1.get_amount_paid())

# Accessing order summary
print("Order Summary:\n", order1.get_order_summary())



print("\nAll tests completed successfully!")