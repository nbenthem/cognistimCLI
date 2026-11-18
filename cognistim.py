

# 1. NATALIA: USER PROFILE MANAGEMENT

def manage_user_profile(name: str, age: int) -> dict:
    """
    Create a user profile with initial training statistics.

    Args:
        name (str): The user's name.
        age (int): The user's age in years.

    Returns:
        dict: A dictionary containing the user's personal
              information and initial training statistics.
    """

    # Create a dictionary to store all the user's information.
    # Each key identifies a different piece of information:
    # name: stores the user's name.
    # age: stores the user's age.
    # total_score: starts at 0 and stores the points earned.
    # completed_activities: starts at 0 and counts completed exercises.
    profile = {
        "name": name.strip().title(),
        "age": age,
        "total_score": 0,
        "completed_activities": 0
    }

    # Display a welcome message using the user's name.
    print(f"\nWe're glad to have you here, {profile['name']}! Welcome to Cognistim.")

    # Return the complete profile so other functions can use it.
    return profile


# 2. IVÁN: READING COMPREHENSION EXERCISE

def run_reading_exercise() -> int:
    """
    Display a short text and test the user's reading comprehension.

    Args:
        None.

    Returns:
        int: 10 points if the answer is correct, or 0 otherwise.
    """

    print("\nREADING EXERCISE\n")

    # Store the text that the user must read and understand.
    text = (
        "Manolo is 78 years old. Every morning, "
        "he reads the newspaper and solves memory puzzles "
        "to keep his mind active."
    )

    # Display the reading text.
    print("Read the following text carefully:\n")
    print(text)

    # Wait until the user has finished reading.
    input("\nPress ENTER when you are ready to answer...")

    # Display the comprehension question and its three options.
    print("\nQuestion: What does Manolo do every morning?")
    print("A) He watches television.")
    print("B) He reads the newspaper and solves puzzles.")
    print("C) He goes swimming.")

    # Check that the user selects one of the available options.
    # If the input is invalid, ask again.
    while True:
        answer = input("\nChoose A, B or C: ").strip().upper()

        if answer not in ["A", "B", "C"]:
            print("Invalid option. Please choose A, B or C.")
            continue

        break

    # Store the correct answer for comparison.
    correct_answer = "B"

    # Compare the user's answer with the correct one.
    if answer == correct_answer:
        print("Correct! Well done!")
        return 10
    else:
        print("Not quite right! Good effort! Keep practising!")
        return 0


# 3. CAROL: WORD & MEMORY CHALLENGE

def check_memory_word() -> bool:
    """
    Test the user's ability to memorize and recall a word.

    Args:
        None.

    Returns:
        bool: True if the recalled word is correct, False otherwise.
    """

    # Store the original word that the user must memorize.
    original_word = "GARDEN"

    print("\nMEMORY CHALLENGE\n")
    print("Memorize this word:")
    print("\n       " + original_word)

    # Wait until the user is ready to continue.
    input("\nPress ENTER when you are ready to continue...")

    # Display asterisks to represent the hidden word.
    print("The word is now hidden:")
    print("\n******")

    # Ask the user to recall the original word.
    # Only alphabetic characters are accepted.
    while True:
        user_recall = input("\nWhich word did you see? ").strip()

        if not user_recall.isalpha():
            print("Please enter a word using letters only.")
            continue

        break

    # Compare the recalled word with the original one.
    # upper() allows the answer to be written in either
    # uppercase or lowercase.
    if user_recall.upper() == original_word:
        print("Excellent memory! Correct answer.")
        return True
    else:
        print(f"Good effort! The correct word was {original_word}.")
        return False


# 4. SAMUEL: MENTAL MATHEMATICS EXERCISE

def evaluate_mental_math(num1: int, num2: int) -> int:
    """
    Test the user's mental arithmetic skills through addition.

    Args:
        num1 (int): The first number in the addition.
        num2 (int): The second number in the addition.

    Returns:
        int: 10 points when the user gives the correct answer.
    """

    # Calculate and store the correct result.
    expected_sum = num1 + num2

    print("\n========== MENTAL MATHEMATICS ==========\n")
    print(f"Calculate: {num1} + {num2}")

    # Allow repeated attempts until the answer is correct.
    while True:

        # Ask the user to enter the result.
        user_input = input("Your answer: ").strip()

        # Convert the input into an integer.
        # If the user enters letters or invalid characters,
        # ValueError is handled and the exercise continues.
        try:
            user_sum = int(user_input)

        except ValueError:
            print("Please enter a valid number. Try again!")
            continue

        # Compare the user's result with the expected sum.
        if user_sum == expected_sum:
            print("Correct! Excellent calculation!")
            return 10

        else:
            print("Not quite! Don't give up, try again!")
            print("You can do it!")


