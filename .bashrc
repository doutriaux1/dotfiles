# Moving around
alias ..="cd .."
alias ...="cd ../.."

# SPACK
export SPACK_ROOT=/usr/workspace/cdoutrix/spack
alias activate_spack=". ${SPACK_ROOT}/share/spack/setup-env.sh"

# CONDA
alias activate_conda="source /g/g19/cdoutrix/miniconda3/bin/activate"
alias activate_amlcs="conda activate /usr/workspace/aml_cs/kosh/toss_3_x86_64_ib/dev"

## Git 
alias gci="git commit"
alias gco="git checkout"
alias gcl='${HOME}/bin/git-clean-local.py -s -V'
alias gst='git status'
alias gbr='for branch in `git branch -r | grep -v HEAD`;do echo -e `git show --format="%ci %cr" $branch | head -n 1` \\t$branch; done | sort -r'
alias gb='for branch in `git branch -r | grep -v HEAD`;do echo -e `git show --format="%ci %cr" $branch | head -n 1` \\t$branch; done | sort'

# Python
alias pb="python setup.py install"
alias p="ipython"
PYTHONSTARTUP=${HOME}/.pythonrc
JUPYTERLAB_DIR=${HOME}/.jupyter

# Editors
export EDITOR='vi'

# History
export HISTCONTROL=erasedups
export HISTSIZE=1000000
export HISTFILESIZE=1000000
export TMOUT=0

# Unix
alias ls="ls -h"
alias ll="ls -l"
alias md="mkdir"
alias pd="pushd"

# SSH AGENT
function agent {
   eval `ssh-agent` ;
   ssh-add
   }
