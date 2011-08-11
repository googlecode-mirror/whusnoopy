#!/bin/bash

cur_dir=`pwd`
s_dir=`dirname $0`
if [ "${s_dir}" == "." ]; then
  markdown_dir="$cur_dir"
elif [ "${s_dir:0:2}" == "./" ]; then
  markdown_dir="$cur_dir/${s_dir:2:1024}"
fi

root_dir=`dirname $markdown_dir`

function YWLOG()
{
  now_time=`date +%D_%H:%M:%S`
  log_message=$*

  echo -e "$now_time $log_message"
}

function genhtml() {
    YWLOG "Start to generate html from all text files"

    filelist=`ls $markdown_dir/*.text`

    for file in $filelist
    do
      basename=`basename $file`
      htmlpath="$root_dir/${basename%%.*}.html"
      `markdown_py $file | $markdown_dir/htmlregen.py > $htmlpath`
    done
}

YWLOG "start to generate all html files"
genhtml
YWLOG "all html files generated"

exit