# 5. ALENDAY: UPDATE USER PROGRESS

def update_user_progress(profile: dict, new_points: int) -> dict:
    """
    Update the user's score and completed activities.

    Args:
        profile (dict): The user's current profile and statistics.
        new_points (int): The points earned in the latest activity.

    Returns:
        dict: The updated user profile.
    """

    # Add the points earned in the latest exercise
    # to the user's existing total score.
    profile["total_score"] += new_points

    # Increase the activity counter by one because
    # the user has completed another exercise.
    profile["completed_activities"] += 1

    # Return the profile with its updated statistics.
    return profile


# 6. ADRIÁN: DAILY MOTIVATIONAL REPORT

def generate_motivational_report(profile: dict) -> str:
    """
    Generate a motivational report showing the user's progress.

    Args:
        profile (dict): The user's profile containing their name,
                        score and completed activities.

    Returns:
        str: A motivational message displaying the user's progress.
    """

    # Retrieve the information needed from the user profile.
    name = profile["name"]
    score = profile["total_score"]
    activities = profile["completed_activities"]

    # Build a report using the user's personal information
    # and current training statistics.
    report = (
        f"\nGreat job today, {name}!\n"
        f"You completed {activities} mental exercises "
        f"and earned {score} points.\n"
        "Keep up the wonderful work!"
    )

    # Return the report as a string so it can be displayed.
    return report


# 7. RICCARDO: DAILY ACTIVITY MENU

def show_activity_menu() -> None:
    """
    Display the main menu with all available activities.

    Args:
        None.

    Returns:
        None.
    """

    # Display the five available menu options.
    print("====================================")
    print("       COGNISTIM BRAIN TRAINING")
    print("====================================")
    print("1. Reading comprehension")
    print("2. Memory challenge")
    print("3. Mental mathematics")
    print("4. View daily progress")
    print("5. Exit")
    print("====================================")


# MAIN PROGRAM

if __name__ == "__main__":

    print("\nWelcome to the Cognistim Training App!")

    # Ask for the user's name and remove unnecessary spaces.
    name = input("Enter your name: ").strip()

    # Prevent the user from continuing with an empty name.
    while not name:
        print("Please enter a valid name.")
        name = input("Enter your name: ").strip()

    # Ask for the user's age and validate the input.
    while True:
        age_input = input("Enter your age: ").strip()

        try:
            # Convert the entered age into an integer.
            age = int(age_input)

            # Only accept positive ages.
            if age <= 0:
                print("Please enter a valid positive age.")
                continue

            break

        except ValueError:
            # Ask again if the input is not a valid integer.
            print("Please enter a valid number for your age.")

    # Create the user's profile with the validated information.
    user_profile = manage_user_profile(name, age)

    # Keep the application running until the user chooses to exit.
    while True:

        # Display the main menu before each selection.
        show_activity_menu()

        # Ask the user which activity they want to perform.
        choice = input("Choose an activity (1-5): ").strip()

        if choice == "1":

            # Run the reading exercise and receive the earned points.
            points = run_reading_exercise()

            # Add the points and completed activity to the profile.
            user_profile = update_user_progress(
                user_profile, points
            )

        elif choice == "2":

            # Run the memory exercise and receive its True/False result.
            correct = check_memory_word()

            # Award 10 points for a correct answer or 5 for an incorrect one.
            points = 10 if correct else 5

            # Update the user's training statistics.
            user_profile = update_user_progress(
                user_profile, points
            )

        elif choice == "3":

            # Run the addition exercise using the numbers 12 and 8.
            points = evaluate_mental_math(12, 8)

            # Update the user's score and completed activities.
            user_profile = update_user_progress(
                user_profile, points
            )

        elif choice == "4":

            # Generate and display the current progress report.
            print(generate_motivational_report(user_profile))

        elif choice == "5":

            # Display the final report before closing the application.
            print(generate_motivational_report(user_profile))
            print("\nThank you for training your mind today!")
            break

        else:

            # Inform the user if the selected menu option is invalid.
            print("Invalid option. Please choose a number from 1 to 5.")