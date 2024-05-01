import uuid


def qr_str(tournament_id: int, user_id: int):
    return f"{tournament_id}-{user_id}-{str(uuid.uuid4())}"
