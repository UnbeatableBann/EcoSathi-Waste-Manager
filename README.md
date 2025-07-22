# 🌿 EcoSathi – Waste Manager

**Connect • Collect • Conserve**

EcoSathi is an innovative waste management platform that connects users with ragpickers to schedule waste pickups. It promotes transparency, empowerment, and sustainable living by providing fair pricing, real‑time tracking, and ragpicker support.

---

## 🚀 Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Quick Start](#quick-start)
* [Usage](#usage)
* [Contributing](#contributing)
* [Contact & Acknowledgements](#contact--acknowledgements)

---

## ✨ Features

* **Multi‑user roles**: Choose between Client, Individual Ragpicker, or Organization.
* **Authentication**: Secure login via JWT and Google OAuth.
* **Map Integration**: View and connect with nearby ragpickers using Leaflet.js.
* **AI Chatbot**: Gemini-powered generative AI assists users.
* **Earnings Dashboard**: Track ragpicker/client earning stats.
* **Verification**: Users are validated via identity proof.
* **Ragpicker Empowerment**: Access skill-building courses and job opportunities.

---

## 🛠 Tech Stack

| Layer      | Technology             |
| ---------- | ---------------------- |
| Frontend   | HTML, CSS, JS  |
| Backend    | Python, Django    |
| Database   | PostgreSQL                |
| Auth       | Django AUth      |


---
## 📋 Usage Guide

1. **Register/Login** – as Client or Ragpicker (via Google or email).
2. **Profile Setup** – upload ID proof, set preferences.
3. **Map View** – Clients find ragpickers; ragpickers see pickup requests.
4. **Chatbot** – Ask the Gemini AI assistant for help.
5. **Earnings** – Track completed pickups and revenue.

---

## 🚢 Deployment

### Frontend

* Build with:

  ```bash
  cd client
  npm run build
  ```
* Deploy static files (e.g. to Vercel, Netlify, GitHub Pages).

### Backend

* Deploy the server (Express + MongoDB):

  * Options: Heroku, DigitalOcean, AWS EC2.
  * Set environment variables accordingly.

---

## ✅ Testing

*(If applicable)*

* **Backend**: `npm test` in `/server` (Jest/Supertest)
* **Frontend**: `npm test` in `/client` (React Testing Library)

*(Add instructions relevant to your tests)*

---

## 🤝 Contributing

We welcome contributions!

1. Fork the repo.
2. Create your feature branch:

   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit changes:

   ```bash
   git commit -m "Add feature XYZ"
   ```
4. Push:

   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request.

**Please** ensure code follows established style guidelines and add tests for new features.

---

## 🙏 Contact & Acknowledgements

* Created by **UnbeatableBann**
* Inspired by the EcoSathi platform
* Thanks to the open-source community and contributors!

---

*EcoSathi – building a cleaner, fairer world, one pickup at a time.*
