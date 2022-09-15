import matplotlib.pyplot as plt
plt.axis("equal")
name = ("Deep","Yuvraj","Harsh","Sanskar","Sahil","Tejas","Aryan","Pruthvi")
contri = [100,200,150,175,111,201,501,380]
colours = ['black','cyan','lightgreen','violet','magenta','red','green','blue']
plt.pie(contri,labels =name,autopct="%2d%%"color=colours)
plt.show()