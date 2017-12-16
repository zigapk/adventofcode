#include<stdio.h>
#include<string.h>
#include <stdlib.h>

int main() {
  int jumps[2048];
  int jumps2[2048];
  int s1, s2 = 0;
  int size = 0;

  while (1) {
    char line[64];
    fgets(line, 64, stdin);
    if (line == '\0') break;

    jumps[size] = atoi(line);
    jumps2[size] = atoi(line);
    size++;
    printf("%d %d\n", size, jumps[size]);
  }
  size++;

  // printf("%d %d %d %d \n", jumps[0], jumps[1], jumps[2], jumps[3]);

  // part 1
  // int i = 0;
  // while(i >= 0 && i < size) {
  //   int a = jumps[i];
  //   jumps[i]++;
  //   s1++;
  //   i += a;
  // }


  printf("%d\n", s1);
  printf("%d\n", s2);
}
