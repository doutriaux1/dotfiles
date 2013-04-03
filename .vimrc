set mouse=a
set nu
execute pathogen#infect()
syntax on
filetype plugin indent on
let g:miniBufExplMapWindowNavVim = 1
let g:miniBufExplMapWindowNavArrows = 1
let g:miniBufExplMapCTabSwitchBufs = 1
let g:miniBufExplModSelTarget = 1
map T :TaskList<CR>
map P :TlistToggle<CR>
set expandtab
set textwidth=79
set tabstop=8
set softtabstop=4
set shiftwidth=4
set autoindent
