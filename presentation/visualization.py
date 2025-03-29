'''
CST8002 - Programming Language Research Project
Professor: Tyler DeLay
Author: Aly Kaamoush
Date: April 6, 2025
Description: Visualization module for generating and displaying charts
'''

import matplotlib.pyplot as plt
import numpy as np

class ChartGenerator:
    '''Generates and displays various chart types using matplotlib'''
    
    def __init__(self):
        '''Initialize chart generator'''
        self.author_name = "Program by Aly Kaamoush"
    
    def create_vertical_bar_chart(self, labels, values, title, x_label, y_label):
        '''
        Create and display a vertical bar chart
        
        Args:
            labels: List of labels for x-axis
            values: List of values for y-axis
            title: Chart title
            x_label: Label for x-axis
            y_label: Label for y-axis
        '''
        plt.figure(figsize=(10, 6))
        plt.bar(labels, values, color='skyblue')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        # Add author name as a footer
        plt.figtext(0.5, 0.01, self.author_name, ha='center', fontsize=10)
        
        # Display the chart
        plt.show()
    
    def create_horizontal_bar_chart(self, labels, values, title, x_label, y_label):
        '''
        Create and display a horizontal bar chart
        
        Args:
            labels: List of labels for y-axis
            values: List of values for x-axis
            title: Chart title
            x_label: Label for x-axis
            y_label: Label for y-axis
        '''
        plt.figure(figsize=(10, 8))
        plt.barh(labels, values, color='lightgreen')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.tight_layout()
        
        # Add author name as a footer
        plt.figtext(0.5, 0.01, self.author_name, ha='center', fontsize=10)
        
        # Display the chart
        plt.show()
    
    def save_chart(self, filename):
        '''
        Save the current chart to a file
        
        Args:
            filename: Name of the file to save the chart to
        '''
        plt.savefig(filename)
        plt.close()
        return filename

