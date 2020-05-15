from django.shortcuts import render
import csv
import codecs
import sys
from io import StringIO

# Create your views here.


def my_template(request):
    return render(request, 'my_template.html')


def csv_display(request):
    if request.method == 'POST':
        file = request.FILES['file']
        table = csv.reader(codecs.iterdecode(file, 'utf-8'))

        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        def creator():

            print("<table border='1' style='width: 100%;'>")
            for i, row in enumerate(table):
                print("<tr>")

                if i == 0:
                    print("<th>#</th>")
                else:
                    print("<th>" + str(i) + "</th>")

                for column in row:
                    if i == 0:
                        print("<th>" + column + "</th>")
                    else:
                        print("<td style='text-align:center'>" + column + "</td>")

                print("</tr>")

            print("</table>")
            sys.stdout = old_stdout
            result_string = result.getvalue()
            return result_string

    creator_var = (creator())
    return render(request, 'csv_display.html', {'creator_var': creator_var})
