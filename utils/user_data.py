import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def _read_json(path):
    full_path = BASE_DIR / path
    if not full_path.exists():
        return {}
    with full_path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def _write_json(path, data):
    full_path = BASE_DIR / path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    with full_path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)


def _is_mission_completed(mission):
    if "completed" in mission:
        return bool(mission["completed"])

    if "progress" in mission:
        progress = mission["progress"]

        if isinstance(progress, bool):
            return progress

        if isinstance(progress, (int, float)):
            return progress >= 1

        if isinstance(progress, str):
            return progress.strip().lower() in {"done", "completed", "finished", "true", "1", "yes"}

    return False


def load_missions():
    missions = _read_json("data/missions.json")
    return missions if isinstance(missions, list) else []


def load_user_profile():
    profile = _read_json("data/user_profile.json")
    return profile if isinstance(profile, dict) else {}


def save_user_profile(profile):
    _write_json("data/user_profile.json", profile)


def load_leaderboard():
    rows = _read_json("data/leaderboard.json")
    return rows if isinstance(rows, list) else []


def save_leaderboard(rows):
    _write_json("data/leaderboard.json", rows)


def build_dashboard_data():
    missions = load_missions()
    profile = load_user_profile()

    completed_missions = [m for m in missions if _is_mission_completed(m)]
    total_xp = sum(int(m.get("xp", 0)) for m in completed_missions)
    completed_count = len(completed_missions)
    completion_rate = round((completed_count / len(missions) * 100), 1) if missions else 0

    skill_points = {
        "python": 0,
        "sql": 0,
        "data_visualization": 0,
    }

    for mission in completed_missions:
        title = mission.get("title", "").lower()
        xp = int(mission.get("xp", 0))

        if "python" in title:
            skill_points["python"] += xp
        if "sql" in title:
            skill_points["sql"] += xp
        if "visual" in title or "data" in title:
            skill_points["data_visualization"] += xp

    stored_skills = profile.get("skills", {})
    if isinstance(stored_skills, dict):
        for key in skill_points:
            if key in stored_skills:
                skill_points[key] = int(stored_skills.get(key, 0))

    return {
        "profile": profile,
        "missions": missions,
        "completed_missions": completed_missions,
        "total_missions": len(missions),
        "completed_count": completed_count,
        "completion_rate": completion_rate,
        "total_xp": total_xp,
        "skill_points": skill_points,
    }