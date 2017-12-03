#include<stdio.h>
#include<string.h>
#include <stdlib.h>

int main() {
  char line[4096];
  fgets(line, 4096, stdin);

  int s1, s2 = 0;
  for(int i = 0; i < strlen(line); i++) {
    if (line[i] == line[(i+1) % (strlen(line) - 1)]) s1 += line[i] - '0';
    if (line[i] == line[(i+1+strlen(line)/2) % (strlen(line) - 1)]) s2 += line[i] - '0';
  }
  printf("%d\n", s1);
  printf("%d\n", s2);
}
