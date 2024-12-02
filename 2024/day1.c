#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void * a, const void * b) {
    return *((int *)a) - *((int *)b);
}

int main() {
    FILE * f = fopen("input1.txt", "r");
    char buff[20];
    int l1[1000];
    int l2[1000];
    int i = 0;
    while (fgets(buff, 128, f)) {
        int a, b;
        sscanf(buff, "%d %d", &a, &b);
        l1[i] = a; l2[i] = b;
        i++;
    }
    fclose(f);

    qsort(l1, i, sizeof(int), compare);
    qsort(l2, i, sizeof(int), compare);
    int sum = 0;
    int sum2 = 0;
    for (int j = 0; j < i; j++) {
        int d = l1[j] - l2[j];
        sum += d < 0 ? -d : d;

        for (int k = 0; k < i; k++) {
            if (l1[j] == l2[k]) sum2 += l1[j];
        }
    }
    printf("%d\n", sum);
    printf("%d\n", sum2);
    return 0;
}