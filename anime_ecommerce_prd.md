
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

## 📊 Database Schema
[ERD](https://postimg.cc/LgLHLG2N)

<details>
<summary>📚 Database Tables Overview</summary>

### 🛍️ Product
- `id_product` (PK)  
- `name`  
- `description`  
- `price`  
- `quantity`  
- `id_category` (FK)

### 🗂️ Category
- `id_category` (PK)  
- `name`  
- `parent_category` (FK)

### 🖼️ Media
- `id_media` (PK)  
- `media`  
- `alternative_text`  
- `id_product` (FK)

### 📦 Order_Item
- `id_order_item` (PK)  
- `id_order` (FK)  
- `id_product` (FK)

### 🧾 Order
- `id_order` (PK)  
- `order_number`  
- `total`  
- `address`  
- `creation_date`  
- `delivery_date`  
- `id_status` (FK)  
- `customer_phone`  
- `customer_email`  
- `id_user` (FK)

### 👤 User
- `id_user` (PK)  
- `first_name`  
- `last_name`  
- `username`  
- `email`  
- `phone`  
- `creation_date`

### 💳 Payment
- `id_payment` (PK)  
- `id_order` (FK)  
- `provider`  
- `amount`  
- `method`  
- `status`  
- `date`

### 🔒 Authorization
- `id_auth` (PK)  
- `id_user` (FK)  
- `hashed_password`  
- `hash_method`

### 🛒 Cart
- `id_cart` (PK)  
- `id_user` (FK)

### 🧺 CartItem
- `id_cart_item` (PK)  
- `id_product` (FK)  
- `id_cart` (FK)  
- `quantity`  
- `added_date`

### 🔄 Status
- `id_status` (PK)  
- `status`

</details>

<details>
<summary>📚 Full SQL Script</summary>

```sql
CREATE TABLE "Order"(
  "idOrder" BIGINT NOT NULL,
  "orderNumber" CHAR(255) NOT NULL,
  "total" INTEGER NOT NULL,
  "address" CHAR(255) NOT NULL,
  "creationDate" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
  "deliveryDate" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
  "idStatus" BIGINT NOT NULL,
  "customerPhone" CHAR(255) NOT NULL,
  "customerEmail" CHAR(255) NOT NULL,
  "idUser" BIGINT NULL
);
ALTER TABLE "Order" ADD PRIMARY KEY("idOrder");
ALTER TABLE "Order" ADD CONSTRAINT "order_ordernumber_unique" UNIQUE("orderNumber");

CREATE TABLE "Product"(
  "idProduct" BIGINT NOT NULL,
  "name" CHAR(255) NOT NULL,
  "desc" TEXT NOT NULL,
  "price" INTEGER NOT NULL,
  "quantity" INTEGER NOT NULL,
  "idCategory" BIGINT NOT NULL
);
ALTER TABLE "Product" ADD PRIMARY KEY("idProduct");
ALTER TABLE "Product" ADD CONSTRAINT "product_name_unique" UNIQUE("name");

CREATE TABLE "Order Item"(
  "idOrderItem" BIGINT NOT NULL,
  "idOrder" BIGINT NOT NULL,
  "idProduct" BIGINT NOT NULL
);
ALTER TABLE "Order Item" ADD PRIMARY KEY("idOrderItem");

CREATE TABLE "User"(
  "idUser" BIGINT NOT NULL,
  "firstName" CHAR(255) NOT NULL,
  "lastName" CHAR(255) NOT NULL,
  "username" CHAR(255) NOT NULL,
  "email" CHAR(255) NOT NULL,
  "phone" CHAR(255) NOT NULL,
  "creationDate" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE "User" ADD PRIMARY KEY("idUser");

CREATE TABLE "Authorization"(
  "idAuth" BIGINT NOT NULL,
  "idUser" BIGINT NOT NULL,
  "hashedPassword" CHAR(255) NOT NULL,
  "hashMethod" CHAR(255) NOT NULL
);
ALTER TABLE "Authorization" ADD PRIMARY KEY("idAuth");

CREATE TABLE "Cart"(
  "idCart" BIGINT NOT NULL,
  "idUser" BIGINT NOT NULL
);
ALTER TABLE "Cart" ADD PRIMARY KEY("idCart");

CREATE TABLE "Category"(
  "idCategory" BIGINT NOT NULL,
  "name" CHAR(255) NOT NULL,
  "parentCategory" BIGINT NOT NULL
);
ALTER TABLE "Category" ADD PRIMARY KEY("idCategory");

CREATE TABLE "Media"(
  "idMedia" BIGINT NOT NULL,
  "media" TEXT NOT NULL,
  "alternativeText" TEXT NOT NULL,
  "idProduct" BIGINT NOT NULL
);
ALTER TABLE "Media" ADD PRIMARY KEY("idMedia");

CREATE TABLE "CartItem"(
  "idCartItem" BIGINT NOT NULL,
  "idProduct" BIGINT NOT NULL,
  "idCart" BIGINT NOT NULL,
  "quantity" INTEGER NOT NULL,
  "addedDate" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE "CartItem" ADD PRIMARY KEY("idCartItem");

CREATE TABLE "Payment"(
  "idPayment" BIGINT NOT NULL,
  "idOrder" BIGINT NOT NULL,
  "provider" TEXT NOT NULL,
  "method" CHAR(255) NOT NULL,
  "status" CHAR(255) NOT NULL,
  "date" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
  "amount" INTEGER NOT NULL
);
ALTER TABLE "Payment" ADD PRIMARY KEY("idPayment");

CREATE TABLE "Status"(
  "idStatus" BIGINT NOT NULL,
  "status" CHAR(255) NOT NULL
);
ALTER TABLE "Status" ADD PRIMARY KEY("idStatus");

ALTER TABLE "CartItem" ADD CONSTRAINT "cartitem_idcart_foreign" FOREIGN KEY("idCart") REFERENCES "Cart"("idCart");
ALTER TABLE "CartItem" ADD CONSTRAINT "cartitem_idproduct_foreign" FOREIGN KEY("idProduct") REFERENCES "Product"("idProduct");
ALTER TABLE "Order Item" ADD CONSTRAINT "order_item_idproduct_foreign" FOREIGN KEY("idProduct") REFERENCES "Product"("idProduct");
ALTER TABLE "Order Item" ADD CONSTRAINT "order_item_idorder_foreign" FOREIGN KEY("idOrder") REFERENCES "Order"("idOrder");
ALTER TABLE "Cart" ADD CONSTRAINT "cart_iduser_foreign" FOREIGN KEY("idUser") REFERENCES "User"("idUser");
ALTER TABLE "Payment" ADD CONSTRAINT "payment_idorder_foreign" FOREIGN KEY("idOrder") REFERENCES "Order"("idOrder");
ALTER TABLE "Order" ADD CONSTRAINT "order_idstatus_foreign" FOREIGN KEY("idStatus") REFERENCES "Status"("idStatus");
ALTER TABLE "Order" ADD CONSTRAINT "order_iduser_foreign" FOREIGN KEY("idUser") REFERENCES "User"("idUser");
ALTER TABLE "Category" ADD CONSTRAINT "category_parentcategory_foreign" FOREIGN KEY("parentCategory") REFERENCES "Category"("idCategory");
ALTER TABLE "Media" ADD CONSTRAINT "media_idproduct_foreign" FOREIGN KEY("idProduct") REFERENCES "Product"("idProduct");
ALTER TABLE "Authorization" ADD CONSTRAINT "authorization_iduser_foreign" FOREIGN KEY("idUser") REFERENCES "User"("idUser");
ALTER TABLE "Product" ADD CONSTRAINT "product_idcategory_foreign" FOREIGN KEY("idCategory") REFERENCES "Category"("idCategory");
```
</details>


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
