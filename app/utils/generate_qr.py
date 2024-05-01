import uuid


def qr_str(tournament_id: int, user_id: int, is_competitor: bool = True):
    if is_competitor:
        return f"{tournament_id}-{user_id}-{str(uuid.uuid4())}"

    return f"{tournament_id}-{user_id}-{str(uuid.uuid4())}"
