#include <stdlib.h>

void    ft_free_stuff(char *new, int *value)
{
    if (new != NULL)
        free(new);
    if (value != NULL)
        free(value);
    exit(1);
}

int main(void)
{
    int len = 69;
    char *new = malloc(sizeof(char) * len);
    int *value = malloc(sizeof(int) * len);
    if (!new || !value)
        ft_free_stuff(new, value);
    return 0;
}