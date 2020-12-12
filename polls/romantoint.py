class Solution:
    def romantoint(o: int):
        rome_numerals={'M':1000,'MI':999,'MX':900,'D':500,'DI':499,'DX':490,'C':100,'CI':99,'CX':90,'L':50,'LI':49,'LX':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
        rome_letters=['M','D','C','L','X','V','I']
        s = int(o)
        for lit in rome_letters:
            while s>=rome_numerals[lit]:
                print(lit)
                s-=rome_numerals[lit]
                
                

                
                
if __name__ == "__main__":
    s = input("")
    Solution.romantoint(s)