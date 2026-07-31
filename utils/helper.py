import json
import os


def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def save_json(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def update_leaderboard(user):

    leaderboard_file = "data/leaderboard.json"

    if not os.path.exists(leaderboard_file):
        save_json(leaderboard_file, [])

    leaderboard = load_json(leaderboard_file)

    found = False

    for player in leaderboard:

        if player["name"] == user["name"]:

            player["xp"] = user["xp"]
            player["level"] = user["level"]
            player["rank"] = user["rank"]
            player["problemsSolved"] = user["problemsSolved"]

            found = True
            break

    if not found:

        leaderboard.append({
            "name": user["name"],
            "xp": user["xp"],
            "level": user["level"],
            "rank": user["rank"],
            "problemsSolved": user["problemsSolved"]
        })

    leaderboard = sorted(
        leaderboard,
        key=lambda x: x["xp"],
        reverse=True
    )

    save_json(leaderboard_file, leaderboard)