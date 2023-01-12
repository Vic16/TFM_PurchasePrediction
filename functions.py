import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


##############
##############
##############
##############


def profiler(df):
    """
    receive a pandas dataframe and print all features of the table.
    params:
        df: pandas object
        return: none
    """
    print("El dataset se encuentra compuesto por {} filas y {} columnas".format(df.shape[0],df.shape[1]))
    print("-------")
    print("")
    print("Tipos de datos contenidos en la tabla")
    print("-------")
    print("")
    print(df.info())
    print("")
    print("------- Valores nulos")
    print(df.isna().sum())
    print("")
    print("-------")

##############
##############
##############
##############

def count_freq(table, variable):
    """
    Recibe una tabla y una variable categórica y
    devuelve las frecuencias
    
    args:
        table: pandas df object
        variable: str, columna o campo del df
    """
    freq = pd.DataFrame((table.groupby([str(variable)]).size().reset_index(
                                                    name='count').sort_values(
                                                    by = "count", ascending = False)))
    freq["%"] = round((freq['count'] / freq['count'].sum()) * 100, 3)
    return freq   


##############
##############
##############
##############


def graf_freq(df, variable):
    """
    Recibe una tabla y una variable categórica y 
    devuelve el gráfico de frecuencias
    args:
        table: pandas df object
        variable: str, columna o campo del df
    """
    sns.countplot(x = str(variable), 
                  data = df,
                  order = df[str(variable)].value_counts().index,
                  palette="viridis")
    plt.xticks(rotation = 90)
    return plt.show()

##############
##############
##############
##############

def graf_freq_by_target(df, variable, variableHue):
    """
    Recibe una tabla y una variable categórica y 
    devuelve el gráfico de frecuencias agrupado por la variable target
    args:
        table: pandas df object
        variable: str, columna o campo del df
    """
    sns.countplot(x = variable, 
              data = df,
              order = df[variable].value_counts().index,
              hue = variableHue,
              palette="viridis")
    plt.xticks(rotation = 90)
    #plt.legend(title='Depósito a plazo fijo?', 
    #       loc='upper right', labels=['No', 'Yes'])
    return plt.show()


##############
##############
##############
##############


def getBoxPlot(data, columnName):
    """
    """
    sns.boxplot(y=columnName, palette="viridis", data=data).set(title='Boxplot {}'.format(columnName))
    plt.show()

##############
##############
##############
##############

def replaceOuliers(column):
    """
    """
    colReplace = np.array(column)
    median = np.median(column)
    
    upper =  np.percentile(np.array(column),95)
    lower =  np.percentile(np.array(column),5)
    
    colReplace[colReplace[:] > upper] = median
    colReplace[colReplace[:] < lower] = median
    return list(colReplace)