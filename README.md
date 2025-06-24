# ☕ GCU Coffee Machine

A Python-based coffee machine simulator built using Object-Oriented Programming principles. This project demonstrates core OOP concepts including classes, encapsulation, and state management.

## 🚀 Features

- **Three Coffee Options**: Espresso, Latte, and Cappuccino
- **Resource Management**: Tracks water, milk, and coffee inventory
- **Payment System**: Handles transactions with change calculation
- **Order History**: Maintains record of last 5 orders with timestamps
- **Admin Report**: Protected admin access to view machine status and sales
- **Input Validation**: Handles invalid inputs gracefully

## 🛠️ Technologies Used

- Python 3.x
- Object-Oriented Programming (OOP)
- Time module for timestamps

## 📋 Prerequisites

- Python 3.6 or higher installed on your system

## 🔧 Installation & Setup

1. Clone this repository:
```bash
git clone https://github.com/jaweriafayyaz/coffee-machine.git
cd coffee-machine
```

2. Run the program:
```bash
python coffee_machine.py
```

## 🎮 How to Use

1. **Start the Program**: Run the script and you'll see the welcome message
2. **Order Coffee**: Type `espresso`, `latte`, or `cappuccino`
3. **Make Payment**: Enter the amount when prompted
4. **View History**: Type `history` to see recent orders
5. **Admin Report**: Type `report` and enter password `gcuadmin`
6. **Exit**: Type `exit` to quit

### Sample Usage:
```
👋 Welcome to GCU Coffee Machine!

Enter drink name (espresso/latte/cappuccino), 'report', 'history', or 'exit': latte
💰 Please pay Rs 200
Enter amount: Rs 250
💸 Here is your change: Rs 50
✅ Here's your Latte! Enjoy ☕
```

## 📊 Menu & Pricing

| Drink | Water (ml) | Milk (ml) | Coffee (g) | Price (Rs) |
|-------|------------|-----------|------------|------------|
| Espresso | 50 | 0 | 18 | 100 |
| Latte | 200 | 150 | 24 | 200 |
| Cappuccino | 250 | 100 | 24 | 250 |

## 🏗️ Project Structure

```
coffee-machine/
│
├── coffee_machine.py    # Main application file
├── README.md           # Project documentation
└── .gitignore         # Git ignore file
```

## 🔍 OOP Concepts Demonstrated

- **Classes**: `Drink`, `Order`, `CoffeeMachine`
- **Encapsulation**: Private data with public methods
- **Composition**: Orders contain drink objects
- **State Management**: Resource tracking and money collection
- **Method Organization**: Logical grouping of functionality

## 🚀 Future Enhancements

- [ ] Add unit tests
- [ ] Implement data persistence (save/load orders)
- [ ] Add more drink options
- [ ] GUI interface using tkinter
- [ ] Multiple payment methods
- [ ] Inventory alerts and restocking

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Jaweria Fayyaz**
- GitHub: [@jaweriafayyaz](https://github.com/jaweriafayyaz)
- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/jaweria-fayyaz/)

## 🎓 Academic Project

This project was developed as part of my Object-Oriented Programming coursework at GCU (Government College University). It showcases fundamental OOP principles and Python programming skills.

---

⭐ **If you found this project helpful, please give it a star!** ⭐
