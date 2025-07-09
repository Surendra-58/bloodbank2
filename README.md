# 🩸 BloodBank2 - Blood Donation Management System

A full-featured web application built with **Django** that connects **donors**, **hospitals**, and **admins** to manage blood requests, inventory, and donation activities efficiently.

## 🚀 Features

### 👤 Donor
- Register & verify with identity proof
- Update personal details and donation history
- Accept/reject blood donation requests (based on BMI eligibility)
- View donation count and profile statistics
- Comment and like blog posts

### 🏥 Hospital
- Raise blood requests
- Track request status: Pending, Processing, Delivered/Failed
- Update profile and upload hospital ID
- View blood inventory status

### 🛠️ Admin
- Approve new users (donors, hospitals)
- Manage blood inventory
- Monitor and manage blood requests
- View donor and hospital profiles
- Post blogs and announcements

### 📦 Other Core Modules
- Modern blog system with like/comment/share
- Live notifications for new blog posts
- Firebase-based messaging (Messenger-like chat system)
- AJAX support for interactive features
- BMI-based donor health validation
- Responsive & interactive UI (Bootstrap, custom styles)

## 🖼️ Screenshots

> Add screenshots here (e.g. home page, donor profile, hospital dashboard)

## 🧑‍💻 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite / PostgreSQL
- **Media Storage:** Cloudinary (recommended for deployment)
- **Notifications & Messaging:** Firebase
- **Deployment:** Render / Heroku / Railway (configurable)

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Surendra-58/bloodbank2.git
   cd bloodbank2
