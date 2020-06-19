#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char w[100], s[100], p[100], u[100];
    gets (w);
    strcpy(u, w);
    gets (s);
    int i = 0, j = 0, sw;
    while (i != strlen(s) + 1)
        if (strchr ("., ;!?", s[i]))
        {
            j = 0; sw = 1;
            while (j != strlen(p))
            {
                if (strchr(w, p[j]) == 0)
                    sw = 0;
                else
                    w[strchr(w, p[j]) - w] += 100;
                j++;
            }
            if (sw == 1)
                printf("%s ", p);
            strcpy(w, u);
            strcpy(p, p + j);
            j = 0;
            i++;
        }
        else
        {
            p[j] = s[i];
            p[j + 1] = '\0';
            j++;
            i++;
        }
    return 0;
}
/*
caca
da caca dsada gg acac caac acca cssasd
*/

