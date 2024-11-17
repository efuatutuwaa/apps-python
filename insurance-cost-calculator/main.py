import yaml

class InsuranceCalculator:
    def __init__(self, name, age, sex, bmi, num_of_kids, smoker, market_parameter, age_parameter, sex_parameter,
                 bmi_parameter, num_kids_parameter, smoker_parameter):
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_of_kids = num_of_kids
        self.smoker = smoker
        self.market_parameter = market_parameter
        self.age_parameter = age_parameter
        self.sex_parameter = sex_parameter
        self.bmi_parameter = bmi_parameter
        self.num_kids_parameter = num_kids_parameter
        self.smoker_parameter = smoker_parameter

    def __str__(self):
        return f"Insurance model : {self.name}{(self.age)}"

    def calculate_insurance_cost(self):
        estimated_cost = self.market_parameter * self.age - self.age_parameter * self.sex + self.sex_parameter * self.bmi + self.bmi_parameter * self.num_of_kids + self.num_kids_parameter * self.smoker - self.smoker_parameter
        print(f"The estimated insurance cost for {self.name} is {estimated_cost}")
        return estimated_cost


def mathematical_parameters():
    print("Hello, I am an insurance calculator!! Please enter the mathematical parameters")
    market_parameter = int(input("Enter the market parameter"))
    age_parameter = int(input("Enter the age parameter"))
    sex_parameter = int(input("Enter the sex parameter"))
    bmi_parameter = int(input("Enter the bmi parameter"))
    num_kids_parameter = int(input("Enter the number of kids parameter"))
    smoker_parameter = int(input("Enter the smoker parameter"))
    return market_parameter, age_parameter, sex_parameter, bmi_parameter, num_kids_parameter, smoker_parameter


def get_user_input():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    sex = int(input("Enter your sex (0 for female, 1 for male): "))
    bmi = float(input("Enter your BMI: "))
    num_of_kids = int(input("Enter the number of children: "))
    smoker = int(input("Are you a smoker? (0 for non-smoker, 1 for smoker): "))
    return name, age, sex, bmi, num_of_kids, smoker


def main():
    with open("config.yml") as file:
        config = yaml.safe_load(file)
    age_parameter = config['age_parameter']
    sex_parameter = config['sex_parameter']
    bmi_parameter = config['bmi_parameter']
    market_parameter = config['market_parameter']
    smoker_parameter = config['smoker_parameter']
    num_kids_parameter = config['num_kids_parameter']
    # market_parameter,age_parameter,sex_parameter,bmi_parameter,num_kids_parameter,smoker_parameter = mathematical_parameters()
    print("Welcome to the Insurance Cost Calculator!")
    name, age, sex, bmi, num_of_kids, smoker = get_user_input()
    my_insurance_cal = InsuranceCalculator(name, age, sex, bmi, num_of_kids, smoker, market_parameter, age_parameter,
                                           sex_parameter,
                                           bmi_parameter, num_kids_parameter, smoker_parameter)
    my_insurance_cal.calculate_insurance_cost()
    print(my_insurance_cal)

if __name__ == "__main__":
     main()