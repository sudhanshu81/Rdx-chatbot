import streamlit as st
from PIL import Image

# Set the page layout
st.set_page_config(page_title="Food Interactive Page", page_icon="🍔", layout="wide")

# Add custom CSS to style the page
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
            font-family: Arial, sans-serif;
        }
        h1 {
            text-align: center;
            color: #ff6347;
        }
        .food-category {
            font-size: 24px;
            color: #444;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .food-card {
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 10px;
            text-align: center;
            margin-bottom: 20px;
            background-color: white;
        }
        .food-img {
            border-radius: 10px;
            width: 100%;
            max-width: 250px;
            height: auto;
        }
        .suggestions {
            background-color: #ffebcc;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Header for the app
st.markdown("<h1>🍕 Welcome To The Tasty Food  🍔</h1>", unsafe_allow_html=True)

# Sidebar for food selection
st.sidebar.header("Choose Your Favorite Food Category")
food_category = st.sidebar.selectbox("Select a category", ["Fast Food", "Desserts", "Healthy", "Beverages"])

# Function to display food cards
def display_food(image_path, food_name):
    st.markdown(f"<div class='food-card'><img src='{image_path}' class='food-img'/><h3>{food_name}</h3></div>", unsafe_allow_html=True)

# Show different food categories
st.markdown("<h2 class='food-category'>Explore Food Categories:</h2>", unsafe_allow_html=True)

# Columns for better layout
col1, col2, col3 = st.columns(3)

if food_category == "Fast Food":
    with col1:
        display_food("https://images.unsplash.com/photo-1606787366850-de6330128bfc", "Burger")
    with col2:
        display_food("https://images.unsplash.com/photo-1546069901-eacef0df6022", "Pizza")
    with col3:
        display_food("https://images.unsplash.com/photo-1586190848861-99aa4a171e90", "Fries")
elif food_category == "Desserts":
    with col1:
        display_food("https://images.unsplash.com/photo-1581579180652-eb52961ca605", "Cake")
    with col2:
        display_food("https://images.unsplash.com/photo-1515548219560-4e0a04881a9d", "Ice Cream")
    with col3:
        display_food("https://images.unsplash.com/photo-1517197089047-e2962e4d1b80", "Donut")
elif food_category == "Healthy":
    with col1:
        display_food("https://images.unsplash.com/photo-1512058564366-c9a2e7db5a9d", "Salad")
    with col2:
        display_food("https://images.unsplash.com/photo-1526040652367-ac003a0475fe", "Avocado Toast")
    with col3:
        display_food("https://images.unsplash.com/photo-1572441710564-6a85936ba843", "Smoothie Bowl")
elif food_category == "Beverages":
    with col1:
        display_food("https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445", "Coffee")
    with col2:
        display_food("https://images.unsplash.com/photo-1502069019502-0eeaa22ba23c", "Milkshake")
    with col3:
        display_food("https://images.unsplash.com/photo-1551021192-0a3f1d73680c", "Juice")

# User input for food preferences
st.markdown("<h2>🍽️ What's Your Favorite Dish?</h2>", unsafe_allow_html=True)
favorite_food = st.text_input("Enter your favorite food")

if favorite_food:
    st.markdown(f"<div class='suggestions'><h3>🍴 Yummy! We love {favorite_food} too! 😋</h3></div>", unsafe_allow_html=True)

# Food suggestions based on the user's input
st.markdown("<h2>💡 Get a Food Suggestion:</h2>", unsafe_allow_html=True)

# A list of random food suggestions
import random

suggestions = {
    "Fast Food": ["Cheeseburger", "Pepperoni Pizza", "Loaded Nachos"],
    "Desserts": ["Chocolate Lava Cake", "Tiramisu", "Fruit Tart"],
    "Healthy": ["Quinoa Salad", "Veggie Wrap", "Kale Smoothie"],
    "Beverages": ["Iced Latte", "Green Tea", "Lemonade"]
}

if st.button("Give me a food suggestion"):
    suggestion = random.choice(suggestions[food_category])
    st.markdown(f"<div class='suggestions'><h3>✨ How about trying some {suggestion} today? 🍽️</h3></div>", unsafe_allow_html=True)

# Footer
st.markdown("<hr><div style='text-align: center;'>🍴 Made with ❤️ using Streamlit by Food Lover 🍽️</div>", unsafe_allow_html=True)
