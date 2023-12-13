file */* | grep PNG | awk '{ a = substr($1, 1, length($1) - 5); printf("mv %s.jpg %s.png\n", a, a); }' > png.sh
