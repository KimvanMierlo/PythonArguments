# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

planet_gravity = {
	'sun' : 274,
	'jupiter' : 24.9,
	'neptune' : 11.2,
	'saturn' : 10.4,
	'earth' : 9.8,
	'uranus' : 8.9,
	'venus' : 8.9,
	'mars' : 3.7,
	'mercury' : 3.7,
	'moon' : 1.6,
	'pluto' : 0.6
}

def greet(name, template='Hello, <name>!'):
	return template.replace("<name>", name)


print(greet("Mark"))
print(greet('Mark', 'Hello my name is <name>.'))


def force(mass, body='earth'):
	return mass * planet_gravity[body]

print(force(3, 'sun'))

def pull(m1, m2, d):
	G = 6.674*(10**-11)
	force = G*((m1*m2)/(d*d))
	return force

mass_earth = 5.972*(10**24)
print(pull(0.1, mass_earth, 6.371*(10**6)))