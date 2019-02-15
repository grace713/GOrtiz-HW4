#!/usr/bin/env python
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# ## Player Count

# * Display the total number of players
# 

# In[2]:



player_count = len(purchase_data["SN"].value_counts())
total_players = pd.DataFrame([player_count], columns = ["Total Players"])

print(total_players)


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[3]:



# Count, Average Price, Number of Purchases and Total Revenue
unique_items = purchase_data["Item ID"].count()
average_price = purchase_data["Price"].mean()
num_purchases = purchase_data["Purchase ID"].count()
total_revenue = purchase_data["Price"].sum()

# Create new DataFrame
summary_df = pd.DataFrame({"Number of Unique Items": [unique_items],
                           "Average Price": "$" + str("%.2f" % average_price),
                           "Number of Purchases": str(num_purchases),
                           "Total Revenue": "$" + str(total_revenue),})
summary_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[4]:


gender_grouped = purchase_data[["SN","Gender","Price"]]
counts_g = gender_grouped["Gender"].value_counts()

# Purchase counts
purchase_counts = [counts_g[0],counts_g[1],counts_g[2]]

gender_grouped = gender_grouped.groupby("Gender")
total_spent = gender_grouped.sum()
total_spent

# Total Purchase Value
total_purchase_value_g = [total_spent.iloc[1,0], total_spent.iloc[0,0], total_spent.iloc[2,0]]

# Average Purchase Price
avg_purchase_g = [total_spent.iloc[1,0]/counts_g[0], total_spent.iloc[0,0]/counts_g[1], total_spent.iloc[2,0]/counts_g[2]]

# Average Total Purchase Per Person
avg_tot_g = [total_spent.iloc[1,0]/gender_counts[0], total_spent.iloc[0,0]/gender_counts[1], total_spent.iloc[2,0]/gender_counts[2]]

# Create DataFrame & setting index
purchase_analysis_g_df = pd.DataFrame({
    "Purchase Count": purchase_counts,
    "Average Purchase Price": avg_purchase_g,
    "Total Purchase Value": total_purchase_value_g,
    "Average Total Purchase Per Person": avg_tot_g,
    "Gender": ["Male", "Female", "Other / Non-Disclosed"]
})
purchase_analysis_g_df = purchase_analysis_g_df.set_index("Gender")
purchase_analysis_g_df = purchase_analysis_g_df[["Purchase Count", "Average Purchase Price", "Total Purchase Value",
                                                 "Average Total Purchase Per Person"]]

# Formatting Prices
purchase_analysis_g_df.style.format({"Average Purchase Price": "${:.2f}", "Average Total Purchase Per Person": "${:.2f}",
                                     "Total Purchase Value":"${:.2f}"})


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[5]:


# Group by gender and get count
gender_grouped = purchase_data[["SN", "Gender"]]
gender_grouped = gender_grouped.drop_duplicates()
gender_counts = gender_grouped["Gender"].value_counts()

# List of values
total_counts = [gender_counts[0],gender_counts[1],gender_counts[2]]
gender_percents = [round((gender_counts[0]/player_count)*100,2),round((gender_counts[1]/player_count)*100,2),round((gender_counts[2]/player_count)*100,2)]

# Create Dataframe
gender_demo_df = pd.DataFrame({
    "Total Count": total_counts,
    "Percentage of Players": gender_percents,
})
gender_demo_df.index = (["Male", "Female", "Other / Non-Disclosed"])
gender_demo_df


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[6]:


gender_grouped = purchase_data[["SN","Gender","Price"]]
counts_g = gender_grouped["Gender"].value_counts()

# Purchase counts
purchase_counts = [counts_g[0],counts_g[1],counts_g[2]]

gender_grouped = gender_grouped.groupby("Gender")
total_spent = gender_grouped.sum()
total_spent

# Total Purchase Value
total_purchase_value_g = [total_spent.iloc[1,0], total_spent.iloc[0,0], total_spent.iloc[2,0]]

# Average Purchase Price
avg_purchase_g = [total_spent.iloc[1,0]/counts_g[0], total_spent.iloc[0,0]/counts_g[1], total_spent.iloc[2,0]/counts_g[2]]

# Average Total Purchase Per Person
avg_tot_g = [total_spent.iloc[1,0]/gender_counts[0], total_spent.iloc[0,0]/gender_counts[1], total_spent.iloc[2,0]/gender_counts[2]]

