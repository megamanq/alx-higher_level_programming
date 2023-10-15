#include "lists.h"

/**
 * is_palindrome - check if a listy is
 * palindrome
 * @head: ptr to head of list
 * Return: 0 if not , 1 f is
 */

int is_palindrome(listint_t **head)
{
	listint_t *curr;
	int i = 0, len = 0;
	int arr[5000];

	if (*head == NULL)
	{
		return (1);
	}

	curr = *head;
	while (curr)
	{
		arr[len] = curr->n;
		curr = curr->next;
		len++;
	}

	if (len == 1)
	{
		return (1);
	}

	len--;
	while (i < len)
	{
		if (arr[i] != arr[len])
		{
			return (0);
		}
		i++;
		len--;
	}
	return (1);
}
