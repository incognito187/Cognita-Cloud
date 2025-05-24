# Cognita-Cloud

Here's a **complete and structured use case** for the **WhatsApp Ordering Service** at **BVS Butchery Ghana**, covering the full customer journey from initial interaction to order placement, and how BVS Butchery Ghana captures all relevant data into a **Google Cloud-hosted Google Sheet**.

---

## 🧾 Use Case: WhatsApp-Based Meat Ordering System for BVS Butchery Ghana

### 🎯 Objective:
To allow customers to place meat orders via WhatsApp by first selecting between **Beef, Lamb, or Chicken**, then choosing products, quantities, and delivery preferences — with all order details automatically captured in real-time into a **Google Sheet** hosted on **Google Cloud**.

---

## 📝 User Story:

**Actor:** Customer (e.g., Ms. Ama Mensah)  
**Channel:** WhatsApp Business  
**Goal:** Place an order for meat products after being prompted to choose between Beef, Lamb, or Chicken  
**System:** WhatsApp Bot + Google Sheets Integration using Zapier or Make.com  

---

## ✅ Main Success Scenario – Order Placement Flow

### Step 1: Customer Initiates Chat
Customer sends any message to BVS Butchery’s WhatsApp number (e.g., “Hi”).

### Step 2: Bot Asks for Product Category
Bot replies:

> 👋 Welcome to *BVS Butchery Ghana*!  
> What type of meat would you like to order?  
> Reply with:
> - `Beef`  
> - `Lamb`  
> - `Chicken`

### Step 3: Customer Selects Meat Type
Customer replies:

```
Beef
```

### Step 4: Bot Lists Available Products Based on Selection
Bot replies:

> Here are our beef options:  
> - Beef Bone-In @ GHC 85/kg  
> - Beef Boneless @ GHC 125/kg  
> - Beef Fillet (imported premium) @ GHC 545/kg  
> - Beef Heart & Liver @ GHC 45/kg  
> - Beef Ribeye (300g pack) @ GHC 205/pack  
> - Beef Topside (Imported) @ GHC 250/kg  
> - Beef Tripe (Imported) @ GHC 45/kg  
>  
> Please reply with your selection(s), e.g.:  
> "I want 2kg Beef Boneless and 1 pack Beef Ribeye"

### Step 5: Customer Places Order
Customer replies:

```
I want 1kg Beef Bone-In and 2 packs of Beef Ribeye
```

### Step 6: Bot Confirms Order Summary
Bot replies:

> Got it! Your order:
> - 1kg Beef Bone-In @ GHC 85 = GHC 85  
> - 2 x Beef Ribeye (300g pack) @ GHC 205 each = GHC 410  
>  
> **Total: GHC 495**  
>  
> Is this order for **Pickup** or **Delivery**?

### Step 7: Customer Chooses Order Type

#### Option A: Pickup
Customer replies:

```
Pickup
```

Bot replies:

> Great! Where would you like to pick up your order?  
> 1. Madina Branch  
> 2. Kaneshie Market  
> 3. Tema Station

Customer replies:

```
Madina Branch
```

Bot confirms:

> Your order is confirmed for pickup at the **Madina Branch**.  
> We’ll notify you when it’s ready!

#### Option B: Delivery (Alternative Path)
Customer replies:

```
Delivery
```

Bot replies:

> Please provide your delivery address.

Customer replies:

```
No. 12 Liberation Ave, East Legon
```

Bot replies:

> When would you like the delivery?

Customer replies:

```
Tomorrow at 5 PM
```

Bot replies:

> Please confirm your phone number for delivery coordination.

Customer replies:

```
+233247654321
```

Bot confirms:

> Your order will be delivered to:  
> **No. 12 Liberation Ave, East Legon**  
> Scheduled for: **Tomorrow at 5 PM**  
> Contact: **+233247654321**  
>  
> Our rider will contact you when close.

---

## 🛠️ Technical Implementation Overview

| Component | Description |
|----------|-------------|
| **WhatsApp Business API** | To receive messages/orders from customers |
| **Rule-based Chatbot Logic** | Guides users through category → product → quantity → order type → location |
| **Parser Logic** | Extracts product names, quantities, calculates prices |
| **Google Sheets (Google Cloud)** | Centralized order log updated in real-time |
| **Zapier / Make.com Automation** | Connects WhatsApp messages to Google Sheets |
| **Optional CRM Sync** | For storing recurring customer details |

