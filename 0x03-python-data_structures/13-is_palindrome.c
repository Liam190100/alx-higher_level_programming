#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - shows list is a palindrome
 * @head: pointer list header
 *
 * Return: (1 if palindrome, 0 otherwise)
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL;
	listint_t *second_half, *first_half = *head;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	second_half = reverse_list(slow);
	is_palindrome = compare_lists(first_half, second_half);
	second_half = reverse_list(second_half);

	if (prev != NULL)
		prev->next = second_half;
	else
		*head = second_half;
	return (is_palindrome);
}
/**
 * reverse_list - reverses the list of palindrome
 * @head: list to the pointer head
 *
 * Return: (reversed list)
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *curr = head, *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	return prev;
}
/**
 * compare_lists - two lists
 * @list1: first list
 * @list2: second list
 *
 * Return: (1 lists , 0)
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);

		list1 = list1->next;
		list2 = list2->next;
	}

	return 1;
}
