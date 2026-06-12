from abc import ABC, abstractmethod

# ORDER CLASSES


class Order:
    def __init__(self, order_id, customer_name, amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.amount = amount

    def get_order_details(self):
        return (
            f"Order ID: {self.order_id}, "
            f"Customer: {self.customer_name}, "
            f"Amount: ₹{self.amount}"
        )


class RegularOrder(Order):
    pass


class DiscountedOrder(Order):
    def __init__(self, order_id, customer_name, amount, discount):
        discounted_amount = amount - discount
        super().__init__(order_id, customer_name, discounted_amount)
        self.discount = discount


class PriorityOrder(Order):
    def __init__(self, order_id, customer_name, amount, priority_fee):
        total_amount = amount + priority_fee
        super().__init__(order_id, customer_name, total_amount)
        self.priority_fee = priority_fee



# PAYMENT INTERFACES & CLASSES


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):

    def pay(self, amount):
        print(f"[Credit Card] Payment of ₹{amount} successful.")


class UPIPayment(PaymentMethod):

    def pay(self, amount):
        print(f"[UPI] Payment of ₹{amount} successful.")


class WalletPayment(PaymentMethod):

    def pay(self, amount):
        print(f"[Wallet] Payment of ₹{amount} successful.")



# NOTIFICATION INTERFACES & CLASSES


class NotificationService(ABC):

    @abstractmethod
    def send_notification(self, message):
        pass


class EmailNotification(NotificationService):

    def send_notification(self, message):
        print(f"[Email] {message}")


class SMSNotification(NotificationService):

    def send_notification(self, message):
        print(f"[SMS] {message}")


class PushNotification(NotificationService):

    def send_notification(self, message):
        print(f"[Push Notification] {message}")



# STORAGE INTERFACES & CLASSES


class StorageService(ABC):

    @abstractmethod
    def save_order(self, order):
        pass


class DatabaseStorage(StorageService):

    def save_order(self, order):
        print("[Database] Order saved:")
        print(order.get_order_details())


class FileStorage(StorageService):

    def save_order(self, order):
        print("[File] Order saved:")
        print(order.get_order_details())



# ORDER SERVICE


class OrderService:

    def __init__(
        self,
        payment_method: PaymentMethod,
        notification_service: NotificationService,
        storage_service: StorageService
    ):
        self.payment_method = payment_method
        self.notification_service = notification_service
        self.storage_service = storage_service

    def place_order(self, order: Order):

        print("\n========== ORDER PROCESSING ==========")

        # Step 1: Process Payment
        self.payment_method.pay(order.amount)

        # Step 2: Save Order
        self.storage_service.save_order(order)

        # Step 3: Send Notification
        self.notification_service.send_notification(
            f"Order {order.order_id} placed successfully."
        )

        print("======================================\n")



# MAIN DRIVER CODE


if __name__ == "__main__":

    # Create Orders
    regular_order = RegularOrder(201, "Ankit", 8500)

    discounted_order = DiscountedOrder(
        211,
        "Aditya",
        6500,
        700
    )

    priority_order = PriorityOrder(
        209,
        "Kaushal",
        9000,
        500
    )

    # Create Services
    payment = UPIPayment()
    notification = EmailNotification()
    storage = DatabaseStorage()

    # Inject Dependencies
    order_service = OrderService(
        payment,
        notification,
        storage
    )

    # Process Orders
    order_service.place_order(regular_order)
    order_service.place_order(discounted_order)
    order_service.place_order(priority_order)