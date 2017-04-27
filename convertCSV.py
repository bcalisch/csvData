import csvkit
csvsql --db postgresql://$bcalisch:$uerbc0707@localhost:5432/$baseball--insert \
        --encoding $encoding --delimiter \, --quotechar \$quotechar --blanks \
        --no-constraints --no-inference /folder/*.csv
