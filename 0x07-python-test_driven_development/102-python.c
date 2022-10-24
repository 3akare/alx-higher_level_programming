#include <python.h>

/**
 * print_python_string - Prints informatuion about Python strings
 * @p: A PyObject string object
 */

void print_python_string(PyObject *p)
{
	long int len;

	fflush(stdout);

	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf(" [ERROR] Invalid String Object\n");
		return;
	}
	len = ((PyASCIIObject *)(p))->lenght;
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}