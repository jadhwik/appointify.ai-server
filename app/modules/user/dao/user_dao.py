from fastapi_pagination import Page, Params
from fastapi_pagination.ext.sqlalchemy import paginate  # Remove the alias
from sqlmodel import Session

from app.common.criteria import BaseCriteria
from app.common.dao.basic_dao import BasicDao
from app.modules.user.misc import UserFilter
from app.modules.user.models import Users

class UserDao(BasicDao[Users]):
    def __init__(self):
        super().__init__(Users)

    def save_user(self, session, user: Users):
        print(f"Saving user: {user.name}")
        return self.save(session, user)

    def get_by_id(self, session: Session, id: int):
        return self.find_by_id(self, session, id)

    def search(self, session: Session, filters: UserFilter) -> Page[Users]:
        base_criteria = BaseCriteria(Users)
        base_criteria.eq("name", filters.name)
        base_criteria.eq('phone', filters.phone)
        query = base_criteria.build()
        params = Params(page=filters.page, size=filters.rows)
        return paginate(session, query, params)