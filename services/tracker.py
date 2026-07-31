import requests


# ==========================================
# GitHub API
# ==========================================
def get_github_data(username):

    try:

        url = f"https://api.github.com/users/{username}"

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()

        return {
            "public_repos": data.get("public_repos", 0),
            "followers": data.get("followers", 0),
            "following": data.get("following", 0)
        }

    except:
        return None


# ==========================================
# LeetCode GraphQL
# ==========================================
def get_leetcode_data(username):

    try:

        url = "https://leetcode.com/graphql"

        headers = {
            "Content-Type": "application/json",
            "Referer": "https://leetcode.com",
            "User-Agent": "Mozilla/5.0"
        }

        query = """
        query userProblemsSolved($username: String!) {
          matchedUser(username: $username) {

            profile {
              ranking
            }

            submitStats {
              acSubmissionNum {
                difficulty
                count
              }
            }

          }
        }
        """

        payload = {
            "query": query,
            "variables": {
                "username": username
            }
        }

        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            return None

        data = response.json()

        user = data["data"]["matchedUser"]

        if user is None:
            return None

        stats = user["submitStats"]["acSubmissionNum"]

        return {

            "totalSolved": stats[0]["count"],

            "easySolved": stats[1]["count"],

            "mediumSolved": stats[2]["count"],

            "hardSolved": stats[3]["count"],

            "ranking": user["profile"]["ranking"]

        }

    except:

        return None