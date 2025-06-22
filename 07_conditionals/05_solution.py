# Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = input("Enter weather condition ['Sunny', 'Rainy', 'Snowy']: ").lower()

if weather == 'sunny':
    print("Go for a walk")
elif weather == 'rainy':
    print("Read a book")
elif weather == 'snowy':
    print('Build a snowman')
else:
    print("No suggestion available")