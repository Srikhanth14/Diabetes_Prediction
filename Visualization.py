import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def visualization(df):

    # Title
    st.title('📊  Diabetes Data Visualizer')

    col1, col2 = st.columns(2)

    columns = df.columns.tolist()

    with col1:
        st.write("")
        st.write(df.head(8))

    with col2:
        # Allow the user to select columns for plotting
        x_axis = st.selectbox('Select the X-axis', options=columns+["None"])
        y_axis = st.selectbox('Select the Y-axis', options=columns+["None"])
        hue = st.selectbox('Select the hue',options=columns+['None'])

        plot_list = ['Count Plot', 'Bar Plot', 'Box Plot', 'Histogram', 'Violin Plot', 'Line Plot', 'Heatmap']
        # Allow the user to select the type of plot
        plot_type = st.selectbox('Select the type of plot', options=plot_list)

    # Generate the plot based on user selection
    if st.button('Generate Plot'):

        fig, ax = plt.subplots(figsize=(6, 4))

        if plot_type == 'Count Plot':
            sns.countplot(x=df[x_axis],hue=df[hue], ax=ax)
        elif plot_type == 'Bar Plot':
            sns.barplot(x=df[x_axis], y=df[y_axis], errorbar=None,ax=ax)
        elif plot_type == 'Box Plot':
            sns.boxplot(x=df[x_axis], y=df[y_axis], ax=ax)
        elif plot_type == 'Histogram':
            sns.histplot(df[x_axis], kde=True, ax=ax)
            y_axis='Density'
        elif plot_type == 'Violin Plot':
            sns.violinplot(x=df[x_axis], y=df[y_axis], ax=ax)
        elif plot_type == 'Line Plot':
            sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)
        elif plot_type == 'Heatmap':
            sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)

        # Adjust label sizes
        ax.tick_params(axis='x', labelsize=10)  # Adjust x-axis label size
        ax.tick_params(axis='y', labelsize=10)  # Adjust y-axis label size

        # Adjust title and axis labels with a smaller font size
        plt.title(f'{plot_type} of {y_axis} vs {x_axis}', fontsize=12)
        plt.xlabel(x_axis, fontsize=10)
        plt.ylabel(y_axis, fontsize=10)

        # Show the results
        st.pyplot(fig)



