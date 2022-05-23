"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП."""


class MyError(Exception):
    # class for error if data was imputed incorrectly
    def __init__(self, message):
        self.message = message


class EquipmentStorage:

    def __init__(self, equipment_type, quantity):
        self.equipment_type = equipment_type
        self.quantity = quantity
        self.location = {"Storage": quantity}

    def to_storage(self):
        # new location of equipment
        to_place = input(
            f"Please enter where {self.equipment_type} should be put. For example Room, Archive, etc.\n")\
            .title()
        # from where equipment should be replaced.
        while True:
            from_place = input(
                f"Please enter from where {self.equipment_type} should be replace. Available: "
                f"{list(self.location.keys())}.\n").title()
            if self.location.__contains__(from_place.title()):
                break
            else:
                print(f'No {self.equipment_type} at {from_place.title()} now. Please select another location')

        # quantity of equipment to be replaced. inputting in a loop till correct quantity
        while True:
            try:
                quantity = int(input(
                    f'Please enter quantity of {self.equipment_type} to replace. Currently available:'
                    f' {self.location.get(from_place)}.\n'))
                if quantity < 1:
                    raise MyError("quantity should be more than 0")
                elif self.location[from_place.title()] < quantity:
                    raise MyError(
                        f"It is not possible to move {quantity} {self.equipment_type} to {to_place.title()}.\n"
                        f"Current available numbers of {self.equipment_type} at {from_place.title()} is"
                        f" {self.location.get(from_place.title())}.\n")
            except MyError as e:
                print(e)
            except Exception as e:
                print(e)
            else:
                break
        # changing quantity in items
        self.location[to_place.title()] = quantity
        self.location[from_place.title()] -= quantity
        print(f'{quantity} {self.equipment_type} were moved to {to_place.title()}. \n Current status is:'
              f' {self.location}\n')


class Printers(EquipmentStorage):
    def __init__(self, equipment_type, quantity, color):
        super().__init__(equipment_type, quantity)
        self.color = color


class Scanners(EquipmentStorage):
    def __init__(self, equipment_type, quantity, paper_format):
        super().__init__(equipment_type, quantity)
        self.paper_format = paper_format


class Xerox(EquipmentStorage):
    def __init__(self, equipment_type, quantity, sides):
        super().__init__(equipment_type, quantity)
        self.sides = sides


# creating class items
printers_group1 = Printers('Printer', 4, 'multicolor')
scanners_group1 = Scanners('Scanner', 4, 'A4')
xerox_group1 = Xerox('Xerox', 4, 2)

# creating user's interface
print(
    f'\n Current status\n{printers_group1.equipment_type}: {printers_group1.location}\n'
    f'{scanners_group1.equipment_type}: {scanners_group1.location}\n{xerox_group1.equipment_type}:'
    f' {xerox_group1.location}\n')

while True:
    equipment_type = input(
        f'Enter equipment you want to move (available equipment: {printers_group1.equipment_type}, '
        f'{scanners_group1.equipment_type}, {xerox_group1.equipment_type}): ').lower()
    if equipment_type == printers_group1.equipment_type.lower():
        printers_group1.to_storage()
    elif equipment_type == scanners_group1.equipment_type.lower():
        scanners_group1.to_storage()
    elif equipment_type == xerox_group1.equipment_type.lower():
        xerox_group1.to_storage()
    else:
        print(f'There is no {equipment_type}.')
