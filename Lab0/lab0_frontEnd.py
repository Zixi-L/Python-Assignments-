import lab0_backEnd
from lab0_backEnd import Import_data

def main():
    
    co2_temp_data = Import_data('Co2.html','Temperature.html' ,"[+-]?\d+(?:\.\d+)?")    
    
    yes = True
    
    while yes:
        get_year_or_compare = input('Please input a year between 1959 and 2018, or < , or >: ')
    
        continuing = True
        
        while continuing: 
            if get_year_or_compare == '>':
                print('CO2 levels bigger than average are: ', co2_temp_data.get_bigger_than_Average_list())
                continue_answer = input('Do you want to continue? Please input Yes or No: ')
                if continue_answer == 'No':
                    continuing = False
                else:
                    get_year_or_compare = input('Please input a year between 1959 and 2018, or < , or >: ')
                
            elif get_year_or_compare == '<':
                print('CO2 levels smaller than average are: ', co2_temp_data.get_smaller_than_average_list())
                continue_answer = input('Do you want to continue? Please input Yes or No: ')
                if continue_answer == 'No':
                    continuing = False
                else:
                    get_year_or_compare = input('Please input a year between 1959 and 2018, or < , or >: ')
                
                
            # isdigit() means all the characters in the string are digits
            elif get_year_or_compare.isdigit() and int(get_year_or_compare) in range(1959,2019):
                
                print('The Co2 level of', int(get_year_or_compare),
                      'is', co2_temp_data.get_co2_from_dic(int(get_year_or_compare)),
                      '\nThe temperature differnce between', get_year_or_compare,
                      'and average is', co2_temp_data.get_temp_from_dic(int(get_year_or_compare)))
                
                continue_answer = input('Do you want to continue? Please input Yes or No: ')
                if continue_answer == 'No':
                    continuing = False
                else:
                    get_year_or_compare = input('Please input a year between 1959 and 2018, or < , or >: ')
                
            else:
                print('Error')
                get_year_or_compare = input('Please input a year between 1959 and 2018, or < , or >: ')
                    
        yes = False
        print('See you next time!')
            
main()