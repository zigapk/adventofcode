#include<stdio.h>
#include<string.h>
#include <stdlib.h>

int main() {
  int s1, s2 = 0;

  while (1) {
    char line[4096];
    fgets(line, 4096, stdin);
    if (strlen(line) <= 3) break;

    // split string
    int iline[100];
    char * pch;
    int size = 0;
    pch = strtok(line, " ");
    while (pch != NULL) {
      iline[size] = atoi(pch);
      size++;
      pch = strtok(NULL, " ");
    }

    // part 1 - find min and max
    int max = 0; int min = 23945234;
    for (int i = 0; i < size; i++) {
      if (iline[i] > max) max = iline[i];
      if (iline[i] < min) min = iline[i];
    }
    s1 += max-min;

    // part 2 - find evenly devisible numbers
    for (int x = 0; x < size - 1; x++) {
      for (int y = x + 1; y < size; y++) {
        if (iline[x] % iline[y] == 0) s2 += iline[x] / iline[y];
        if (iline[y] % iline[x] == 0) s2 += iline[y] / iline[x];
      }
    }
  }
  printf("%d\n", s1);
  printf("%d\n", s2);
}
