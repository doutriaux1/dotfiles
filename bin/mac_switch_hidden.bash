STATUS=`defaults read com.apple.finder AppleShowAllFiles`
if [ $STATUS == 1 ]; 
then
  defaults write com.apple.finder AppleShowAllFiles 0
else
  defaults write com.apple.finder AppleShowAllFiles 1
fi
