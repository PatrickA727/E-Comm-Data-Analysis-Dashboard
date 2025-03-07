import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style='dark')

top_states_df = pd.read_csv("top_5_states.csv")
top_categories_df = pd.read_csv("top_item_categories.csv")

top_states_df.rename(columns={"customer_id": "customer_count"}, inplace=True)

st.header('E-Commerce Data Analysis Project')
st.subheader("Top 5 States with Most E-Commerce Customers")

fig, ax = plt.subplots(figsize=(8, 5))
sns.set_theme(style="darkgrid")
sns.barplot(x=top_states_df["customer_state"], y=top_states_df["customer_count"], palette="Blues_r", ax=ax)

ax.set_xlabel("State")
ax.set_ylabel("Number of Customers")

st.pyplot(fig)

st.subheader('Most sold products by categories in the 5 states with the most E-commerce customers')

fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.barplot(
    y=top_categories_df["customer_state"], 
    x=top_categories_df["count"], 
    hue=top_categories_df["product_category_name"], 
    dodge=False, 
    palette="viridis", 
    ax=ax2
)

# Labels & Title
ax2.set_xlabel("Number of Products Sold by Category", color="black")  
ax2.set_ylabel("State", color="black")
ax2.set_title("Most Sold Product Category in Top 5 States", color="black")

ax2.tick_params(axis="x", colors="black", rotation=0)  
ax2.xaxis.set_major_locator(plt.MaxNLocator(integer=True))  

ax2.tick_params(axis="y", colors="black")
legend = ax2.legend(title="Product Category")
for text in legend.get_texts():
    text.set_color("black") 
legend.get_title().set_color("black")  

st.pyplot(fig2)
