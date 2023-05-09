class Calculator:
    
    def validation_type_number(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            return True
        elif isinstance(x, float) and isinstance(y, float):
            return True
        else:
            return False

    def sum(self, x:int, y:int) -> int or float:
        if self.validation_type_number(x, y):
            return x + y

    def subtraction(self, x, y):
        if self.validation_type_number(x, y):
            return x - y

    def multiplication(self, x, y):
        if self.validation_type_number(x, y):
            return x * y

    def division(self, x, y):
        if self.validation_type_number(x, y):
            try:
                return round(x / y, 2)
            except ZeroDivisionError:
                return None

