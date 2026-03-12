# Python OOP Concepts – Learning Projects

A collection of beginner-to-intermediate Python scripts that demonstrate core **Object-Oriented Programming (OOP)** concepts including classes, instances, methods, encapsulation, and class interactions.

---

## 📁 Files Overview

| File | Concept | Difficulty |
|------|---------|------------|
| `Musical_Instrument_Inventory.py` | Intro to classes & methods | Beginner |
| `Planet_Class.py` | Input validation & `__str__` | Beginner–Intermediate |
| `Email_Simulator.py` | Multi-class systems & encapsulation | Intermediate |

---

## 🎵 Musical_Instrument_Inventory.py

### Description
A simple introduction to defining and using Python classes. This script models musical instruments and demonstrates how to create objects (instances) and call methods on them.

### Key Concepts
- **Class definition** with `__init__` constructor
- **Instance variables** (`name`, `instrument_type`)
- **Methods** that `print` directly (`play`) vs. **methods that `return` a string** (`get_fact`)

### How It Works
1. The `MusicalInstrument` class is defined with two attributes: `name` and `instrument_type`.
2. Two instrument objects are instantiated — an Oboe and a Trumpet.
3. The `play()` method prints a message directly.
4. The `get_fact()` method *returns* a string, so it must be wrapped in `print()` to display output.

### Sample Output
```
The Oboe is fun to play!
The Oboe is part of the woodwind family of instruments.
The Trumpet is fun to play!
The Trumpet is part of the brass family of instruments.
```

---

## 🪐 Planet_Class.py

### Description
Extends basic class concepts by adding **input validation** and a custom **string representation** using the `__str__` dunder method. Models planets in a solar system.

### Key Concepts
- **Type checking** with `isinstance()` and raising `TypeError`
- **Value validation** with `raise ValueError` for empty strings
- **Dunder method** `__str__` for human-readable object representation
- Instance methods that `return` formatted strings

### How It Works
1. The `Planet` class validates all three constructor arguments (`name`, `planet_type`, `star`) — they must be non-empty strings; otherwise an exception is raised.
2. `__str__` controls what `print(planet)` displays, giving each object a clean, readable format.
3. The `orbit()` method returns a descriptive string about the planet's star.
4. Three planets (Earth, Venus, Jupiter) are created and their string representations and orbit info are printed.

### Sample Output
```
Planet: Earth | Type: terrestrial | Star: Sun
Planet: Venus | Type: terrestrial | Star: Sun
Planet: Jupiter | Type: gas | Star: Sun
Earth is orbiting around Sun...
Venus is orbiting around Sun...
Jupiter is orbiting around Sun...
```

---

## 📧 Email_Simulator.py

### Description
A more advanced multi-class system that simulates a basic email application. Demonstrates how multiple classes interact to model a real-world system with **sending, reading, and deleting emails**.

### Key Concepts
- **Multi-class architecture** — `Email`, `Inbox`, and `User` classes work together
- **Encapsulation** — each class manages its own data and responsibilities
- **Object composition** — a `User` *has an* `Inbox`; an `Email` *has a* sender and receiver
- **`datetime` module** for timestamping emails
- **`__str__` dunder method** for inbox list display
- **Index-based operations** with bounds checking

### Classes

#### `Email`
Represents a single email message.
| Attribute/Method | Description |
|---|---|
| `sender`, `receiver` | `User` objects |
| `subject`, `body` | String content |
| `timestamp` | Auto-set on creation via `datetime.now()` |
| `read` | Boolean, starts as `False` |
| `mark_as_read()` | Sets `read = True` |
| `display_full_email()` | Marks as read and prints full email details |
| `__str__()` | Returns a compact summary line for inbox listing |

#### `Inbox`
Manages the list of received emails for one user.
| Method | Description |
|---|---|
| `receive_email(email)` | Appends an email to the inbox list |
| `list_emails()` | Prints all emails or an "inbox is empty" message |
| `read_email(index)` | Displays full email at 1-based index; handles invalid input |
| `delete_email(index)` | Removes email at 1-based index; handles invalid input |

#### `User`
Represents a participant in the email system. Owns an `Inbox` and can send/receive emails.
| Method | Description |
|---|---|
| `send_email(receiver, subject, body)` | Creates an `Email` and delivers it to the receiver's inbox |
| `check_inbox()` | Calls `inbox.list_emails()` |
| `read_email(index)` | Delegates to `inbox.read_email(index)` |
| `delete_email(index)` | Delegates to `inbox.delete_email(index)` |

### How It Works
1. Two users, `Tory` and `Ramy`, are created.
2. Tory sends Ramy an email; Ramy replies to Tory.
3. Ramy checks his inbox (shows 1 unread email).
4. Ramy reads email #1 (status changes to "Read").
5. Ramy deletes email #1.
6. Ramy checks his inbox again (now empty).

### Sample Output
```
Email sent from Tory to Ramy!
Email sent from Ramy to Tory!

Ramy's Inbox:
Your Emails:
1. [Unread] From: Tory | Subject: Hello | Time: 2024-01-15 10:30

--- Email ---
From: Tory
To: Ramy
Subject: Hello
Received: 2024-01-15 10:30
Body: Hi Ramy, just saying hello!
------------

Email deleted.

Ramy's Inbox:
Your inbox is empty.
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher

### Running the Scripts
Each file can be run independently from the terminal:

```bash
python Musical_Instrument_Inventory.py
python Planet_Class.py
python Email_Simulator.py
```

> **Note:** `Musical_Instrument_Inventory.py` and `Planet_Class.py` run their code at the module level (no `main()` function). `Email_Simulator.py` uses the `if __name__ == '__main__':` guard, which is a Python best practice to prevent code from running when the file is imported as a module.

---

## 🧠 OOP Concepts Summary

| Concept | Where Used |
|---|---|
| Class & constructor (`__init__`) | All three files |
| Instance variables | All three files |
| Instance methods | All three files |
| `__str__` dunder method | `Planet_Class.py`, `Email_Simulator.py` |
| Input validation / exceptions | `Planet_Class.py` |
| Object composition | `Email_Simulator.py` |
| Multi-class interaction | `Email_Simulator.py` |
| Standard library (`datetime`) | `Email_Simulator.py` |
| `if __name__ == '__main__'` guard | `Email_Simulator.py` |
