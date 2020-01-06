for _ in range(int(input())):
    n = int(input())
    stt = input()
    tts = stt[::-1]
    st = []
    for __ in stt:
        if __ != ' ':
            st.append(__)
    a1 = st.count('1')
    a2 = st.count("2")
    a3 = st.count("3")
    a4 = st.count('4')
    a5 = st.count('5')
    a6 = st.count('6')
    a7 = st.count('7')
    if a1 == 0 or a2 == 0 or a3 == 0 or a4 == 0 or a5 == 0 or a6 == 0 or a7 == 0:
        print("0")
    if a1+a2+a3+a4+a5+a6+a7 != len(st):
        print("len")
    if stt == tts and st[0:a1] == 1 and st[a1:a1+a2] == 2 and st[a1+a2:a1+a2+a3] == 3 and st[a1+a2+a3:a1+a2+a3+a4] == 4 and st[a1+a2+a3+a4:a1+a2+a3+a4+a5] == 5 and st[a1+a2+a3+a4+a5:a1+a2+a3+a4+a5+a6] == 6 and st[a1+a2+a3+a4+a5+a6:a1+a2+a3+a4+a5+a6+a7] == 7:
        print("yes")

