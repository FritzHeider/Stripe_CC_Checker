import stripe
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set your Stripe secret key from environment variable
stripe.api_key = os.getenv('STRIPE_API_KEY')

def check_payment_method(payment_token):
    try:
        print(f"Checking payment method for token: {payment_token}")
        payment_method = stripe.PaymentMethod.retrieve(payment_token)
        setup_intent = stripe.SetupIntent.create(
            payment_method=payment_method.id,
            confirm=True,
            usage='off_session'
        )
        if setup_intent.status == 'succeeded':
            print(f"Token {payment_token} is valid.")
            return 'Valid'
        else:
            print(f"Token {payment_token} is invalid.")
            return 'Invalid'
    except stripe.error.StripeError as e:
        print(f"Error with token {payment_token}: {str(e)}")
        return f'Error: {str(e)}'

def main():
    print("Launching file selector...")
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select file with tokenized payment methods")
    
    if not file_path:
        print("No file selected, exiting.")
        return

    print(f"File selected: {file_path}")
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f'payment_status_{date_str}.txt'
    print(f"Output will be written to {output_file}")

    with open(file_path, 'r') as file, open(output_file, 'w') as outfile:
        for line in file:
            token = line.strip()
            if token:
                status = check_payment_method(token)
                outfile.write(f'{token}: {status}\n')

    print("All tokens processed. Check the output file for results.")

if __name__ == '__main__':
    main()
