# Teracyte Home Assignment

A full-stack web application for viewing and analyzing cell microscopy images with secure authentication and real-time data polling capabilities. Built as a home assignment to demonstrate full-stack development skills.

## Installation

### Prerequisites
- Python 3.8+
- Node.js 18+
- Git

### Clone the Repository
```bash
git clone https://github.com/TomerDun/teracyte-home.git
cd teracyte-home
```

### Back-End Setup

#### 1. Environment Configuration
Obtain a valid `.env` file and place it in the `back-end/` directory. Use `.env.example` as a reference and update configurations as needed:

```bash
cd back-end
# Create .env file with the following variables:
# SECRET_KEY - Your secret key for JWT signing
# ALGORITHM - HS256
# ACCESS_TOKEN_EXPIRE_MINUTES - Token expiration time
# DATABASE_URL - sqlite:///./teracyte.db
# FRONTEND_URL - http://localhost:5173
# TC_API_BASE_URL - Teracyte API base URL
# TC_USERNAME - Teracyte API username
# TC_PASSWORD - Teracyte API password
```

#### 2. Install Dependencies and Run Server
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn server:app --reload
```
The back-end server will start on `http://localhost:8000`

**Note:** Running the server for the first time will automatically create the SQLite database file.

#### 3. Create Admin User (Development Only)
If an admin user does not exist in the Users table, create one by making a POST request:

```bash
# Example using curl or any API client
POST http://localhost:8000/api/test-create-user
Content-Type: application/json

{
  "username": "admin",
  "password": "your-password"
}
```

### Front-End Setup

#### 1. Install Dependencies
```bash
cd front-end
npm install
```

#### 2. Configuration (Optional)
If needed, update the backend API base URL in `front-end/src/services/apiService.ts`:

```typescript
export const API_BASE_URL = 'http://localhost:8000/api';
export const SERVER_BASE_URL = 'http://localhost:8000';
```

#### 3. Run Development Server
```bash
npm run dev
```
The front-end application will start on `http://localhost:5173`

## Tech Stack

### Back-End
- **FastAPI** - Modern Python web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database
- **Pydantic** - Data validation

### Front-End
- **React 19** - UI framework
- **Vite** - Build tool and dev server
- **React Router** - Client-side routing
- **Tailwind CSS** - Utility-first CSS framework
- **Recharts** - Charting library for histograms

### Development Tools
- **ESLint** - Code linting

## AI Tooling Used

This project was developed with the assistance of AI-powered tools:

- **GitHub Copilot** - AI pair programming for code generation, completion, and refactoring throughout the development process
- **Figma MCP** - Used in conjunction with Copilot for design-to-code workflow
- **Figma Make** - Initial UI/UX mockups and design prototyping

## Main Features

### 5.1 Authentication Proxy & JWT Token Manager
- **Auth Proxy**: Acts as an intermediary between the client and Teracyte API, handling authentication securely
- **JWT Token Management**: Automatically monitors token expiration and refreshes access tokens using refresh tokens
- **Retry Logic**: Implements resilient token retrieval with automatic retry mechanisms for API reliability
- **Token Validation**: Verifies JWT format and expiration before making API requests

### 5.2 Data Polling for Image Data
- **Automated Polling**: Fetches new cell image data from the Teracyte API every 30 seconds
- **Real-time Updates**: Automatically updates the dashboard when new images are available
- **Histogram Generation**: Displays pixel intensity distribution for each image

### 5.3 History Panel
- **Complete Image Archive**: Shows all previously retrieved cell images
- **Quick Navigation**: Click any historical image to view its details and histogram
- **Persistent Storage**: Image history is maintained in the database for future reference
- **Visual Timeline**: Chronologically organized image cards with thumbnails and metadata

## System Design

### 6.1 Authentication Flow

```
1. User Login
   ↓
2. Client sends credentials to Backend API
   ↓
3. Backend validates user credentials (local DB)
   ↓
4. Backend requests tokens from Teracyte API
   ↓
5. Backend receives and stores access_token + refresh_token (DB only)
   ↓
6. Backend generates app-specific JWT token (longer-lived)
   ↓
7. Backend returns app JWT to Client
   ↓
8. Client stores app JWT (localStorage)
   ↓
9. Client includes app JWT in subsequent API requests

Token Management:
   - Teracyte API tokens: Stored only in backend DB, never exposed to client
   - App JWT: Used for client authentication against the backend
   - Backend automatically refreshes Teracyte tokens when expired
   - Client only handles app JWT
```

### 6.2 Data Retrieval Flow

```
1. User lands on Home Page
   ↓
2. Initial data load:
   - Fetch latest image data (or specific image if selected)
   - Fetch image history
   ↓
3. Display:
   - Image with metadata
   - Histogram chart
   - History panel
   ↓
4. Polling Loop (every 30s):
   │
   ├─→ Client requests new image data
   │   ↓
   ├─→ Backend forwards request to Teracyte API (auto-refreshes tokens if needed)
   │   ↓
   ├─→ Teracyte API returns new image (if available)
   │   ↓
   ├─→ Backend saves to database
   │   ↓
   ├─→ Client updates UI and refreshes history panel
   │   ↓
   └─→ Wait 30s, repeat

User Interaction:
   - If specific image selected → Fetch and display that image
   - Otherwise → Display latest image and auto-update UI when it changes
   - Click history item → Fetch and display specific image
```

## Screenshots

Additional screenshots and images of the application are available in the `screenshots/` folder.

