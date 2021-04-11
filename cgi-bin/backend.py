#!python
import cgi
import cgitb
cgitb.enable()


def main():
    form = cgi.FieldStorage()

    base64_image_data = form['image'].value

    # TODO: Decode the data and write to file
    # run the function to read the barocde from the image
    barcode = "15357643"

    print("Content-type: text/plain\n\n"+barcode)

if __name__ == "__main__":
    main()