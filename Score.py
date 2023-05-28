import os

SCORES_FILE = "scores.txt"
POINTS_OF_WINNING = 0


def add_score(difficulty):
    # Calculate points for winning based on the difficulty
    points = (difficulty * 3) + 5

    try:
        # Check if the scores file exists
        if os.path.exists(SCORES_FILE):
            # Read the current score from the file
            with open(SCORES_FILE, "r") as file:
                current_score = int(file.read())
                points += current_score

        # Write the updated score to the file
        with open(SCORES_FILE, "w") as file:
            file.write(str(points))

    except IOError:
        # If reading/writing to the file fails, create a new one and save the current score
        with open(SCORES_FILE, "w") as file:
            file.write(str(points))
