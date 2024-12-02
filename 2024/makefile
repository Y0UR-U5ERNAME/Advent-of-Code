compile day$(DAY): day$(DAY).o
	@gcc -o day$(DAY) day$(DAY).o -Wall
day$(DAY).o: day$(DAY).c input$(DAY).txt
	@gcc -c day$(DAY).c -Wall
run: day$(DAY)
	@./day$(DAY).exe
clean:
	rm *.o
	rm *.exe