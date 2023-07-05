# some helper lists and functions

def get_state_abbreviations():
    """
    Returns a dictionary mapping the names of U.S. states and territories
    to their corresponding two-letter abbreviations.
    
    Returns:
        dict: A dictionary with state names as keys and abbreviations as values.
    """
    return {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY",
        "District of Columbia": "DC",
        "Puerto Rico": "PR",
        "Guam": "GU",
        "American Samoa": "AS",
        "U.S. Virgin Islands": "VI",
        "Northern Mariana Islands": "MP",
    }


def calculate_dataframe_memory_usage(df):
    """
    Calculate the memory usage of a Pandas DataFrame in megabytes.
    
    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame for which to calculate memory usage.
    
    Returns
    -------
    float
        The memory usage of the DataFrame in megabytes.
    """
    
    # Calculate the memory usage of each column in bytes
    memory_usage_per_column = df.memory_usage(deep=True)
    
    # Sum up the memory usage of each column to get total memory usage in bytes
    total_memory_usage_in_bytes = memory_usage_per_column.sum()
    
    # Convert the total memory usage to MB
    total_memory_usage_in_mb = total_memory_usage_in_bytes / (1024 * 1024)
    
    return total_memory_usage_in_mb


def display_dataframe_overview(df):
    """
    Display an overview of a Pandas DataFrame, including the number of rows,
    number of columns, column names, first 3 rows, last 3 rows, and 3 random samples.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to display the overview for.
    """

    num_rows, num_columns = df.shape
    column_names = df.columns.tolist()

    if len(column_names) < 10:

        print(
            f"DataFrame Overview:\n"
            f"Number of rows: {num_rows}\n"
            f"Number of columns: {num_columns}\n"
            f"Column names: {column_names}\n"
        )

        print("First 3 rows:")
        display(df.head(3))

        print("\nLast 3 rows:")
        display(df.tail(3))

        print("\nRandom 3 samples:")
        display(df.sample(3))

    else:
            print(
            f"DataFrame Overview:\n"
            f"Number of rows: {num_rows}\n"
            f"Number of columns: {num_columns}\n")

            a_string = str(df.columns.tolist()[0:11])
            b_string = str(df.columns.tolist()[11:])
            print(f"cms_df columns:")
            print(a_string[:-1])
            print(f"{b_string[1:]}\n")        

            print("First 3 rows:")
            display(df.head(3))

            print("\nLast 3 rows:")
            display(df.tail(3))

            print("\nRandom 3 samples:")
            display(df.sample(3))


def print_column_names(df):
    """
    Prints the column names of the given DataFrame in two parts: the first 11 and the remaining ones.

    Parameters
    ----------
    dataframe : df
        The DataFrame whose column names are to be printed.
    """
    a_string = str(df.columns.tolist()[0:11])
    b_string = str(df.columns.tolist()[11:])
    print(f"cms_df columns:")
    print(a_string[:-1])
    print(f"{b_string[1:]}\n")


def split_state_county_zip(a_string, re, state_abbreviations):
    """
    This function takes a string in the format of "State:County:Zip_Code and returns a tuple of "County, State" and Zip Code.
    Example: split_state_county_zip("New York:Nassau:11590") ==> ('Nassau County, NY', '11590')

    Args:
        a_string (str): The input string in the format "State:County:Zip_Code"

    Returns:
        tuple: A tuple formatted as ("county and state abbreviation", "zip code".
        Returns None if regex doesn't match
    """



    pattern = r"^(.+):(.+):(\d+)$"
    match = re.match(pattern, a_string)
    if match:
        state, county, zip_code = match.groups()
        state_abbrev = state_abbreviations.get(state)
        if state_abbrev == "LA":
            county_state = f"{county} Parish, {state_abbrev}"
        elif state_abbrev == "AK":
            county_state = f"{county} Borough, {state_abbrev}"
        else:
            county_state = f"{county} County, {state_abbrev}"
        return county_state, zip_code
    else:
        return None






def print_the_stats(merged_mean, result):
    """
    Prints the stats for the regression model
    input: merged_mean (pd.DataFrame)
    return: None
    """

    from scipy.stats import pearsonr 

    print(f"slope of the line: {result.params['Indy_Var']}")
    print(f"Intercept: {result.params['Intercept']}\n")

    # Calculate Pearson correlation coefficient
    merged_mean = merged_mean.dropna()
    x = merged_mean['Indy_Var']
    y = merged_mean['PPP']
    correlation, p_val = pearsonr(x, y)
    correlation = round(correlation, 2)
    p_val = round(p_val, 2)

    print(f"Pearson correlation r: {correlation} with a p-value of: {p_val}")
    if correlation < 0:
        print(f"Negative correlation\n")
    elif correlation > 0:
        print(f"Positive correlation\n")

    print(f"Coefficient of Determination ('goodness of fit') \nR-squared: {result.rsquared}\nR\u00B2 is the proportion of the variance in the dependent variable \nthat is predictable from the independent variable")  


def min_max(df, column_name):
    """
    Print the minimum and maximum value of a specific column in a pandas DataFrame.

    input:
    df : pandas.DataFrame
        The DataFrame from which to find the min and max values.
    column_name : str
        The name of the column in df for which to find the min and max values.

    Prints
    ------
    The minimum and maximum values of the specified column in the DataFrame.
    Each value is printed on a new line, with a label indicating whether it is the min or max value.
    """

    min_value = df[column_name].min()
    max_value = df[column_name].max()

    print(f"{column_name}: 'Minimum value: {min_value}")
    print(f"{column_name}: 'Maximum value: {max_value}")
    print()


def print_the_stats_2(df, result,  indy_var, dep_var):
    """
    Prints the stats for the regression model

    return: None
    """

    from scipy.stats import pearsonr 

    print(f"slope of the line: {(result.params[dep_var])}")
    print(f"Intercept: {round(result.params['Intercept'],4)}\n")

    # Calculate Pearson correlation coefficient
    df = df.dropna()
    x = df[indy_var]
    y = df[dep_var]
    correlation, p_val = pearsonr(x, y)
    correlation = round(correlation, 2)
    p_val = round(p_val, 2)

    print(f"Pearson correlation r: {correlation} with a p-value of: {p_val}")
    if correlation < 0:
        print(f"Negative correlation\n")
    elif correlation > 0:
        print(f"Positive correlation\n")

    print(f"Coefficient of Determination ('goodness of fit') \nR-squared: {round(result.rsquared, 2)}\nR\u00B2 is the proportion of the variance in the dependent variable \nthat is predictable from the independent variable")  
    

def corrStrengthSignificanceAnalysis(df, f1, f2):
    from scipy.stats import pearsonr 
    """
    Calculate and print the Pearson correlation coefficient and p-value
    between two features in a DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - f1 (str): The column name of the first feature.
    - f2 (str): The column name of the second feature.

    Returns:
    None

    """ 
    p_coeff, p_val = pearsonr(df[f1], df[f2])
    print(f"Coefficient: {p_coeff} with p-value: {p_val}")

