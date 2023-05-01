import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import numpy as np

df = pd.read_excel('data/calories_yt.xlsx',sheet_name='Totals',header=1)
df = df.dropna(thresh=3)

df1=pd.melt(df, id_vars =['Year'],var_name='Food',value_name='Calories')
df1['Decade'] = np.where(df1['Year']<1980, '1970s'
, np.where(df1['Year']<1990,'1980s'
, np.where(df1['Year']<2000,'1990s'
, np.where(df1['Year']<2010,'2000s','2010s'))))

df2=pd.read_excel('data/calories_yt.xlsx',sheet_name='DETAIL')
df2=df2.dropna(thresh=3)

food1_df=df2.groupby(['Food 1','Year'],as_index=False)['Avg. Per Capita Calories'].sum()
food1_df['Decade'] = np.where(food1_df['Year']<1980, '1970s'
, np.where(food1_df['Year']<1990,'1980s'
, np.where(food1_df['Year']<2000,'1990s'
, np.where(food1_df['Year']<2010,'2000s','2010s'))))

df3=df2[['Food','Food 1']].copy()
df3=df3.drop_duplicates()
df3=df3.reset_index()
df3=df3.drop(columns='index')

joined=food1_df.join(df3.set_index('Food 1'), on = 'Food 1')

st.image('images/Collage3.jpg')
st.title('Loss-Adjusted Food Availability in the United States 1970-2018')

st.sidebar.header("Filters")

decades = list(df1['Decade'].drop_duplicates())
decades_filter = st.sidebar.multiselect(
    'Choose decade:', decades)
food_list=list(joined['Food'].drop_duplicates())
food_filter = st. sidebar.selectbox('Choose Food Category',food_list,default='Dairy')

tab1, tab2, tab3 = st.tabs(['Overall Distribution', 'Year over Year', 'Detail'])

with tab1:

        df1 = df1[df1['Food']!='Total']
        if decades_filter:
            df1 = df1[df1['Decade'].isin(decades_filter)]
        else: df1=df1

        graph = alt.Chart(df1).mark_bar().encode(
            x=alt.X('mean(Calories)',title='Average Per Capita Calories'),
            y=alt.Y('Food',title="Food",sort='-x'),
            text='mean(Calories)'
        )

        graph=graph.mark_bar() + graph.mark_text(align='left', dx=2).encode(
                text=alt.Text("mean(Calories):Q", format=",.0f")
                )

        st.altair_chart(graph, use_container_width=True)

with tab2:
    df1 = df1[df1['Food']!='Total']
    if decades_filter:
        df1 = df1[df1['Decade'].isin(decades_filter)]
    else: df1=df1   

    graph2= alt.Chart(df1,title='Average Per Capita Calories by Year').mark_line().encode(
    x='Year:N',
    y='Calories',
    color ='Food:N'
    )
    st.altair_chart(graph2,use_container_width=True)

with tab3:
    st.subheader('Please Select a Food Category for detail')
    
    if decades_filter:
        joined=joined[joined['Decade'].isin(decades_filter)]
    else: joined=joined

    fig = px.bar(joined[joined['Food'] ==food_filter], x="Year", y="Avg. Per Capita Calories", color="Food 1", title=food_filter)
    st.plotly_chart(fig,use_container_width=True)

with st.expander('About this app'):
  st.write("This project uses data from the [USDA](https://www.ers.usda.gov/data-products/food-availability-per-capita-data-system/)")
  st.image('images/usda-logo-color.png', width=50)
