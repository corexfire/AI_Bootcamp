import random

class CRMService:
    @staticmethod
    def get_order_status(order_id):
        # Mock logic
        if "123" in order_id:
            return "Shipped", "Your order is on the way and will arrive tomorrow."
        elif "999" in order_id:
            return "Cancelled", "Your order was cancelled due to payment failure."
        else:
            return "Processing", "We are currently packing your order."

    @staticmethod
    def create_ticket(user_id, issue_type, description):
        ticket_id = f"TICKET-{random.randint(1000, 9999)}"
        print(f"[CRM] Created ticket {ticket_id} for User {user_id}: {issue_type} - {description}")
        return ticket_id

class PaymentGateway:
    @staticmethod
    def check_transaction(transaction_id):
        return "Success" if int(transaction_id) % 2 == 0 else "Failed"
