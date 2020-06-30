#!/usr/bin/python3

class Test:

    def testing(self):
        string = "this is my test"
        return string
    def take_list(self,*args):
        for item in args:
            st = self.testing()
            return (item, st)
    
    def take_dict(self,**kwargs):
        return [kwargs]
    

if __name__=='__main__':
    t = Test()
    item = ['a', 'b','c']
    print(t.take_list(item))
    print(t.take_dict(a='5',b='7'))