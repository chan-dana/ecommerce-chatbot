from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error
import re

app = Flask(__name__)

# Function to search the database based on keywords, price, and category
def search_products(query=None, max_price=None, category=None):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your MySQL password
            database="ecommerce"
        )
        
        if conn.is_connected():
            cursor = conn.cursor()
            
            # Build query dynamically based on provided filters
            conditions = []
            params = []

            if query:
                conditions.append("(name LIKE %s OR description LIKE %s)")
                params.extend([f"%{query}%", f"%{query}%"])
            if max_price is not None:
                conditions.append("price <= %s")
                params.append(max_price)
            if category:
                conditions.append("category = %s")
                params.append(category)

            # Combine conditions into a single SQL WHERE clause
            where_clause = " AND ".join(conditions)
            sql_query = f"SELECT * FROM products WHERE {where_clause}" if conditions else "SELECT * FROM products"

            cursor.execute(sql_query, tuple(params))
            results = cursor.fetchall()

            # Return products as a list of dictionaries
            return [
                {
                    "product_id": row[0],
                    "name": row[1],
                    "price": row[2],
                    "category": row[3],
                    "description": row[4],
                    "image_url": row[5],
                }
                for row in results
            ]
    except Error as e:
        print(f"Error: {e}")
        return []
    finally:
        if conn.is_connected():
            conn.close()

@app.route('/')
def home():
    return render_template('chatbot.html')

# API endpoint for chatbot queries
@app.route('/chat', methods=['POST'])
def chatbot():
    user_message = request.json.get('message', '').strip().lower()

    if not user_message:
        return jsonify({"reply": "Please enter a valid query."})
    
    # Basic commands
    if user_message in ["hello", "hi", "hey"]:
        return jsonify({"reply": "Hello! How can I help you today? You can search for products by name, category, or price."})
    elif user_message in ["help", "how does this work"]:
        return jsonify({"reply": "You can ask me to search for products by their name, category, or price. For example, 'Show me electronics under 200.00', 'I need a laptop under 500.00', or 'Products under 200.00 in clothing'."})
    
    # Check if user is asking for products under a specific price and category
    price_match = re.search(r'under\s*(\d+\.\d{2})', user_message)
    category_match = re.search(r'in\s*(\w+)', user_message)

    max_price = float(price_match.group(1)) if price_match else None
    category = category_match.group(1) if category_match else None

    if max_price or category:
        products = search_products(query=None, max_price=max_price, category=category)
        if products:
            reply = f"Here are some products under ${max_price}" + (f" in {category}:" if category else ":") + "<br>"
            for p in products:
                reply += f"<strong>{p['name']}</strong> - ${p['price']}<br>{p['description']}<br>"
            return jsonify({"reply": reply, "products": products})
        else:
            reply = f"Sorry, I couldn't find any products under ${max_price}" + (f" in {category}" if category else "") + "."
            return jsonify({"reply": reply})
    
    # Search for products by name or description
    products = search_products(query=user_message)
    if products:
        reply = "Here are some products I found:<br>"
        for p in products:
            reply += f"<strong>{p['name']}</strong> - ${p['price']}<br>{p['description']}<br>"
        return jsonify({"reply": reply, "products": products})
    else:
        return jsonify({"reply": "Sorry, I couldn't find any products matching your query."})

if __name__ == '__main__':
    app.run(debug=True)
