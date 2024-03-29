import requests

class Employee:
    """ a sample Employee class"""
    
    raise_amt = 1.05
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last) 
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) 
    
    # we make a mock test as we dont want our test to depend on the website being up. 
    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'