---

## 📊 Data Captured in Google Sheet

The system logs the following data into a **Google Sheet** stored on **Google Cloud**:

| Timestamp | Customer Name | Phone Number | Product | Quantity | Unit Price | Total Price | Order Type | Location/Address | Delivery Date | Delivery Time | Status |
|-----------|---------------|--------------|---------|----------|------------|-------------|------------|------------------|---------------|---------------|--------|
| 2025-04-05 11:00 AM | Kofi Boateng | +233247654321 | Beef Bone-In | 1 kg | 85 | 85 | Pickup | Madina Branch | - | - | Processing |
| 2025-04-05 11:00 AM | Abena Mensah | +233241234567 | Beef Ribeye (pack) | 2 packs | 205 | 410 | Delivery | No. 12 Liberation Ave | Tomorrow | 5 PM | Processing |

---

## 🔁 Alternative Flows

### 1. Changing Category After Selection
Customer says:

```
Oops, I meant Chicken
```

Bot replies:

> No problem! Here are our chicken options:  
> - Chicken Neck @ GHC 25/kg  
> - Chicken Thigh (soft) @ GHC 70/kg  
> - Chicken Thigh HARD @ GHC 75/kg  
> - Chicken Eggs (free range) @ GHC 60/dozen  
>  
> Please reply with your selection(s)

### 2. Invalid Input Handling
Customer says:

```
Hello, I need fish
```

Bot replies:

> Sorry, we currently only offer meat products including Beef, Lamb, and Chicken.

---

## 📈 Business Benefits for BVS Butchery Ghana

- **Structured ordering flow** that guides users step-by-step
- **Improved accuracy** due to guided prompts and parsing logic
- **Real-time logging** of all orders into the cloud
- **Better fulfillment tracking** for both pickup and delivery
- **Scalable and low-cost solution**
- **Customer insights** via analytics on order history and trends

---

## 📱 Sample Customer Message Template (Optional)

To assist customers who prefer a faster way to order:

```
ORDER:
Category: [Beef/Lamb/Chicken]
Items:
- [Quantity] [Product Name]
- [Quantity] [Product Name]
Order Type: [Pickup/Delivery]
Location/Address: [Pickup Location or Full Address]
[If Delivery] Date: [DD/MM/YYYY], Time: [HH:MM]
Phone: [+233...]
```

---

## 🚀 Next Steps You Can Take

Would you like me to help you with:
- A **template Google Sheet structure**?
- A **Zapier automation setup guide**?
- A **Dialogflow chatbot script** for this use case?
- A **sample bot response JSON structure** for backend integration?

Let me know how you'd like to proceed!


---

Here's a **complete solution** for building a **WhatsApp Ordering Chatbot using Twilio Studio, Python (Flask), and Google Sheets** for **BVS Butchery Ghana**.

This system will:

- Use **Twilio Studio** to create the WhatsApp chatbot flow.
- Use **Python (Flask)** as the backend to handle dynamic logic like price calculation or data formatting.
- Send collected order data to a **Google Sheet** (hosted on Google Cloud) for tracking and fulfillment.

---

## ✅ Solution Overview

| Component | Purpose |
|----------|---------|
| **Twilio Studio** | Visual builder for WhatsApp bot flow (menu prompts, user input collection). |
| **Python + Flask API** | Backend server to handle complex logic, calculations, and sending data to Google Sheets. |
| **Google Sheets API** | Store and manage orders in real-time. |
| **Twilio WhatsApp Sandbox / Number** | Customer interface via WhatsApp. |

---

## 🧩 Step-by-Step Implementation

### 1. **Set Up Your Google Sheet**

Create a new Google Sheet with the following columns:

| Timestamp | Name | Phone | Product | Quantity | Unit Price | Total Price | Order Type | Location/Address | Delivery Date | Delivery Time | Status |
|-----------|------|-------|---------|----------|------------|-------------|------------|------------------|---------------|---------------|--------|

> 🔗 Share the sheet with your service account email (from Google Cloud project) with "Editor" access.

---

### 2. **Enable Google Sheets API & Create Service Account**

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or use an existing one
3. Enable **Google Sheets API**
4. Create a **Service Account**, grant it **Editor** permissions
5. Download JSON key file (e.g., `credentials.json`)
6. Save this file in your project directory

