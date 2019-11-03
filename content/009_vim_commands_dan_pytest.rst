#######################
Vim Commands dan Pytest
#######################

:date: 2019-09-01 09:00
:author: Hazuli Fidastian
:tags: vim ; neovim ; pytest
:lang: id
:status: draft

.. code-block:: viml

   " Parse currenttag from tagbar, replace . with ::
   function! LCurrentMethod()
       let l:curtag = tagbar#currenttag('%s', '', 'f')
       return substitute(l:curtag, '\.', '::', '')
   endfunction
   
   " Parse currenttag from tagbar, replace .[all next chars] with ''
   function! LCurrentClass()
       let l:curtag = tagbar#currenttag('%s', '', 'f')
       return substitute(l:curtag, '\..*', '', '')
   endfunction
   
   nnoremap Ts :nnoremap Tt :-tabnew term://pytest %
   nnoremap Tt :-tabnew term://pytest %
   nnoremap T. :-tabnew term://pytest %:h
   nnoremap TT :-tabnew term://pytest
   nnoremap TC :!xdg-open htmlcov/index.html<Cr>
   nnoremap Tm :exe ':-tabnew term://pytest %::' . LCurrentMethod()
   nnoremap Tc :exe ':-tabnew term://pytest %::' . LCurrentClass()
