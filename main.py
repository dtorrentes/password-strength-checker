import re
import getpass

def check_password_strength(password):
    """
    Evaluates the strength of a password based on multiple criteria.
    Returns a score (0–5) and feedback messages.
    """

    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append(
            "Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>)."
        )

    return score, feedback


def get_strength_label(score):
    """Returns a human-readable label for the password strength."""
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"


def main():
    print("\n--- Password Strength Checker ---")
    print("Please enter a password to evaluate.\n")

    try:
        password = getpass.getpass("Enter Password: ")
    except Exception:
        print("Error reading secure input.")
        return

    if not password:
        print("No password entered.")
        return

    score, feedback = check_password_strength(password)
    label = get_strength_label(score)

    print("\n--- Results ---")
    print(f"Strength Rating: {label} ({score}/5)")

    if feedback:
        print("\nSuggestions to improve your password:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("\nGreat job! Your password meets all recommended criteria.")


if __name__ == "__main__":
    main()
