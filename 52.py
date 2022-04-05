x="春眠不覺曉處處聞啼鳥夜來風雨聲花落知多少"
setx=set()
y="紅豆生南國春來發幾枝願君多采擷此物最相思"
sety=set()
for i in x:
    setx.add(i)
for i in y:
    sety.add(i)

print(setx&sety)  