---

### 3. **Set Up Flask App (Backend Server)**

#### Install Required Packages:
```bash
pip install flask google-auth-httplib2 google-api-python-client twilio python-dotenv
```

#### Project Structure:
```
bvs-butchery-bot/
├── app.py
├── credentials.json
├── .env
└── requirements.txt
```

#### `.env` File:
```env
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
GOOGLE_SHEET_ID=your_sheet_id
```

#### `app.py` – Main Flask App:
```python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Google Sheets Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(os.getenv("GOOGLE_SHEET_ID")).sheet1

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").strip()
    from_number = request.values.get("From", "").replace("whatsapp:", "")

    resp = MessagingResponse()
    msg = resp.message()

    try:
        # This is a simplified version of how you might parse the final message
        if "ORDER SUMMARY:" in incoming_msg:
            lines = incoming_msg.splitlines()
            name = lines[1].split(":")[1].strip()
            phone = from_number
            product = lines[2].split(":")[1].strip()
            quantity = lines[3].split(":")[1].strip()
            unit_price = int(lines[4].split(":")[1].strip())
            total_price = int(lines[5].split(":")[1].strip())
            order_type = lines[6].split(":")[1].strip()
            location = lines[7].split(":")[1].strip()
            delivery_date = lines[8].split(":")[1].strip() if len(lines) > 8 else ""
            delivery_time = lines[9].split(":")[1].strip() if len(lines) > 9 else ""

            # Append to Google Sheet
            sheet.append_row([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                name,
                phone,
                product,
                quantity,
                unit_price,
                total_price,
                order_type,
                location,
                delivery_date,
                delivery_time,
                "Pending"
            ])

            msg.body("✅ Thank you! Your order has been received and will be processed shortly.")
        else:
            msg.body("We're processing your order... Please complete the selection in the menu.")

    except Exception as e:
        msg.body("❌ There was an error processing your order. Please try again later.")
        print(e)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
```

---

### 4. **Deploy Flask App**

You can deploy your Flask app using:

- **Ngrok** (for testing): `ngrok http 5000`
- **Heroku**
- **Render**
- **Google Cloud Run**

After deployment, you'll get a public URL like: `https://your-flask-app.onrender.com/whatsapp`

---

### 5. **Build the Bot Flow in Twilio Studio**

#### Steps:

1. Log in to [Twilio Console](https://www.twilio.com/console)
2. Go to **Studio > Flows > Create New Flow**
3. Choose **Start from scratch**
4. Drag and drop widgets to build the flow:
   - **Send & Wait for Reply**: Ask category (Beef/Lamb/Chicken)
   - **Split Based On** → User response
   - Show product list based on category
   - Collect product names and quantities
   - Ask pickup/delivery
   - Collect address/date/time if delivery
   - Final confirmation
   - Use **Webhook** widget to POST to `/whatsapp` endpoint

#### Example Webhook Payload to Send to Flask:
```json
{
  "Name": "Ama Mensah",
  "Product": "Beef Bone-In",
  "Quantity": "1kg",
  "Unit Price": 85,
  "Total Price": 85,
  "Order Type": "Pickup",
  "Location": "Madina Branch"
}
```

---

### 6. **Connect to WhatsApp**

1. In Twilio Console, go to **Phone Numbers > Manage > Active Numbers**
2. Configure your WhatsApp sandbox number
3. Set the **Studio Flow** as the default handler for incoming messages

---

## 📈 Business Benefits Recap

| Feature | Benefit |
|--------|---------|
| WhatsApp Chatbot | 24/7 customer ordering |
| Dynamic Menus | Easy navigation through products |
| Google Sheets Integration | Real-time order tracking |
| Scalable Architecture | Add more features later (SMS, voice, AI) |
| Low Maintenance | Minimal human interaction required |

---

## 🚀 Next Steps You Can Take

Would you like me to help you with:
- A **ready-to-use Twilio Studio Flow JSON export**?
- A **sample Ngrok + Flask setup guide**?
- A **Dialogflow + Twilio Flex integration** for advanced use cases?
- A **web UI dashboard for viewing orders from the Google Sheet**?

Let me know what you'd like next — I'm happy to provide templates, code samples, or full walkthroughs!