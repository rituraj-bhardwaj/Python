# Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter password: ")

if len(password) < 6:
    print(" Strength: Weak")
elif len(password) >= 6 < 10:
    print("Strength: Medium")
else:
    print("Strength: String")