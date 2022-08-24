import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Ceci est un test')

st.write("1, 2, 1, 2, test, test")

DF = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv', sep=',')

DF

--

viz_correlation = sns.heatmap(DF.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)


option = st.selectbox(
     'What country do you want to display ?',
     ('US', 'Europe', 'Japan'))

st.write('You selected:', option)

--

sns.set_style("white")

# Basic 2D density plot
kdeplot1 = sns.kdeplot(x=DF.cylinders, y=DF.mpg)
st.pyplot(kdeplot1.figure)
 
# Custom the color, add shade and bandwidth
kdeplot2 =sns.kdeplot(x=DF.cylinders, y=DF.hp, cmap="Reds", shade=True, bw_adjust=.5)
st.pyplot(kdeplot2.figure)

# Add thresh parameter
kdeplot3 =sns.kdeplot(x=DF.cylinders, y=DF.weightlbs, cmap="Blues", shade=True, thresh=0)
st.pyplot(kdeplot3.figure)

--

with sns.axes_style('white'):
    jointplot1 = sns.jointplot(x=DF.cylinders, y=DF.mpg, kind='kde')
st.pyplot(jointplot1.figure)

--

with sns.axes_style('white'):
    jointplot2 = sns.jointplot(x=DF.cylinders, y=DF.mpg, kind='hex')
st.pyplot(jointplot2.figure)

--

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
 


