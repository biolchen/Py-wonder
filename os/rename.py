import os
os.chdir(os.path.dirname(__file__))

# Am I in the correct directory?
print(os.getcwd())

print(dir(os))

# Print all the current file names
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name)
    print(file_ext)
    print(file_name.split('_'))

    # One way to do this
    f_title, f_course, f_number = file_name.split('_')
    print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

    # Need to remove whitespace
    f_title = f_title.strip()
    f_course = f_course.strip()
    # f_number = f_number.strip()

    # Want to remove the number sign?
    # f_number = f_number.strip()[1:]

    # One thing I noticed about this output is that if it was sorted by filename
    # then the 1 and 10 would be next to each other. How do we fix this? One way we can fix this is to pad
    # the numbers. So instead of 1, we'll make it 01. If we had hundreds of files then this would maybe need to be 001.
    # We can do this in Python with zfill
    f_number = f_number.strip()[1:].zfill(2)

    # print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

    # You have the power to reformat in any way you see fit
    print('{}-{}{}'.format(f_number, f_title.strip(), file_ext.strip()))

    new_name = '{}-{}{}'.format(file_num, file_title, file_ext)
    os.rename(fn, new_name)


' 1'.strip()[1:].zfill(2)
str = "this is string example....wow!!!"
print(str.zfill(40))
print(str.zfill(50))
# print(len(os.listdir()))
