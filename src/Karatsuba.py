'''
Created on 2 Jul 2015

@author: biedakl
'''
class KaratsubaAlg:
    def compute(self, num1, num2):
        if(len(str(num1)) != len(str(num2))):
            print("Numbers should have the same number of digits")
            return
        
        self.n = len(str(num1))/2
        self.n2 = len(str(num1)) - len(str(num1))/2
        print("n: "+ str(self.n))
        
        (a,b,c,d) = self.seperate(num1, num2)
        return self.doKaratsuba(a,b,c,d)
    
    def doKaratsuba(self, a, b, c, d):
        print("ac*10^n + (ad + bc)*10^n/2 + bd")
        print("ac: "+str(a*c))
        print("ad: "+str(a*d))
        print("bc: "+str(b*c))
        print("bd: "+str(b*d))
        result = a*c*10**(2*self.n2) + (a*d + b*c)*10**(self.n2) + b*d
        print("Result: " + str(result))
        return result
    
    def seperate(self, num1, num2):    
        (a,b) = self.divide(num1)
        (c,d) = self.divide(num2)
        
        print("a: "+str(a))
        print("b: "+str(b))
        print("c: "+str(c))
        print("d: "+str(d))
        return (a,b,c,d)
    
    def divide(self, number):
        digits = list(str(number))
        a = ""
        b = ""
        
        i = 0
        for digit in digits:
            if(i<self.n):
                a+=digit
            else:
                b+=digit
            i+=1
        
        return(int(a), int(b))


x = 12345
y = 67890
ka = KaratsubaAlg()
ka.compute(x, y)
print(x*y)