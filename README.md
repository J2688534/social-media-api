# Social Media API

A backend project built with **Django** and **Django REST Framework**.  
This API allows users to:
- Register and log in
- Create, read, update, and delete posts
- Follow and unfollow other users
- View a feed of posts from followed users


## Tech Stack
- Python
- Django
- Django REST Framework (DRF)
- SQLite (default, can be swapped with PostgreSQL)

- I was able to complete 
Social Media API is a Django-based backend application that allows users to create accounts, log in, follow/unfollow other users, and view profiles. This project solves the problem of connecting users and managing social interactions through a RESTful API.

## Features
- **User Registration & Login**  
- **View User Profile**  
- **Follow/Unfollow Users**  
- **JWT Authentication using SimpleJWT**  
- **REST API with Django REST Framework** 

# Social Media API  

A simple **social media backend API** built with **Django REST Framework**.  
It allows users to register, log in, create posts, comment, and like posts.  
This project demonstrates authentication, CRUD operations, and API best practices.  

---

## 🚀 Features  

- **User Authentication**  
  - Register new users  
  - Login with JWT (JSON Web Token)  
  - Token-based authentication  

- **Posts**  
  - Create, read, update, delete posts  
  - Optional media (URL link to images/videos)  
  - View posts in reverse chronological order  

- **Comments**  
  - Add comments to posts  
  - View comments for a post  

- **Likes**  
  - Like or unlike posts  
  - View who liked a post  

---

## 🛠️ Tech Stack  

- **Python 3**  
- **Django 5**  
- **Django REST Framework (DRF)**  
- **SQLite (default)**  
- **JWT Authentication**  

---

## 🔑 Authentication  

This project uses **JWT authentication**:  

1. Register:  
   ```http
   POST /api/users/register/