# Create DataFrame & setting index
purchase_analysis_g_df = pd.DataFrame({
    "Purchase Count": purchase_counts,
    "Average Purchase Price": avg_purchase_g,
    "Total Purchase Value": total_purchase_value_g,
    "Average Total Purchase Per Person": avg_tot_g,
    "Gender": ["Male", "Female", "Other / Non-Disclosed"]
})
purchase_analysis_g_df = purchase_analysis_g_df.set_index("Gender")
purchase_analysis_g_df = purchase_analysis_g_df[["Purchase Count", "Average Purchase Price", "Total Purchase Value",
                                                 "Average Total Purchase Per Person"]]

# Formatting Prices
purchase_analysis_g_df.style.format({"Average Purchase Price": "${:.2f}", "Average Total Purchase Per Person": "${:.2f}",
                                     "Total Purchase Value":"${:.2f}"})


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[7]:


# Purchase Count
purchase_10 = purchase_data[purchase_data["Age"] < 10].count()[0]
purchase_14 = purchase_data[(purchase_data["Age"] >= 10) & (purchase_data["Age"] <= 14)].count()[0]
purchase_19 = purchase_data[(purchase_data["Age"] >= 15) & (purchase_data["Age"] <= 19)].count()[0]
purchase_24 = purchase_data[(purchase_data["Age"] >= 20) & (purchase_data["Age"] <= 24)].count()[0]
purchase_29 = purchase_data[(purchase_data["Age"] >= 25) & (purchase_data["Age"] <= 29)].count()[0]
purchase_34 = purchase_data[(purchase_data["Age"] >= 30) & (purchase_data["Age"] <= 34)].count()[0]
purchase_39 = purchase_data[(purchase_data["Age"] >= 35) & (purchase_data["Age"] <= 39)].count()[0]
purchase_40 = purchase_data[purchase_data["Age"] >= 40].count()[0]
purchases_a = [purchase_10, purchase_14, purchase_19, purchase_24, purchase_29, purchase_34, purchase_39, purchase_40]

# Total Purchase Value
total_10 = purchase_data.loc[purchase_data['Age'] < 10, 'Price'].sum()
total_14 = purchase_data.loc[(purchase_data['Age'] >= 10) & (purchase_data['Age'] <=14), 'Price'].sum()
total_19 = purchase_data.loc[(purchase_data['Age'] >= 15) & (purchase_data['Age'] <=19), 'Price'].sum()
total_24 = purchase_data.loc[(purchase_data['Age'] >= 20) & (purchase_data['Age'] <=24), 'Price'].sum()
total_29 = purchase_data.loc[(purchase_data['Age'] >= 25) & (purchase_data['Age'] <=29), 'Price'].sum()
total_34 = purchase_data.loc[(purchase_data['Age'] >= 30) & (purchase_data['Age'] <=34), 'Price'].sum()
total_39 = purchase_data.loc[(purchase_data['Age'] >= 35) & (purchase_data['Age'] <=39), 'Price'].sum()
total_40 = purchase_data.loc[purchase_data['Age'] >= 40, 'Price'].sum()
totals_a = [total_10, total_14, total_19, total_24, total_29, total_34, total_39, total_40]

# Age count
df2 = purchase_data[["SN","Age"]]
df2 = df2.drop_duplicates()
age_10 = df2[df2["Age"] < 10].count()[0]
age_14 = df2[(df2["Age"] >= 10) & (df2["Age"] <= 14)].count()[0]
age_19 = df2[(df2["Age"] >= 15) & (df2["Age"] <= 19)].count()[0]
age_24 = df2[(df2["Age"] >= 20) & (df2["Age"] <= 24)].count()[0]
age_29 = df2[(df2["Age"] >= 25) & (df2["Age"] <= 29)].count()[0]
age_34 = df2[(df2["Age"] >= 30) & (df2["Age"] <= 34)].count()[0]
age_39 = df2[(df2["Age"] >= 35) & (df2["Age"] <= 39)].count()[0]
age_40 = df2[df2["Age"] >= 40].count()[0]
ages = [age_10, age_14, age_19, age_24, age_29, age_34, age_39, age_40]

# Average Purchase Price
avg_price_a = [total_10/purchase_10, total_14/purchase_14, total_19/purchase_19, total_24/purchase_24, total_29/purchase_29,
              total_34/purchase_34, total_39/purchase_39, total_40/purchase_40]

# Average Total Purchase Per Person
norms_a = [total_10/age_10, total_14/age_14, total_19/age_19, total_24/age_24, total_29/age_29, total_34/age_34,
           total_39/age_39, total_40/age_40]

