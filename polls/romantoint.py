class Solution:
    def int_to_roman(o: int):
        rome_numerals={'M':1000,'IM':999,'XM':990, 'CM':900,'D':500,'ID':499,'XD':490,'C':100,'IC':99,'XC':90,'L':50,'IL':49,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
        rome_numbers=[rome_letter for rome_letter in rome_numerals]
        s = int(o)
        str_list=[]
        for lit in rome_numbers:
            while s>=rome_numerals[lit]:
                str_list.append(lit)
                s-=rome_numerals[lit]
                
        return ''.join(str_list)
                

                
                
if __name__ == "__main__":
    s = input("")
    print(Solution.int_to_roman(s))