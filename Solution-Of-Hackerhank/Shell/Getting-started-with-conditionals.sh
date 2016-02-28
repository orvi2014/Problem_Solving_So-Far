# Getting started with conditionals

read sign

if [[ "$sign" == 'Y' || "$sign" == 'y' ]]; then
    echo 'YES'
else
    echo 'NO'
fi
