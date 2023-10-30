# Реализуйте генераторную функцию  txt_to_dict() , которая не принимает никаких аргументов.
# Функция должна возвращать генератор, порождающий последовательность словарей, каждый
# из которых содержит информацию об очередной планете из файла  planets.txt , а именно ее
# название, диаметр, массу и орбитальный период. Например:
# {'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}

def txt_to_dict():
    
    with open('planets.txt', 'r') as file:
        mass_planet_dict = []
        for line in file:
            if len(line.split()) != 0:
                mass_planet_dict.append(line.rstrip('\n'))
                # print(mass_planet_dict)
                continue  
            else:      
                # print(mass_planet_dict)
                # print(*({stroka.split('=')[0].rstrip()  :  stroka.split('=')[1].lstrip().rstrip('\n')} for stroka in mass_planet_dict))
                yield {stroka.split('=')[0].rstrip()  :  stroka.split('=')[1].lstrip().rstrip('\n') for stroka in mass_planet_dict}
                # yield from ({stroka.split('=')[0].rstrip()  :  stroka.split('=')[1].lstrip().rstrip('\n')} for stroka in mass_planet_dict)
                mass_planet_dict = []
                
        
            
# TEST_1:
planets = txt_to_dict()

print(next(planets))
print()
# TEST_2:
planets = txt_to_dict()

print(*planets)        