import letters as lt
name = "Fidel Ysla"
first = name.split()[0][0]
second = name.split()[1][0]

abc = [lt.A,
       lt.B,
       lt.C,
       lt.D,
       lt.E,
       lt.F,
       lt.G,
       lt.H,
       lt.I,
       lt.J,
       lt.K,
       lt.L,
       lt.M,
       lt.N,
       lt.O,
       lt.P,
       lt.Q,
       lt.R,
       lt.S,
       lt.T,
       lt.U,
       lt.V,
       lt.W,
       lt.X,
       lt.Y,
       lt.Z]

for i in abc:
    if first == i[1]:
        for n in abc:
            if second == n[1]:
                print(f"""
                      {i[0]}{n[0]}
                      """)
