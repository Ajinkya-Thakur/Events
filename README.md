# Events - Event Expense Tracker

**Events** is an simple event expense tracker that eliminates the hassle of managing event expenses.  
Access it for free: [events-self.vercel.app](https://events-self.vercel.app)

---

## Features

### 1. **Quick Sign-In**
   - Start instantly by signing in with your Google account.

### 2. **Budget Estimation**
   - Set expected contributions from members to get an estimated budget for your event.

### 3. **Flexible Event Management**
   - Create events and define your personal contribution.
   - Add registered users as event members using their email addresses.

### 4. **Expense Tracking**
   - Members can log expenses, which automatically updates individual and event balances.
   - View transaction history for complete transparency.

### 5. **Comprehensive Insights**
   - The event details page displays remaining balances for the event and individual members.

### 6. **Control & Flexibility**
   - Members can delete events or individual transactions if needed.

---

## How It Works

1. **Sign Up/Sign In**: Log in with your Google account to start using the app.
2. **Create an Event**: Add a new event, set expected contributions, and invite members.
3. **Add Expenses**: Log expenses for the event and track contributions automatically.
4. **Manage Events**: Delete events or specific transactions as per your requirements.

---

## Tech Stack

- **Languages**: python, HTML  
- **Framework**: Django  
- **Database**: PostgreSQL  
- **Hosting**: Vercel  

---

## Getting Started Locally

To run this project locally, follow below steps

1. Clone the repository on your local.
2. Navigate to the root directory i.e Events/events.
3. Add a .env file containing 'DATABASE_URL' and 'SECRET_KEY'.
4. Run 'pip install -r requirements.txt'
5. create folder named 'migrations' in Django apps.
6. Run 'python manage.py migrate' to apply migrations to your database
7. To configure google auth follow https://youtu.be/yO6PP0vEOMc?si=kQ4Q2SmXxrrMPpDQ
8. Finally, run 'python manage.py runserver' to start the development server.

 
