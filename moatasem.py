def collect_user_info():
    user_info = {}

    # Bad Habits
    while True:
        print("Do you have any bad habits? (yes/no)")
        bad_habits = input().lower()
        if bad_habits in ["yes", "no"]:
            if bad_habits == "yes":
                user_info["bad_habits"] = input("Please describe your bad habits: ")
            else:
                user_info["bad_habits"] = "None"
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Job
    while True:
        user_info["job"] = input("What is your job title? ")
        if user_info["job"].strip() != "":
            break
        else:
            print("Invalid input. Please enter a valid job title.")

    # Family Role
    while True:
        print("What is your family role? (e.g. mother, father, sibling, etc.)")
        user_info["family_role"] = input()
        if user_info["family_role"].strip() != "":
            break
        else:
            print("Invalid input. Please enter a valid family role.")

    # Allergies
    while True:
        print("Do you have any allergies? (yes/no)")
        allergies = input().lower()
        if allergies in ["yes", "no"]:
            if allergies == "yes":
                user_info["allergies"] = input("Please describe your allergies: ")
            else:
                user_info["allergies"] = "None"
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Other Relevant Information
    while True:
        user_info["other_info"] = input("Is there any other relevant information you'd like to share? ")
        if user_info["other_info"].strip() != "":
            break
        else:
            print("Invalid input. Please enter some information.")
        
    return user_info
def program():
    user_info = {}

    while True:
        name = input("What's your name?")
        if name.isalpha():  # Check if the input contains only letters
            user_info["name"] = name.upper()
            break
        else:
            print("Invalid input. Please enter your name.")

    while True:
        code = input("Enter your cash code:")
        if code:  # Check if the input is not empty
            user_info["cash_code"] = code
            break
        else:
            print("Invalid input. Please enter your cash code.")

    while True:
        email = input("Enter your email address:")
        if "@" in email and email.count("@") == 1:
            local_part, domain = email.split("@")
            if local_part and domain:  # Check if there's something before and after the @ symbol
                domain_parts = domain.split(".")
                if len(domain_parts) == 2:  # Check if there's a top-level domain
                    tld = domain_parts[1]
                    if tld in ["com", "org", "net", "edu", "gov", "mil", "biz", "info"]:  # Check if the TLD is valid
                        user_info["email"] = email
                        break
                    else:
                        print("Invalid email address. Please use a valid top-level domain (e.g. .com, .org, etc.).")
                else:
                    print("Invalid email address. Please enter a valid domain (e.g. example.com).")
            else:
                print("Invalid email address. Please enter something before and after the @ symbol.")
        else:
            print("Invalid email address. Please try again.")

    print("\nUser Information:")
    for key, value in user_info.items():
        print(f"{key.capitalize()}: {value}")

program()
user_info = collect_user_info()
print("Bad Habits:", user_info["bad_habits"])
print("Job:", user_info["job"])
print("Family Role:", user_info["family_role"])
print("Allergies:", user_info["allergies"])
print("Other Relevant Information:", user_info["other_info"])