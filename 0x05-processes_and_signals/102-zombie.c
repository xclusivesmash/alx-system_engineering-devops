#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * infinite_while - runs an infinite while loop.
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - creates 5 zombie processes.
 * Return: 0.
 */
int main(void)
{
	pid_t myPID;
	unsigned int i;

	i = 0;
	while (i < 5)
	{ /* FORK CHILD PROCESSES */
		myPID = fork();
		if (myPID == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", myPID);
		i = i + 1;
	}
	return (infinite_while());
}
