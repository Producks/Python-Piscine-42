#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

int main(void)
{
    int fd = open(".cub", O_RDONLY);
    if (fd == -1)
        return 1;
    char buffer[50];
    int ret = read(fd, buffer, 50);
    if (ret == -1){
        puts("RETARD");
        return 1;
    }
    return 0;
}