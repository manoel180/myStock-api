from typing import List
from data.repositories.product.find_all import FindAllRepository
from domain.product import ProductModel

class FindAllUseCase():

    def find_all(self) -> List[ProductModel]:
        
        return FindAllRepository().get_products()