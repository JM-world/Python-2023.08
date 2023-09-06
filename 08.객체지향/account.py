class Account():
    def __init__(self, ano, owner, balance):
        self.ano = ano
        self.owner = owner
        try:
            self.balance = self.__error1(balance)
        except Exception:
            self.balance = '*'
            print('잔액은 0원 이상이고 10,000,000원 이하이어야 합니다.')

    def __error1(self, balance):
        if 0 <= balance <= 10000000:
            return balance
        else:
            raise Fare_error
    
    def deposit(self, amount):
            if self.balance == '*':
                return '잔액확인요망'
            else:
                if self.balance + amount <= 10000000:
                    self.balance += amount
                    return self.balance
                else:
                    return '잔액은 10,000,000원을 초과할 수 없습니다.'
            
    def withdrow(self, amount):
        if self.balance == '*':
            return '잔액확인요망'
        else:
            if self.balance - amount >= 0:
                self.balance -= amount
                return self.balance
            else:
                return '출금액이 현재 잔액보다 더 많습니다.'
        
    def __str__(self):
        if self.balance == '*':
            return '잔액은 0원 이상이고 10,000,000원 이하이어야 합니다.'
        else:
            return f'계좌번호: {self.ano}, 소유주: {self.owner}, 잔액 {self.balance:10,d}'

