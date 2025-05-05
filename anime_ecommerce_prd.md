
# 📝 Product Requirements Document (PRD)

**Project Name:** Anime E-commerce Store  
**Authors:** Artur Tymchuk, Dmytro Yarmoliuk
**Date:** 2025-04-25  
**Version:** 1.0

---

## 🔖 1. Overview

**Purpose:**  
Create a functional online store for anime-related products (figures, posters, apparel, etc.) where users can browse, add items to a cart, and place orders.

**Goal:**  
Provide a smooth, user-friendly shopping experience for anime fans, built using Django as the backend framework.

---

## 🎯 2. Objectives & Success Metrics

| Objective                        | Success Metric                                                |
|----------------------------------|---------------------------------------------------------------|
| Enable product browsing          | Users can view a list of products and filter them by category |
| Handle user registration/login   | Users can sign up, log in, and manage their profile           |
| Implement shopping cart          | Users can add, update, and remove items in their cart         |
| Process orders                   | Users can checkout and see order summaries                    |
| Admin can manage content         | Admin panel allows CRUD operations for products and orders    |

---

## 👤 3. Target Users

- Anime enthusiasts  
- Students interested in anime merchandise  
- Collectors of anime figures and posters  

---

## 🔍 4. Features

### ✅ Core Features

| Feature             | Description                                           |
|---------------------|-------------------------------------------------------|
| User Authentication | Sign up, log in, log out, profile page               |
| Product Catalog     | List of products, product detail page, category filter |
| Shopping Cart       | Add, update, remove items from cart                  |
| Checkout            | Order summary, shipping info, place order feature    |
| Order History       | Users can view past orders                           |
| Admin Management    | Admin dashboard to manage products, orders, categories|

### 💡 Optional Features (Future Improvements)

- Product ratings & reviews  
- Payment gateway integration (Stripe/PayPal)  
- Product search bar  
- Wishlist functionality  
- Creating custom products (with future print-on-demand availability)
- Discount codes  


---

## 🧱 5. Tech Stack

| Layer          | Technology                   |
|----------------|------------------------------|
| Backend        | Django (Python)              |
| Frontend       | HTML/CSS, Bootstrap or Tailwind |
| Database       | SQLite (dev), PostgreSQL (prod optional) |
| Hosting        | PythonAnywhere or Railway
| Version Control| Git & GitHub                 |

---

## 🧩 6. Data Models (Simplified so TBD)

### Product
- id_product (PK) 
- Description  
- Name 
- Price  
- Quantity
- Price
- id_category (FK)  

### Category
- id_category  
- Name
- Perent_Category (PK)

### Media
- id_media 
- Media 
- alternative_text
- id_product (FK)

### Order_Item
- id_order_item
- id_order (FK) 
- id_product(FK)

### Order
- id_order
- Order_number  
- Total  
- Address
- Creation_date
- Deliver_date
- id-status (FK)
- Customer_phone
- Customer_email

### User
- id_user
- Login
- First_name
- Last_name
- Email
- Phone
- Creation_date

### Payment
- id_payment
- id_order
- Provider
- Ammount
- Method
- Status
- date
- ?id_password?


---

## 🛠 7. Assumptions

- Users will use basic login (no social auth for now)  
- Payment will not be real; simulated checkout  
- Admin will manage products through Django admin  

---

## 🧪 8. Testing Plan

- Unit tests for models  
- Manual testing for user flows (cart, checkout)  
- Admin tested separately  

---

## 📦 9. Deliverables

- Source code (GitHub)  
- README with setup instructions  
- Screenshots or demo video (for portfolio)
