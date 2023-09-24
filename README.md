# System Architecture for Note-Taking Web Application

## Table of Contents
1. [Overview](#overview)
2. [Front-end](#frontend)
3. [Back-end](#backend)
4. [Database](#database)
5. [Deployment](#deployment)
6. [Step-by-Step Instructions](#stepbystepinstructions)

## Overview
The application comprises a front-end built using ReactJS, a back-end using FastAPI with Python, and a PostgreSQL database for persistence. It follows a traditional three-tier architecture:
- **Presentation Layer (Front-end)**: ReactJS
- **Business Logic Layer (Back-end)**: Python (FastAPI)
- **Data Storage Layer**: PostgreSQL

## Front-end <a name="frontend"></a>
### Login/Signup Page
- Utilize React Router for routing.
- Create forms for login and signup.
- OAuth2 implementation.

### Note-taking Page
- React components for bullet points.
- State management for bullet hierarchy.

### Arrow Button Functionality
- Arrow buttons to toggle child bullet points.

### Offline Storage
- IndexedDB or local storage for offline data.

### Communication with Back-end
- Axios or Fetch API for HTTP requests.

### Authentication
- Store JWT or cookies as directed by the back-end.

## Back-end <a name="backend"></a>
### Authentication
- OAuth2 packages for social login.
- JWT or session-based cookies for authentication.

### API Endpoints
- `/login`, `/signup`: Authentication
- `/notes`: CRUD for notes

### Data Sync
- Endpoint for syncing notes when online.

### Database Models
- 'User' model: `user_id`, `email`, etc.
- 'Note' model: `note_id`, `user_id`, `content`, `parent_id`

### Database Optimization
- Indexing on `parent_id`.
- Pre-fetching children of visible bullet points.

## Database <a name="database"></a>
### User Table
- To store user data.

### Notes Table
- To store notes; each with a reference to its parent.

## Deployment <a name="deployment"></a>
### Frontend
- Deployed on Firebase Hosting.

### Backend
- Deployed on AWS EC2, coupled with PostgreSQL on the same instance.

## Detailed Step-by-Step Instructions <a name="stepbystepinstructions"></a>
### Front-end
1. Create a new React app.
2. `npm install`: Install necessary packages.
3. Components for Login/Signup and Note-taking.
4. State management via React Hooks.
5. Local storage or IndexedDB for offline notes.

### Back-end
1. Create a new Python project.
2. `pip install`: FastAPI, SQLAlchemy, etc.
3. Database models and relationships.
4. CRUD and authentication API endpoints.

### Database
1. Install PostgreSQL.
2. Create User and Notes tables.
3. Foreign keys for relationships.
4. Indexing on `parent_id`.

### Integration
1. Axios for API calls.
2. Offline data synchronization.
