#include "lists.h"
/**
 * check_cycle - check cycle in the linked list
 * @list: check the linked list
 * Return  (if 0 no cycle, if 1 there is a cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
