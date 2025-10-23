from sqlmodel import Session

from app.common.dao.basic_dao import BasicDao
from app.modules.user.models import Users

class UserDao(BasicDao[Users]):
    def __init__(self):
        super().__init__(Users)

    def save_user(self, session, user: Users):
        print(f"Saving user: {user.name}")
        return self.save(session,user)

    def get_by_id(self,session:Session,id:int):
        return self.find_by_id(self,session,id)