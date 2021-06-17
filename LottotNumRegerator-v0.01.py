import random
''' This program will generate lotto numbers ''' 

def lottoNumbers(numberOfNumbers):
    
    list = []
        
    while (len(list) < numberOfNumbers):
        numbers = random.randint(1,50)
        if numbers not in list:
            list.append(numbers)
                
                
    return list

print(lottoNumbers(7))
 