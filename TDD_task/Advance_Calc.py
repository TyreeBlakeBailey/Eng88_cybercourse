class Adavance_calc:

    def cm_to_inches(self, Num1):
        return Num1 * 2.54

    def modular(self, Num1, Num2):
        if Num1 % Num2 == 0:
            return True
        else:
            return False

    def triangle(self, Num1, Num2):
        return (Num1*Num2)/2

    def percentage(self, Num1, Num2):
        return (Num1 / 100)*Num2
