#!/usr/bin/env sh
#
# pdfsplit [input.pdf] [first_page] [last_page] [output.pdf] 
#
# Example: pdfsplit big_file.pdf 10 20 pages_ten_to_twenty.pdf
#
# written by: Westley Weimer, Wed Mar 19 17:58:09 EDT 2008
#
# The trick: ghostscript (gs) will do PDF splitting for you, it's just not
# obvious and the required defines are not listed in the manual page. 

if [ $# -lt 4 ] 
then
        echo "Usage: pdfsplit input.pdf first_page last_page output.pdf"
        exit 1
fi
yes | gs -dBATCH -sOutputFile="$4" -dFirstPage=$2 -dLastPage=$3 -sDEVICE=pdfwrite "$1" >& /dev/null

input_pdf="$1"

total_page=$(strings < $input_pdf | sed -n 's|.*/Count -\{0,1\}\([0-9]\{1,\}\).*|\1|p' | sort -rn | head -n 1)


input=$(zenity --forms --title="PDF Split" \
    --text="PDF Split: \
    This pdf file contains $total_page pages.\n\
    Add a prefix or suffix to the filename.\n\
    Input pages to split" \
    --add-entry="Filename Prefix" \
    --add-entry="Filename Suffix" \
    --add-entry="From Page" \
    --add-entry="To Page")

from_page= 
to_page=

prefix=
suffix=



output_pdf=








gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dFirstPage=1 -dLastPage=5 -sOutputFile=%d.pdf 
