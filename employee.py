"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
  def __init__(self, name, contract_type, **kwargs):
      self.name = name
      self.contract_type = contract_type
      self.kwargs = kwargs

  def get_pay(self):
      if self.contract_type == "salary":
          total_pay = self.kwargs.get("monthly_salary", 0)
          if "bonus" in self.kwargs:
              total_pay += self.kwargs["bonus"]

          if "contracts" in self.kwargs:
              total_pay += self.kwargs["contracts"] * self.kwargs.get("commission_per_contract", 0)

      elif self.contract_type == "hourly":
          total_pay = self.kwargs.get("hours_worked", 0) * self.kwargs.get("hourly_wage", 0)
          if "bonus" in self.kwargs:
              total_pay += self.kwargs["bonus"]

          if "contracts" in self.kwargs:
              total_pay += self.kwargs["contracts"] * self.kwargs.get("commission_per_contract", 0)

      return total_pay

  def __str__(self):
      if self.contract_type == "salary":
          explanation = f"{self.name} works on a monthly salary of {self.kwargs.get('monthly_salary', 0)}. "
      elif self.contract_type == "hourly":
          explanation = f"{self.name} works on a contract of {self.kwargs.get('hours_worked', 0)} hours at {self.kwargs.get('hourly_wage', 0)}/hour. "

      if "bonus" in self.kwargs:
          explanation += f"and receives a bonus commission of {self.kwargs['bonus']}. "
      if "contracts" in self.kwargs:
          explanation += f"and receives a commission for {self.kwargs['contracts']} contract(s) at {self.kwargs.get('commission_per_contract', 0)}/contract. "

      explanation += f"Their total pay is {self.get_pay()}."
      return explanation
# # Billie works on a monthly salary of 4000.  Their total pay is 4000.
# billie = Employee('Billie')

# # Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
# charlie = Employee('Charlie')

# # Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
# renee = Employee('Renee')

# # Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
# jan = Employee('Jan')

# # Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
# robbie = Employee('Robbie')

# # Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
# ariel = Employee('Ariel')

# Employee objects instantiation
billie = Employee('Billie', 'salary', monthly_salary=4000)
charlie = Employee('Charlie', 'hourly', hours_worked=100, hourly_wage=25)
renee = Employee('Renee', 'salary', monthly_salary=3000, contracts=4, commission_per_contract=200)
jan = Employee('Jan', 'hourly', hours_worked=150, hourly_wage=25, contracts=3, commission_per_contract=220)
robbie = Employee('Robbie', 'salary', monthly_salary=2000, bonus=1500)
ariel = Employee('Ariel', 'hourly', hours_worked=120, hourly_wage=30, bonus=600)


