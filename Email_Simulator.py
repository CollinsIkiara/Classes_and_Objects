# Email Simulator

# This program simulates a simple email system where users can send, receive, read, and delete emails.
import datetime

# Define the Email class to represent an email message
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False

    def mark_as_read(self):
        self.read = True

    def display_full_email(self):
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self): # This method defines how the email is displayed in the inbox list
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

# Define the Inbox class to manage received emails for a user
class Inbox:
    def __init__(self): # Initialize an empty list to store received emails
        self.emails = []

    def receive_email(self, email): # Add a new email to the inbox
        self.emails.append(email)

    def list_emails(self): # Display a list of all emails in the inbox with their status, sender, subject, and timestamp if there are any emails, otherwise indicate that the inbox is empty
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')


    def read_email(self, index): # Read a specific email by its index in the inbox list, marking it as read and displaying its full content. If the index is invalid or the inbox is empty, display an appropriate message.
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        self.emails[actual_index].display_full_email()

    def delete_email(self, index): # Delete a specific email by its index in the inbox list. If the index is invalid or the inbox is empty, display an appropriate message.
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        del self.emails[actual_index]
        print('Email deleted.\n')
        
# Define the User class to represent a user in the email system, allowing them to send emails, check their inbox, read specific emails, and delete emails.
class User:
    def __init__(self, name): # Initialize the user with a name and an empty inbox
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body): # Create a new email and send it to the receiver's inbox, then print a confirmation message
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self): # Display the contents of the user's inbox, showing all received emails with their status, sender, subject, and timestamp. If the inbox is empty, indicate that as well.
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index): # Read a specific email from the inbox by its index, marking it as read and displaying its full content. If the index is invalid or the inbox is empty, display an appropriate message.
        self.inbox.read_email(index)

    def delete_email(self, index): # Delete a specific email from the inbox by its index. If the index is invalid or the inbox is empty, display an appropriate message.
        self.inbox.delete_email(index)

# Main function to demonstrate the email simulator with two users, Tory and Ramy, sending and receiving emails, checking their inboxes, reading specific emails, and deleting emails. It mainly implements the class User and its interactions with the Inbox and Email classes to simulate a simple email system.
def main():
    tory = User('Tory')
    ramy = User('Ramy')        
    
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()    
    
if __name__ == '__main__': # This condition ensures that the main function is only executed when the script is run directly, and not when it is imported as a module in another script.
    main()