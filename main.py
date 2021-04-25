# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, template='Hello, <name>!'):
	template_list = template.split("<name>")
	template_list.insert(1, name)
	result = ''
	for part in template_list:
		result += part
	return result


print(greet("Mark"))
print(greet('Mark', 'Hello my name is <name>.'))


def force(mass, body='earth'):

	if body == 'sun':
		gravity = 274
	elif body == 'fupiter':
		gravity = 24.9
	elif body == 'neptune':
		gravity = 11.2
	elif body == 'saturn':
		gravity = 10.4
	elif body == 'earth':
		gravity = 9.8
	elif body == 'uranus':
		gravity = 8.9
	elif body == 'venus':
		gravity = 8.9
	elif body == 'mars':
		gravity = 3.7
	elif body == 'mercury': 
		gravity = 3.7
	elif body == 'moon':
		gravity = 1.6
	elif body == 'pluto':
		gravity = 0.6
	else:
		gravity = 0
		print ('Error: unknown body')

	return mass * gravity

print(force(3, 'sun'))

def pull(m1, m2, d):
	G = 6.674*(10**-11)
	force = G*((m1*m2)/(d*d))
	return force

mass_earth = 5.972*(10**24)
print(pull(0.1, mass_earth, 6.371*(10**6)))