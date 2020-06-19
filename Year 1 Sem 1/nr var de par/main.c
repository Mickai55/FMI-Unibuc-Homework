#include <stdio.h>
#include <stdarg.h>

int minim(int num, ...)
{
    int Min, a, i;
    va_list ap;
    va_start(ap, num);
    Min = va_arg(ap, int);

    for (i = 2; i <= num; i++)
    {
        a = va_arg(ap, int);
        if (a < Min)
            Min = a;
    }
    va_end(ap);
    return Min;
}

int main()
{
    functie (4, 3, 33, 1);
   return 0;
}
