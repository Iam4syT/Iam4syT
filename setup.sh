#!/bin/bash
echo "Setup and Configure Server"

file_name = config.yaml

config_dir = $1

if [-d "$config_dir"]
then
    echo "reading config directory contents"
    config_file = $(ls"$config_dir")
    echo "here are all the configurations file : $config_file "
else
    echo "config dir not found.
          creating one...."
    mkdir "$config_dir"
    touch "$config_dir/config.sh"
fi



user_group = xx
 
if ["$user_group" == "nana"]
then   
    echo "configure the server"
elif ["$user_group" == "admin"]
then
    echo "administer the server"
else    
    echo "No permission to configure server. wrong user group"
fi

read -p "please enter your user group : $administrator"


echo "using file $file_name to configure something"

sum = 0
while true
    do
        read -p "enter a score" : score
        if [ "$score" == "q"]
        then
            break
        fi
        sum = $(($sum + $score))
        echo " total score: $sum"
    done 

echo "all params : $*"
echo "number of params : $#" 
  
for param in $*
    do
        if 
            [-d "$param"]
            then
            echo "executing scripts in the config folder"
            ls -l "$param"
        fi
    echo $param
    done

