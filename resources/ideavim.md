"" Source your .vimrc
"source ~/.vimrc

" Find more examples here: https://jb.gg/share-ideavimrc

set clipboard+=unnamed
set clipboard+=ideaput

nnoremap \e :e C:\\Users\\justi\\.ideavimrc<CR>
nnoremap \r :action IdeaVim.ReloadVimRc.reload<CR>
nnoremap <c-t> :action ActivateTerminalToolWindow<CR>
" nnoremap <leader>t :action Terminal.OpenInTerminal<CR>
nnoremap <c-\> :action SplitVertically<CR>
nnoremap <c--> :action SplitHorizontally<CR>
nnoremap <c-=> :action Unsplit<CR>

" Vimium Mappings
nnoremap <s-k> :action NextTab<CR>
nnoremap <s-j> :action PreviousTab<CR>
nnoremap <s-m> :action MoveEditorToOppositeTabGroup<CR>

" Registers "
Plug 'vim-scripts/ReplaceWithRegister'

let mapleader=","

nnoremap <Leader>q :wq<CR>
nnoremap <Leader>s :w<CR>

nnoremap [[ :action MethodUp<CR>
nnoremap ]] :action MethodDown<CR>

nnoremap zo :action ExpandRegion<CR>
nnoremap zc :action CollapseRegion<CR>
nnoremap zoo :action ExpandAllRegions<CR>
nnoremap zcc :action CollapseAllRegions<CR>
nnoremap <Leader>= :action ReformatCode<CR>
nnoremap <Leader>r :action Refactorings.QuickListPopupAction<CR>

" Copy paragraph below cursor and repaste it"
noremap cp yap<S-}>p

noremap <c-l> <c-w>w
noremap <c-h> <c-w>h
noremap <c-j> <c-w>j
noremap <c-k> <c-w>k

set scrolloff=5
set incsearch
set number relativenumber

map Q gq


Plug 'preservim/nerdtree'
map <s-p>   :NERDTreeToggle<CR>
