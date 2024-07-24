from data.repositories.product.delete import DeleteRepository
from data.repositories.product.find_id import FindByIdRepository


class FindIdUseCase():

    def get_id(self, id: int):
        return FindByIdRepository().product_by_id(id)
        