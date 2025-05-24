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
