#cook your code here
for _ in range(int(input())):
    tag = input().strip()  

    if tag.startswith('</') and tag.endswith('>') and tag[2:-1].isalnum():
        if tag[2:-1].isdigit() or tag[2:-1].islower():
            print('success')
        else:
            print('error')
    else:
        print('error')
