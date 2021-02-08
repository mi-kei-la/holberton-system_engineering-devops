#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int infinite_while(void);

/**
  * main - Create 5 zombie processes, then sleep.
  *
  * Return: 0 (always success).
  */

int main(void)
{
	pid_t child;
	int i;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child > 0)
		{
			printf("Zombie process created, PID: %d\n", child);
			sleep(1);
		}
		else
		{
			exit(0);
		}
	}

	infinite_while();

	return (0);
}

/**
  * infinite_while - Leave a function on sleep.
  *
  * Return: 0 (always success).
  */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
