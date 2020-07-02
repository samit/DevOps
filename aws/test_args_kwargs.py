#!/usr/bin/python3
import json
class Test:

    def testing(self):
        string = "this is my test"
        return string
    def take_list(self,*args):
        for item in args:
            st = self.testing()
            return (item, st)
    
    def take_dict(self,**kwargs):
        print(kwargs['my_dict']['AlarmName'])
    

if __name__=='__main__':
    t = Test()
    item = ['a', 'b','c']
    print(t.take_list(item))
    my_dict = {"name":"Sanjaya", "surname":"Dahal", "age":36}
    with open('cloudwatch.json', 'r') as cwfile:
        records = json.load(cwfile)
    t.take_dict(my_dict=records)
    
