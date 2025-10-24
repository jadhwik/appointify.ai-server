from typing import Any, List, Type, TypeVar, Generic
from pydantic import BaseModel
from app.common.shared.mapper_config import MapperConfig

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
EntityType = TypeVar("EntityType", bound=BaseModel)
ResponseSchemaType = TypeVar("ResponseSchemaType", bound=BaseModel)


class BaseMapper(Generic[CreateSchemaType, EntityType, ResponseSchemaType]):

    def __init__(
        self,
        create_schema: Type[CreateSchemaType],
        entity: Type[EntityType],
        response_schema: Type[ResponseSchemaType],
        ignore_fields: List[str] = None
    ):
        self.create_schema = create_schema
        self.entity = entity
        self.response_schema = response_schema
        self.ignore_fields = set(MapperConfig.IGNORE_COMMON_FIELDS)
        if ignore_fields:
            self.ignore_fields.update(ignore_fields)

    def to_entity(self, dto: CreateSchemaType, **extra_fields) -> EntityType:
        data = dto.model_dump(exclude_unset=True, exclude_none=True)
        for field in self.ignore_fields:
            data.pop(field, None)
        for field, func in MapperConfig.custom_for_creation().items():
            if field not in data:
                data[field] = func(dto)

            data.update(extra_fields)
        return self.entity(**data)

    def update_entity(self, existing: EntityType, update_dto: BaseModel) -> EntityType:
        update_data = update_dto.model_dump(exclude_unset=True, exclude_none=True)
        for field in self.ignore_fields:
            update_data.pop(field, None)

        for field, value in update_data.items():
            if hasattr(existing, field):
                setattr(existing, field, value)
        return existing

    def to_response(self, entity: EntityType) -> ResponseSchemaType:
        data = entity.model_dump()
        for field, func in MapperConfig.custom_for_view().items():
            data[field] = func(entity)
        return self.response_schema.model_validate(data)

    def to_response_list(self, entities: List[EntityType]) -> List[ResponseSchemaType]:
        return [self.to_response(e) for e in entities]
