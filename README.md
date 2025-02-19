# **FOOTBALL LIVE SCORES⚽**

## **📌 Project Overview**
This website displays **live fixtures** for users' favorite football teams in the **Premier League**.

---

## **📂 Table of Contents**
- [About](#about)
- [Working](#working)
- [Guide to Run WebApp](#guide-to-run-webapp)
- [References](#references)

---

## **📜 About**
We designed a **web application** that allows users to select their favorite football teams and fetches **live match fixtures** using an **external API**. This web app is inspired by popular soccer apps like the **Barclays Premier League app**.

### **🔹 Technologies Used**
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Database:** MySQL (Google Cloud)
- **API:** Football API from RapidAPI
- **Hosting & Deployment:** Google Kubernetes Engine (GKE)

---

## **⚙️ Working**
### **1️⃣ Home Page & Signup**
- The home page contains navigation to different sections.
- Users **register** on the **Signup page**, providing details like **name, email, and password**.
- The data is **stored in MySQL** on **Google Cloud**.
- Users select their **favorite team** from a dropdown list, which is also stored in the database.

### **2️⃣ Login & User Session**
- Users log in with their **email and password**.
- The credentials are validated against **MySQL Cloud storage**.
- **Sessions** are initiated to maintain user login state.

### **3️⃣ User Settings Page**
- Users can **update their profile information** (name, email, password).
- The navigation bar updates to show additional options.
- Users can **log out**, which deletes their session and redirects them to the login page.

### **4️⃣ Live Fixture & Team Fixture Pages**
- **Team Fixture Page:** Displays upcoming fixtures **for the selected favorite team**.
- **Live Fixture Page:** Shows live fixtures **for all teams** playing on the current day.

---

## **🛠️ Guide to Run WebApp**

### **Running the Web Application Locally (Windows & Ubuntu)**

### **Windows (Using Visual Studio Code)**
1️⃣ Open **CMD** in **VS Code Terminal**.
2️⃣ Activate the virtual environment:
   ```sh
   .\env\Scripts\activate
   ```
3️⃣ Set the Flask environment:
   ```sh
   set FLASK_APP=app.py
   set FLASK_ENV=development
   ```
4️⃣ Run the application:
   ```sh
   flask run
   ```

### **Ubuntu (Using Terminal)**
1️⃣ Clone the repository:
   ```sh
   git clone https://github.com/CameronRobsonLeigh/Football.git
   ```
2️⃣ Navigate into the repository:
   ```sh
   cd Football/
   ```
3️⃣ Create a virtual environment:
   ```sh
   python3 -m venv venv
   ```
4️⃣ Activate the virtual environment:
   ```sh
   source venv/bin/activate
   ```
5️⃣ Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
6️⃣ Run Flask:
   ```sh
   flask run
   ```

---

## **📜 References**
- **Football API** - Used to fetch live football fixtures.
- **Google Kubernetes Engine (GKE)** - Used for deployment.

---

## **📦 Docker & Deployment**
To create a **Docker container**:
```sh
docker build -t football-live-scores .
docker run -p 5000:5000 football-live-scores
```

To deploy on **Google Kubernetes Engine (GKE)**:
```sh
gcloud container clusters create football-cluster
gcloud container clusters get-credentials football-cluster
docker tag football-live-scores gcr.io/YOUR_PROJECT_ID/football-live-scores
gcloud docker -- push gcr.io/YOUR_PROJECT_ID/football-live-scores
```
