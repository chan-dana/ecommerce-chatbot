from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Function to search the database based on keywords
def search_products(query):
    try:
        conn = mysql.connector.connect(
            host="localhost",      # or use the IP address of the server
            user="root",           # your MySQL username, usually 'root'
            password="",           # your MySQL password (if any)
            database="ecommerce"   # name of your database
        )
        
        if conn.is_connected():
            cursor = conn.cursor()

            # Search products by name or description
            cursor.execute("SELECT * FROM products WHERE name LIKE %s OR description LIKE %s", 
                           (f"%{query}%", f"%{query}%"))
            results = cursor.fetchall()

            # Return products as a list of dictionaries
            return [
                {
                    "product_id": row[0],
                    "name": row[1],
                    "price": row[2],
                    "category": row[3],
                    "description": row[4],
                    "image_url": row[5]
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
        return jsonify({"reply": "Hello! How can I help you today? You can search for products by name or category."})
    elif user_message in ["help", "how does this work"] :
        return jsonify({"reply": "You can ask me to search for products by their name or category. For example, try 'Show me electronics' or 'I need a laptop'."})
    
    # Search for products in the database
    products = search_products(user_message)
    if products:
        reply = "Here are some products I found:\n"
        for p in products:
            reply += f"{p['name']} - ${p['price']} ({p['description']})\nImage: {p['image_url']}\n"
            # Send the image URL along with the reply for rendering in the chatbot
            return jsonify({"reply": reply, "image_url": p['image_url']})
    else:
        reply = "Sorry, I couldn't find any products matching your query."
    
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
