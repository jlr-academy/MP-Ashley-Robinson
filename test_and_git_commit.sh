#!/bin/bash 
set -eu

#Write a script that will run your test suite and (if the tests pass) do a git commit.
#Don't forget to make it accept a commit message.


#invoke pytest on src directory
# test if pytest ./src works. exit code 0


if pytest ./src;
then
echo "All tests passed. Changes will nowbe commited to GIT."
echo "Please enter your commit message "
read comment
git add .
git commit -m "$comment"
git push
else
echo "Tests not passed. Changes will not be commited to GIT"
fi

