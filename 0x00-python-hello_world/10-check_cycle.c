#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *sec;
	listint_t *pre;

	sec = list;
	pre = list;
	while (list && sec && sec->next)
	{
		list = list->next;
		sec = sec->next->next;

		if (list == sec)
		{
			list = pre;
			pre =  sec;
			while (1)
			{
				sec = pre;
				while (sec->next != list && sec->next != pre)
				{
					sec = sec->next;
				}
				if (sec->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