# Create dictionary
puchase_analysis_a = {
    "Purchase Count": purchases_a,
    "Average Purchase Price": avg_price_a,
    "Total Purchase Value": totals_a,
    "Average Total Purchase Per Person": norms_a
}

# Create DataFrame & setting index
purchase_analysis_a_df = pd.DataFrame(puchase_analysis_a)
purchase_analysis_a_df = purchase_analysis_a_df[['Purchase Count', 'Average Purchase Price', 'Total Purchase Value',
                                                 'Average Total Purchase Per Person']]
purchase_analysis_a_df.index = (["<10", "10-14","15-19","20-24","25-29","30-34","35-39","40+"])

# Formatting Prices
purchase_analysis_a_df.style.format({"Average Purchase Price": "${:.2f}", "Average Total Purchase Per Person": "${:.2f}",
                                     "Total Purchase Value":"${:.2f}"})


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[8]:


df3 = purchase_data[["SN","Price","Item Name"]]
total_spent = df3.groupby("SN").sum()
total_spent.sort_values(by = "Price", ascending = False, inplace = True)

# Top Spender SN
names = list(total_spent.index.values)
top_names = [names[0],names[1],names[2],names[3],names[4]]

# Total Purchase Values
total_purchase_values_1 = total_spent.iloc[0,0]
total_purchase_values_2 = total_spent.iloc[1,0]
total_purchase_values_3 = total_spent.iloc[2,0]
total_purchase_values_4 = total_spent.iloc[3,0]
total_purchase_values_5 = total_spent.iloc[4,0]
top_purchase_values = [total_spent.iloc[0,0], total_spent.iloc[1,0], total_spent.iloc[2,0], total_spent.iloc[3,0],
                      total_spent.iloc[4,0]]

# Purchase Counts
top_purchase_counts_1 = df3[df3["SN"] == names[0]].count()[0]
top_purchase_counts_2 = df3[df3["SN"] == names[1]].count()[0]
top_purchase_counts_3 = df3[df3["SN"] == names[2]].count()[0]
top_purchase_counts_4 = df3[df3["SN"] == names[3]].count()[0]
top_purchase_counts_5 = df3[df3["SN"] == names[4]].count()[0]
top_purchase_counts = [top_purchase_counts_1, top_purchase_counts_2, top_purchase_counts_3, top_purchase_counts_4,
                       top_purchase_counts_5]

# Average Purchase Prices
avg_price_1 = total_purchase_values_1/top_purchase_counts_1
avg_price_2 = total_purchase_values_2/top_purchase_counts_2
avg_price_3 = total_purchase_values_3/top_purchase_counts_3
avg_price_4 = total_purchase_values_4/top_purchase_counts_4
avg_price_5 = total_purchase_values_5/top_purchase_counts_5
avg_prices = [avg_price_1, avg_price_2, avg_price_3, avg_price_4, avg_price_5]

# Top Spender Dictionary
top_spenders_dict = {
    "Purchase Count": top_purchase_counts,
    "Average Purchase Price": avg_prices,
    "Total Purchase Value": top_purchase_values,
    "SN": top_names
}

# Create DataFrame & setting index
top_spenders_df = pd.DataFrame(top_spenders_dict)
top_spenders_df = top_spenders_df.set_index("SN")
top_spenders_df = top_spenders_df[["Purchase Count", "Average Purchase Price", "Total Purchase Value"]]

# Formatting prices
top_spenders_df.style.format({"Average Purchase Price": "${:.2f}", "Total Purchase Value": "${:.2f}"})


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[9]:


df4 = purchase_data[["Item ID", "Item Name", "Price"]]
pop_items = df4.groupby("Item ID").count()
pop_items.sort_values(by = "Item Name", ascending = False, inplace = True)
df4 = df4.drop_duplicates(["Item ID", "Item Name"])

# Item IDs
item_ids = [pop_items.index[0], pop_items.index[1], pop_items.index[2], pop_items.index[3], pop_items.index[4]]

# Item Names
name_1 = df4.loc[df4["Item ID"] == item_ids[0], "Item Name"].item()
name_2 = df4.loc[df4["Item ID"] == item_ids[1], "Item Name"].item()
name_3 = df4.loc[df4["Item ID"] == item_ids[2], "Item Name"].item()
name_4 = df4.loc[df4["Item ID"] == item_ids[3], "Item Name"].item()
name_5 = df4.loc[df4["Item ID"] == item_ids[4], "Item Name"].item()
pop_item_names = [name_1, name_2, name_3, name_4, name_5]

