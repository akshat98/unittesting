from dataclasses import dataclass, field
import uuid


@dataclass
class Person:
    name: str
    address: str
    is_alive: bool = True
    email: list[str]  = field(default_factory = list)
    id: str =  field(init=False, default_factory=uuid.uuid4)
    


p1 = Person("aks","tokyo",True, ['johis@gmai.com','joshi@takeme.com'])
p2 = Person("spencer","tokyo",True, ['spencer@gmai.com','spencer@takeme.com'])

print(p1 , '\n', p2)