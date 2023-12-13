

ls manga | awk '{ printf("mv manga/%s/cleaned clean/%s_clean\n", $1, $1); }' > script_move.sh 

