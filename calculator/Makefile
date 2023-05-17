objects = main.o addition.o division.o multiplication.o subtraction.o

calculator: $(objects)
	gcc -o calculator $(objects)

$(objects): %.o: %.c
	gcc -c $< -o $@

clean: 
	rm -f calculator $(objects)

.PHONY: clean
