#include "lists.h"
/**
 * insert_node - inserts singly linked list
 * @head: head of the linked list
 * @number: insert number
 * Return:  node, or NULL 
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *len;


	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);


	new_node->n = number;


	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}


	len = *head;
	while (len->next != NULL && len->next->n < number)
		len = len->next;

	new_node->next = len->next;
	len->next = new_node;

	return (new_node);
}
