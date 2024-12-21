# Blissify E-Commerce Chatbot Project Documentation

## Overview
Blissify is an e-commerce chatbot project designed to enhance user shopping experience by integrating chatbot functionality for seamless product search, category filtering, and price-based recommendations. The project consists of multiple interconnected web pages, styled using Bootstrap, and powered by both PHP and Flask backends.

## Project Structure

### Web Pages:
1. **Home Page (index.html)**
   - **Purpose**: Serves as the landing page of the website.
   - **Features**:
     - Includes a welcome section and links to navigate to other parts of the website.
     - Provides user authentication modals for logging in and signing up.

2. **Shop Page (shop.html)**
   - **Purpose**: Displays all available products with filtering and searching capabilities.
   - **Features**:
     - Product categories: Electronics, Clothing, and Home & Kitchen.
     - Search bar to filter products by keywords.
     - Dynamic filtering buttons for product categories.
     - Product cards display product details such as name, price, and image.

3. **Combined E-Commerce Page**
   - **Purpose**: A unified page displaying products across multiple categories (Clothing, Electrical Appliances, Home & Kitchen Decor), with filtering and cart management.
   - **Features**:
     - Product Categories: Men/Women (Clothing), Electrical Appliances, Home Decor, Kitchen, Furniture, and Lighting.
     - Add-to-Cart: Each product has an "Add to Cart" button, updating the shopping cart in localStorage.
     - Dynamic Filtering: JavaScript-based filtering to show/hide products based on selected categories.
     - Cart Management: A fixed cart button displays the number of items in the cart, with cart data saved in localStorage.
     - Responsive Design: Uses Bootstrap for a mobile-friendly layout.

4. **Cart Page (cart.html)**
   - **Purpose**: Displays the shopping cart contents.
   - **Features**:
     - Shows product details, quantities, and total price.
     - Allows users to update product quantities and remove items.
     - Provides a checkout button to confirm the order.

5. **Order Confirmation Page (confirmation.html)**
   - **Purpose**: Confirms the user's order after checkout.
   - **Features**:
     - Displays order ID, total price, and order items.
     - Includes a "Continue Shopping" button to clear the cart and redirect to the shop page.

6. **Chatbot Page (chatbot.html)**
   - **Purpose**: Features an interactive chatbot to assist users.
   - **Features**:
     - Styled with Bootstrap for a modern, responsive design.
     - Chat interface for searching products by name, category, or price.
     - Typing indicator for a realistic conversational experience.
     - Fetches chatbot replies via Flask API backend.

### Backend Functionality:
1. **Database Connection (db_connect.php)**
   - Establishes a secure MySQLi connection to the e-commerce database.
   - Handles product and user authentication data.
   - Manages database connection errors.

2. **User Authentication (login_backend.php)**
   - Handles login and sign-up processes.
   - Verifies user credentials and manages account creation.

3. **Flask Backend (app.py)**
   - Implements a Flask application for chatbot interactions.
   - **Key Features**:
     - `search_products()`: Searches the database for products based on keywords, price, and category.
     - `/chat` API endpoint: Processes user queries and returns chatbot responses.
     - **Logic**:
       - Handles user messages for greetings, help commands, or product searches.
       - Supports queries for products under a specific price or within a particular category.

### Key Features:
1. **Chatbot Functionality**
   - **Natural Language Understanding**: Processes queries like “Show me laptops under $500” or “Electronics under $200.”
   - **Dynamic Responses**: Retrieves products matching the query and formats results for display.
   - **Typing Indicator**: Shows a "Bot is typing..." message while processing queries.
   - **Error Handling**: Provides fallback messages if no products are found or if an error occurs.

2. **Product Search**
   - **Keyword Search**: Matches product names or descriptions based on user input and redirects to the appropriate category page.
   - **Price Filter**: Retrieves products below a specified price in chatbot.
   - **Category Filter**: Filters products by categories such as Electronics, Clothing, and Home & Kitchen. If no match is found, displays an error message.

3. **Shopping Cart Management**
   - **Dynamic Cart Updates**: Tracks cart items and updates totals in real-time using localStorage.
   - **CRUD Operations**: Allows adding, updating, and removing items from the cart.

4. **Database Integration**
   - **MySQL Database**: Stores product details, user accounts, and transaction data.
   - **Search Queries**: Executes SQL queries to fetch products based on user inputs.

## Technical Details

### Frontend:
- **HTML & CSS**: Provides the structure and styling for web pages.
- **Bootstrap**: Ensures responsiveness and modern UI design.
- **JavaScript**: Manages client-side interactions, such as chatbot communication and cart functionality.

### Backend:
- **PHP**: Handles database connections and authentication.
- **Flask**: Powers the chatbot’s logic and serves as the backend API.
- **MySQL**: Stores data for users, products, and transactions.

### API Endpoints:
- **/chat**
  - **Method**: POST
  - **Input**: JSON payload with a message field.
  - **Output**: JSON response containing the chatbot’s reply and, optionally, product details.

## User Workflow
1. **Home Page (index.html)**: The landing page with a welcome section and links to other parts of the website, including authentication modals for login and sign-up.
2. **Login/Register**: Access the platform via login.html.
3. **Explore Products**: Browse categories on shop.html or use the chatbot for targeted searches.
4. **Add to Cart**: Use "Add to Cart" buttons to build a shopping list.
5. **View Cart**: Review selections on cart.html and proceed to checkout.
6. **Confirm Order**: Complete the transaction and view details on confirmation.html.

## Deployment
- **Local Development**: Run `app.py` using Flask’s development server.
- **Production**: Host the application on a web server with PHP and Python support.

## Version Control & Git Repository
The project is hosted on GitHub for version control. Clone the repository using:  
`https://github.com/chan-dana/ecommerce-chatbot`

Regularly pull updates and commit changes for new features or fixes.

## Future Enhancements
- **AI Integration**: Add advanced natural language processing for better chatbot understanding.
- **Payment Gateway**: Integrate secure payment processing.
- **User Profiles**: Provide personalized product recommendations based on user history.

## Conclusion
The Blissify E-Commerce Chatbot Project brings a modern and interactive touch to online shopping, making it easier and more enjoyable for users to search for products, filter by categories, and get personalized recommendations based on their preferences. By combining PHP for user authentication and Flask for chatbot functionality, this platform creates a smooth and seamless shopping experience. The use of localStorage for cart management and MySQL for secure data storage ensures that users can easily manage their shopping journey, from browsing to checkout.

Looking ahead, there are exciting opportunities to enhance the chatbot’s capabilities with advanced AI, improve personalization features, and even add secure payment processing to make the shopping experience more complete. The future of Blissify holds even more potential for making online shopping smarter and more tailored to each individual user.