# Purchase Counts
item_counts = [pop_items.iloc[0,0], pop_items.iloc[1,0], pop_items.iloc[2,0], pop_items.iloc[3,0], pop_items.iloc[4,0]]

# Item Prices
price_1 = df4.loc[df4["Item Name"] == pop_item_names[0], "Price"].item()
price_2 = df4.loc[df4["Item Name"] == pop_item_names[1], "Price"].item()
price_3 = df4.loc[df4["Item Name"] == pop_item_names[2], "Price"].item()
price_4 = df4.loc[df4["Item Name"] == pop_item_names[3], "Price"].item()
price_5 = df4.loc[df4["Item Name"] == pop_item_names[4], "Price"].item()
item_prices = [price_1,price_2,price_3,price_4,price_5]

# Total Purchase Value
total_values = [pop_items.iloc[0,0]*price_1, pop_items.iloc[1,0]*price_2, pop_items.iloc[2,0]*price_3, 
                pop_items.iloc[3,0]*price_4, pop_items.iloc[4,0]*price_5]

# Create DataFrame & setting index
pop_items_df = pd.DataFrame({
    "Item ID": item_ids,
    "Item Name": pop_item_names,
    "Purchase Count": item_counts,
    "Item Price": item_prices,
    "Total Purchase Value": total_values
})
pop_items_df = pop_items_df.set_index(["Item ID", "Item Name"])
pop_items_df = pop_items_df[["Purchase Count", "Item Price", "Total Purchase Value"]]

# Formatting Prices
pop_items_df.style.format({"Item Price": "${:.2f}", "Total Purchase Value": "${:.2f}"})


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[10]:


df4 = purchase_data[["Item ID", "Item Name", "Price"]]
profit_items = df4.groupby("Item ID").sum()
profit_items.sort_values(by = "Price", ascending = False, inplace = True)
df4 = df4.drop_duplicates(["Item ID", "Price"])

# Item IDs
item_ids = [profit_items.index[0], profit_items.index[1], profit_items.index[2], profit_items.index[3], profit_items.index[4]]

# Item Names
name_1 = df4.loc[df4["Item ID"] == item_ids[0], "Item Name"].item()
name_2 = df4.loc[df4["Item ID"] == item_ids[1], "Item Name"].item()
name_3 = df4.loc[df4["Item ID"] == item_ids[2], "Item Name"].item()
name_4 = df4.loc[df4["Item ID"] == item_ids[3], "Item Name"].item()
name_5 = df4.loc[df4["Item ID"] == item_ids[4], "Item Name"].item()
profit_names = [name_1, name_2, name_3, name_4, name_5]

# Total Purchase Value
values = [profit_items.iloc[0,0],profit_items.iloc[1,0],profit_items.iloc[2,0],profit_items.iloc[3,0],profit_items.iloc[4,0]]

# Item Price
price_1 = df4.loc[df4["Item ID"] == item_ids[0], "Price"].item()
price_2 = df4.loc[df4["Item ID"] == item_ids[1], "Price"].item()
price_3 = df4.loc[df4["Item ID"] == item_ids[2], "Price"].item()
price_4 = df4.loc[df4["Item ID"] == item_ids[3], "Price"].item()
price_5 = df4.loc[df4["Item ID"] == item_ids[4], "Price"].item()
profit_prices = [price_1,price_2,price_3,price_4,price_5]

# Purchase counts
df5 = purchase_data[["Item ID", "Item Name", "Price"]].groupby("Item Name").count()
count_1 = df5.loc[df5.index == profit_names[0], "Item ID"].item()
count_2 = df5.loc[df5.index == profit_names[1], "Item ID"].item()
count_3 = df5.loc[df5.index == profit_names[2], "Item ID"].item()
count_4 = df5.loc[df5.index == profit_names[3], "Item ID"].item()
count_5 = df5.loc[df5.index == profit_names[4], "Item ID"].item()
counts = [count_1, count_2, count_3, count_4, count_5]

# Create DataFrame & setting index
profit_items_df = pd.DataFrame({
    "Item ID": item_ids,
    "Item Name": profit_names,
    "Purchase Count": counts,
    "Item Price": profit_prices,
    "Total Purchase Value": values
})
profit_items_df = profit_items_df.set_index(["Item ID", "Item Name"])
profit_items_df = profit_items_df[["Purchase Count", "Item Price", "Total Purchase Value"]]

# Formatting prices
profit_items_df.style.format({"Item Price": "${:.2f}", "Total Purchase Value": "${:.2f}"})

