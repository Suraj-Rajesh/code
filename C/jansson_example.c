#include <stdio.h>
#include <string.h>
#include <jansson.h>


int getkey(json_t **policy) {

  char* s = NULL;
  char* pol = NULL;
  char* res_str = NULL;

  json_t *root = json_object();
  json_t *json_arr = json_array();

  json_object_set_new( root, "destID", json_integer( 1 ) );
  json_object_set_new( root, "command", json_string("enable") );
  json_object_set_new( root, "respond", json_integer( 0 ));
  json_object_set_new( root, "data", json_arr );

  json_array_append( json_arr, json_integer(11) );
  json_array_append( json_arr, json_integer(12) );
  json_array_append( json_arr, json_integer(14) );
  json_array_append( json_arr, json_integer(9) );

  s = json_dumps(root, 0);

  json_t *res = json_object();
  json_object_set_new(res, "key", json_string("#@$DSFSDFsfs"));
  json_object_set(res, "policy", root);

  if (NULL != policy){
  //   json_t * p = json_object_get(res, "policy");
     *policy = json_object_get(res, "policy");

 //   *policy = p;
//    json_incref(p);
    if (*policy){
        json_incref(*policy);
    }
  }

  json_decref(root);
  json_decref(res);

 return 0;
}


int
main(){
    char *pol = NULL;

    json_t *policy = NULL;
    getkey(&policy);
//    getkey(NULL);

    if (NULL != policy){
        printf("In caller\n");
        pol = json_dumps(policy, 0);
        printf("%s\n", pol);

        json_decref(policy);
    }

}
