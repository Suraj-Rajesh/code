#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/* NOTES */
/*
 *  getopt: Parses command line options, when nothing to parse returns -1
 *
 *  Here, ./a.out -k keyid -f srcfilename dstfilename
 *
 *  Now, in flags, k: means, it is mandatory that -k have some option, or
 *  terminate. Next, -f is just a flag with no arguments. Both, -k and -f 
 *  may not be present. For eg: we can run, ./a.out srcfilename dstfilename.
 *
 * optarg: Points to the option argument.
 * optind: Always points to the next non-parsed argument index.
 *
 * So, argc -= optind;
 *     argv += optind; 
 * Will bring the focus back to the non option arguments(srcfilename and dstfilename)
 * Since, these two are non option arguments, getopt won't touch them and once
 * all option args are parsed, they will be left. So, optind as can be
 * recollected, points to the next non-parsed argument index, hence to
 * srcfilename(it automatically re-adjusts as per the position of these, as
 * long as both srcfilename and dstfilename are next to each other). Some
 * magic happens at argc -= optind; and argv += optind; :D
 * */

int main(int argc, char * argv[]){
    char  * flag = "fk:", * keyid = NULL, * srcfile = NULL, * dstfile = NULL;
    int     force = 0;
    char    ch;
    
    while ((ch = getopt(argc, argv, flag)) != -1){
        switch(ch){
            case 'k':
                keyid = optarg;
                break;
            case 'f':
                force = 1;
                break;
            default:
                printf("Go to hell...\n");
                exit(0);
        }
    }

    argc -= optind;
    argv += optind;

    // If -k keyid is mandatory, use this otherwise, uncomment it
    if(NULL == keyid) exit(0);

    if(argc < 1 || argc > 2) { printf("Wrong arguments bro !!\n"); exit(0); }

    srcfile = argv[0];
    (argv[1] != NULL) ? (dstfile = argv[1]): (dstfile = "default");

    printf("Key: %s\nSrc file: %s\nDst file: %s\n", keyid, srcfile, dstfile);
}
