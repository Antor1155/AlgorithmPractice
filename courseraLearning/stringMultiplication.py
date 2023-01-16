class Solution:

    def help_multiply(self, num1, num2):
        temp = 0
        k = 0.1
        
        for i in range(1, len(num1)+1):
                t = k
                n1= num1[-i]
                for j in range(1,len(num2)+1):

                    k = int(k*10)

                    n2= num2[-j]
                    temp = (int(num1[-i]) * int(num2[-j]) * k ) + temp


                k = t * 10
                
                k = int(k)

        return str(temp)
    
    def multiply(self, num1: str, num2: str) -> str:
       

        if len(num2)< len(num1):
           return(self.help_multiply(num2, num1))
        else:
           return(self.help_multiply(num1, num2))

        

s  = Solution()

n2 = "60974249908865105026646412538664653190280198809433017"
n1 = "500238825698990292381312765074025160144624723742"

x = s.multiply(n1, n2)

print(x, type(x), len(x))
print(int(n1) * int(n2) ,"real ans is")

assert int(x) == int(n1) * int(n2), "number didn't match"