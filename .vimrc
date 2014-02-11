set nonu
set ff=unix
execute pathogen#infect()
syntax on
filetype plugin indent on
let g:miniBufExplMapWindowNavVim = 1
let g:miniBufExplMapWindowNavArrows = 1
let g:miniBufExplMapCTabSwitchBufs = 1
let g:miniBufExplModSelTarget = 1
map T :TaskList<CR>
map PP :TlistToggle<CR>
set expandtab
set textwidth=79
set tabstop=4
set softtabstop=2
set shiftwidth=2
"set autoindent
autocmd BufEnter * silent! lcd %:p:h
set clipboard=unnamed
set hidden
set viminfo='25,\"50,n~/.viminfo
set formatoptions-=tc
set backupskip=/tmp/*,/private/tmp/*
function! ResCur()
  if line("'\"") <= line("$")
    normal! g`"
    return 1
  endif
endfunction

augroup resCur
  autocmd!
  autocmd BufWinEnter * call ResCur()
augroup END

