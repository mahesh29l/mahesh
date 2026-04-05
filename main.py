import os
from restaurants import RestaurantManager
from ratings import RatingManager

def display_menu():
    print("\n===== FOOD DELIVERY APP =====")
    print("1. View Nearby Restaurants")
    print("2. View Restaurant Menu")
    print("3. Rate a Food Item")
    print("4. View Food Ratings")
    print("5. Exit")
    print("=============================
")

def main():
    restaurant_manager = RestaurantManager()
    rating_manager = RatingManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            print("\n--- NEARBY RESTAURANTS ---")
            restaurants = restaurant_manager.get_nearby_restaurants()
            for idx, restaurant in enumerate(restaurants, 1):
                print(f"{idx}. {restaurant['name']} - {restaurant['cuisine']}")
                print(f"   Address: {restaurant['address']}")
                print(f"   Delivery Time: {restaurant['delivery_time']} mins")
                print(f"   Average Rating: {restaurant['rating']}/5.0\n")
        
        elif choice == '2':
            rest_name = input("Enter restaurant name: ").strip()
            menu = restaurant_manager.get_restaurant_menu(rest_name)
            if menu:
                print(f"\n--- {rest_name} MENU ---")
                for item in menu['items']:
                    print(f"• {item['name']} - ${item['price']}")
                print()
            else:
                print("Restaurant not found!\n")
        
        elif choice == '3':
            food_name = input("Enter food item name: ").strip()
            rating = input("Enter rating (1-5): ").strip()
            review = input("Enter review: ").strip()
            try:
                rating = float(rating)
                if 1 <= rating <= 5:
                    rating_manager.add_rating(food_name, rating, review)
                    print("Rating added successfully!\n")
                else:
                    print("Please enter a rating between 1 and 5.\n")
            except ValueError:
                print("Invalid rating. Please enter a number.\n")
        
        elif choice == '4':
            print("\n--- FOOD RATINGS ---")
            ratings = rating_manager.get_all_ratings()
            if ratings:
                for food, data in ratings.items():
                    avg_rating = sum(r['rating'] for r in data) / len(data)
                    print(f"• {food}")
                    print(f"  Average Rating: {avg_rating:.1f}/5.0 ({len(data)} reviews)")
                    print()
            else:
                print("No ratings yet.\n")
        
        elif choice == '5':
            print("Thank you for using Food Delivery App. Goodbye!\n")
            break
        
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()