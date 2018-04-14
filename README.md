```console
$ python auth.py > auth_kotet.txt
$ cat auth_kotet.txt list_info.txt | python getlist.py > apu_list.txt
$ cat auth_kotet.txt kotetttt.txt | python getfollowing.py > kotet_following.txt
$ python auth.py > auth_kotetsec.txt
$ cat auth_kotetsec.txt kotetsec.txt | python getfollowing.py > kotetsec_following.txt
$ sort kotetsec_following.txt kotet_following.txt | uniq -d > dup.txt
$ cat auth_kotet.txt dup.txt | python destroy.py
$ cat auth_kotet.txt target.txt | python getfollowing.py > kotet_following.txt
$ sort kotet_following.txt apu_list.txt | uniq -d > follow.txt
$ cat auth_kotetsec.txt mustfollow.txt | python follow.py
```