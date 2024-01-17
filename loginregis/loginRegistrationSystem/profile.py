import pymysql
import tkinter as tk


def show_profile(id):
    # Connect to the database
    db = pymysql.connect(host='localhost', user='root', password='kkuunn123', db='userdata')

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to retrieve user information
    query = f"SELECT * FROM data1 WHERE id = {id}"
    cursor.execute(query)

    # Fetch the result and store it in a variable
    result = cursor.fetchone()

    # Close the cursor and database connection
    cursor.close()
    db.close()

    # Create a Tkinter window to display user profile
    profile_window = tk.Tk()
    profile_window.title("User Profile")

    # Create labels to display user information
    name_label = tk.Label(profile_window, text="Name: " + result[1])
    email_label = tk.Label(profile_window, text="Email: " + result[2])
    phone_label = tk.Label(profile_window, text="Phone: " + result[3])

    # Add labels to the window
    name_label.pack()
    email_label.pack()
    phone_label.pack()

    # Display the window
    profile_window.mainloop()


# Call the function with a user ID to display their profile
show_profile(1)
