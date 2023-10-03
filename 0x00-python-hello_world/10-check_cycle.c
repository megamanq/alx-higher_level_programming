#include "lists.h"

/**
 * check_cycle - checks if a singly linked list
 * has a cycle in it
 * list: a listint_t list to checl
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *rapid_ptr, *slow_ptr;

	rapid_ptr = list;
	slow_ptr = list;

	while(rapid_ptr && slow_ptr)
	{
		rapid_ptr = rapid_ptr->next->next;
		slow_ptr = slow_ptr->next;

		if (rapid_ptr == slow_ptr)
		{
			return (1);
		}
	}

	return (0);
}
