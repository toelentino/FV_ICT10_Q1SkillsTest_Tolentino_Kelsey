from pyscript import document

# Product prices dictionary
products = {
    "One Piece": 599,
    "Fruits Basket": 500,
    "Bleach": 599,
    "Horimiya": 550,
    "Kimi ni Todoke": 500
}

def process_order(event):
    # This is to clear previous output
    document.querySelector("#output").innerText = ""

    # This is to get customer info
    name = document.querySelector("#cust_name").value
    address = document.querySelector("#cust_address").value
    contact = document.querySelector("#cust_contact").value

    # This is to get the selected items
    checkboxes = document.querySelectorAll("input[type=checkbox]:checked")
    selected_items = [cb.value for cb in checkboxes]

    if not selected_items:
        document.querySelector("#output").innerText = "‼️ Please select at least one item."
        return

    # This is for computing subtotal, tax, and total of the customer's order
    subtotal = sum(products[item] for item in selected_items)
    tax_rate = 0.07
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount

    # This is to build the list of items with line breaks
    items_list = "\n- ".join(selected_items)

    # This is to build a summary using MULTILINE STRING
    summary = f"""📝 Order Summary
--------------------------
👤 Name: {name}
🏠 Address: {address}
📞 Contact: {contact}

📚 Items Ordered:
- {items_list}

Subtotal: ₱{subtotal:.2f}
Tax (7%): ₱{tax_amount:.2f}
Total: ₱{total:.2f}

🐱 Thank you for ordering from The Pining Shelf! 
"""

    # Display result for customer's order
    document.querySelector("#output").innerText = summary