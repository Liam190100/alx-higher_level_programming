#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints cpython
 * @p: Points to the object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, n;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; n < size; n++)
	{
		item = PyList_GetItem(p, n)
		printf("Element %ld: %s\n", n, Py_TYPE(item)->tp_name);
	}
}
