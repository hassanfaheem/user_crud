import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services import UserService

def main():
    user_service = UserService()

    try:
        # Create
        user_service.create_user("elon_musk", "password123", True)
        user_service.create_user("bill_gates", "password456", False)

        # Read
        print(user_service.read_user("elon_musk"))
        print(user_service.read_user("bill_gates"))

        # Update
        user_service.update_user("elon_musk", active=False)
        print(user_service.read_user("elon_musk"))

        # Delete
        user_service.delete_user("bill_gates")
        try:
            print(user_service.read_user("bill_gates"))
        except ValueError as e:
            print(e)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
