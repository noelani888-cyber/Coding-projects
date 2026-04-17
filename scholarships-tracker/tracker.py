scholarships = []

def add_scholarship(name, deadline, amount):
    scholarships.append({
        "name": name,
        "deadline": deadline,
        "amount": amount
    })

def view_scholarships():
    if not scholarships:
        print("No scholarships added.")
        return

    for s in scholarships:
        print(f"{s['name']} | Deadline: {s['deadline']} | ${s['amount']}")

def total_amount():
    return sum(s["amount"] for s in scholarships)
