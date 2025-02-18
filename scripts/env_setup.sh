
PS1='%n@%m %~$ '
alias zshrc="vim $HOME/.zshrc"
alias sourcez="source $HOME/.zshrc"

export PROJECTS="$HOME/SoftwareProjects"
export BLIZZARD="$PROJECTS/Blizzard"
export SNOWMAN="$BLIZZARD/snowman2"
export SCRIPTS="$BLIZZARD/scripts"
export SMOKETESTS="$SNOWMAN/smoketests"
alias spring="$HOME/spring/SpringToolSuite4"
alias pycharm="$HOME/pycharm/bin/pycharm > /dev/null 2>&1 &"
alias scripts="cd $SCRIPTS"
alias blizzard="cd $BLIZZARD"
alias snowman="cd $SNOWMAN"
alias smoke="cd $SMOKETESTS"
alias setup="scripts; vim env_setup.sh;sourcez"
alias localsmoke="$SMOKETESTS/run_local_smoketests.sh"
#/devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1:1.0/0003:1B1C:1B7C.0006/input/input34/event4
