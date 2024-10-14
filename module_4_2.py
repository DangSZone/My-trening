a=25

def test_function(x):
	a = x ** 2
	def inner_function():
		print('Я в области видимости функции test_function')
	inner_function()
	return a
		
print(test_function(5))
# Сначала нам выводится print, потомучто режде чем вернуть значение а, мы запустили функцию inner_function
inner_function()
# При выводе функции inner_function вне test_function, выдается ошибка, 
# потому что мы пытаемся вывести функцию из локальной зоны видимости функции.
# она создается только при вызове основной функции test_function. 
	
