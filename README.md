# Cognita-Cloud

Here's an **enhanced use case** for a **WhatsApp ordering service** at **BVS Butchery Ghana**, where the **WhatsApp bot initiates the conversation by asking the customer what type of meat they want to order: Beef, Lamb, or Chicken**. This helps streamline the ordering process and improves user experience.

---

## 🧾 Use Case: WhatsApp Ordering Service with Initial Category Selection

### 🎯 Objective:
Allow customers to place meat orders via WhatsApp, starting with a prompt to select between **Beef, Lamb, or Chicken**, and have their **orders captured in real-time into a Google Sheet** hosted on **Google Cloud**.

---

## 📝 User Story:

**Actor:** Customer (e.g., Ms. Abena Boateng)  
**Channel:** WhatsApp Business  
**Goal:** Place an order for meat products after being prompted to choose a category  
**System:** WhatsApp Bot + Google Sheets Integration (via Zapier or Make.com)

---

## ✅ Scenario – Happy Path

### Step 1: Customer Initiates Chat
Ms. Abena Boateng sends a message to BVS Butchery Ghana’s WhatsApp Business number.

She types: `Hi`

### Step 2: WhatsApp Bot Responds with Menu Prompt
The system replies:

> 👋 Welcome to *BVS Butchery Ghana*!  
> What type of meat would you like to order?  
> Type:
> - `Beef`  
> - `Lamb`  
> - `Chicken`  

### Step 3: Customer Selects Meat Type
Customer replies:  
```
Beef
```

Bot replies with available beef items:

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

### Step 4: Customer Places Order
Customer replies:

```
I want 1kg Beef Bone-In and 2 packs of Beef Ribeye
```

### Step 5: Bot Acknowledges and Calculates Order
Bot replies:

> Got it! Your order:
> - 1kg Beef Bone-In @ GHC 85 = GHC 85  
> - 2 x Beef Ribeye (300g pack) @ GHC 205 each = GHC 410  
>  
> **Total: GHC 495**  
> We’ll prepare your order and notify you when ready.

### Step 6: Order is Automatically Logged into Google Sheet
The system logs the following data in the **Google Sheet** on **Google Cloud**:

| Timestamp           | Customer Name     | Phone Number    | Product             | Quantity | Unit Price | Total Price |
|---------------------|-------------------|------------------|----------------------|----------|------------|-------------|
| 2025-04-05 11:00 AM | Abena Boateng     | +233247654321   | Beef Bone-In         | 1 kg     | 85         | 85          |
| 2025-04-05 11:00 AM | Abena Boateng     | +233247654321   | Beef Ribeye (pack)   | 2 packs  | 205        | 410         |

### Step 7: Admin Prepares and Confirms Order
Once the butchery team prepares the order, they either update the sheet with a status column or send a confirmation message via WhatsApp:

> Your order is ready for pickup at BVS Butchery, Madina. Thank you!

---

## 🔁 Alternative Flow – Changing Category
If the customer changes their mind after selecting a category:

```
Chicken
Oops, I meant Lamb
```

Bot replies:

> No problem! Here are our lamb options:  
> - Lamb Chops @ GHC 250/kg  
> - Lamb Rack @ GHC 465/kg  
>  
> Please reply with your selection.

---

## 🛠️ Technical Implementation Summary

| Component                  | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| WhatsApp Business API     | To receive messages/orders from customers                                  |
| Rule-based Chatbot Logic  | Asks for category first, then provides product list                         |
| Parser Logic              | Extracts product names, quantities, and calculates prices                   |
| Google Sheets             | Centralized order log updated in real-time                                  |
| Automation Tool (Zapier/Make.com) | Connects WhatsApp messages to Google Sheets                            |
| Optional CRM Sync         | For storing recurring customer details                                      |

---

## 📊 Benefits for BVS Butchery Ghana

- **Structured ordering flow** that guides users through the process
- **Improved accuracy** due to guided menu prompts
- **Real-time logging** of all orders into the cloud
- **Better inventory and fulfillment tracking**
- **Scalable and low-cost solution**

---

## 📱 Sample Customer Message Template (Optional)

To assist customers who prefer a faster way to order:

```
ORDER:
Category: [Beef/Lamb/Chicken]
Items:
- [Quantity] [Product Name]
- [Quantity] [Product Name]
```

---

Would you like me to provide:
- A **template Google Sheet structure**?
- A **Zapier automation setup guide**?
- Or a **dialogflow chatbot flow** for this use case?

Let me know how you'd like to proceed!
