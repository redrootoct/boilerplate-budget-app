class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance = amount
    
    def withdraw(self, amount, description=""):
        self.ledger.append({"amount": -(amount), "description": description})
        test = self.balance-(amount)
        
        if self.check_funds(amount)==True:
            self.balance += -(amount)
            return True
        else:
            return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self,amount, instance_name):
        self.withdraw(amount, f"Transfer to {instance_name.name}")
        if self.check_funds(amount)==True:
            instance_name.deposit(amount,f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self,amount):
        if self.balance >= amount:
            return True
        else:
            return False
        
    def __str__(self):
        selfname=self.name
        mainmane=selfname.center(30,"*")+"\n"
        for i in self.ledger:
           mainmane+= "{:<23}".format(i["description"][0:23])
           mainmane+= "{:>7.2f}".format(i["amount"])
           mainmane+="\n"
        mainmane+=f"Total: {self.balance}"
        return mainmane

def create_spend_chart(categories):
    
    summ_cat=[]
    for i in categories:
        summ=0
        for t in i.ledger:
            if t["amount"]<0:
                summ+=t["amount"]
        summ_cat.append(summ)
    
    percent=[]
    total=sum(summ_cat)
    x=0
    for y in summ_cat:
        x=(((y/total)*100)//10)*10
        percent.append(x)

    head = "Percentage spent by category\n"
    center=""
    for ii in range(100,-1,-10):
        line=(f"{str(ii).rjust(3)}|")
        for iii in percent:
            if iii>=ii:
                line+=(" o ")
            else:
                line+=("   ")
        line+=' \n'
        center+=(line)

    print(center)
    strike = "    "+ "-"*((len(percent)*3)+1) + "\n"
    foot=""
    names= []
    names2= []
    for i4 in categories:
        names.append(i4.name)
    xx=len(max(names,key=len))

    for i4 in categories:
        names2.append((i4.name).ljust(13))
    for x in zip(*names2):
        line3=""
        for y in x:
            line3+=y.center(3)
        foot+= "    " + line3 + " \n"
    all=head+center+strike+foot
    print(all)
    return all.rstrip("\n")
