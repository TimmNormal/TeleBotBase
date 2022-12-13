from _db.db_connect import create_connection
from _db.entity import UserAction


def set_action_context(user_id,action):
    delete_action_context(user_id)
    
    db = create_connection()
    user_action = UserAction(user_id = str(user_id),name = action)
    db.add(user_action)
    db.commit()

def delete_action_context(user_id):
    db = create_connection()
    db.query(UserAction).filter(UserAction.user_id == str(user_id)).delete()
    db.commit()


def get_action_context(user_id):
    db = create_connection()
    user_action = db.query(UserAction).filter(UserAction.user_id == str(user_id)).first()
    if user_action:
        return user_action.name
    return None