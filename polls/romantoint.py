class Solution:
    def romantoint(o: int):
        rome_numerals={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        rome_letters=['M','D','C','L','X','V','I']
        s = int(o)
        for lit in rome_letters:
            while s>=rome_numerals[lit]:
                print(lit)
                s-=rome_numerals[lit]
                
                

                
                
if __name__ == "__main__":
    s = input("")
    Solution.romantoint(s)