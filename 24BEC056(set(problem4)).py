def set4():
    s={'ananya','ami','swaroopa','anupama','brinda','brijesh'}
    sa=set()
    sb==set()
    for nm in s:
        if nm[0]=='a':
            sa.add(nm)
        elif nm[0]=='b':
            sb.add(nm)
        sa = {nm for nm in s if nm[0] == 'a'}
        print(sa)
        print(sb)
set4()