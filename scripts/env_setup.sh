
PS1='%n@%m %~$ '
alias zshrc="vim $HOME/.zshrc"
alias sourcez="source $HOME/.zshrc"

export PROJECTS="$HOME/SoftwareProjects"
export BLIZZARD="$PROJECTS/Blizzard"
export SNOWMAN="$BLIZZARD/snowman"
export SCRIPTS="$BLIZZARD/scripts"
export SMOKETESTS="$SNOWMAN/smoketests"
alias spring="$HOME/spring-eclipse-ide/SpringToolSuite4 > /dev/null 2>&1 &"
alias pycharm="$HOME/pycharm/bin/pycharm > /dev/null 2>&1 &"
alias scripts="cd $SCRIPTS"
alias blizzard="cd $BLIZZARD"
alias snowman="cd $SNOWMAN"
alias smoke="cd $SMOKETESTS"
alias setup="scripts; vim env_setup.sh;sourcez"
alias localsmoke="$SMOKETESTS/run_local_smoketests.sh"
