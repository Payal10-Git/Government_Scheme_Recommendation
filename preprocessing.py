import pandas as pd
import numpy as np
import re

# -----------------------------------------
# Remove unwanted state columns
# -----------------------------------------

def remove_unwanted_columns(df):

    remove_columns = []

    for col in df.columns:

        if "Schemes" in col:
            remove_columns.append(col)

    df = df.drop(columns=remove_columns)

    return df


# -----------------------------------------
# Standardize column names
# -----------------------------------------

def clean_column_names(df):

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("/", "_")
        .str.replace("-", "_")
    )

    return df


# -----------------------------------------
# Clean text columns
# -----------------------------------------

def clean_text_columns(df):

    object_columns = df.select_dtypes(include="object").columns

    for col in object_columns:

        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.replace("\n", " ", regex=False)
            .str.replace("\t", " ", regex=False)
            .str.replace(r"\s+", " ", regex=True)
        )

    return df


# -----------------------------------------
# Replace Empty Values
# -----------------------------------------

def replace_empty_values(df):

    df.replace(
        [
            "",
            " ",
            "NA",
            "N/A",
            "null",
            "None",
            "nan"
        ],
        np.nan,
        inplace=True
    )

    return df

# -----------------------------------------
# Convert Numeric Columns
# -----------------------------------------


# -----------------------------------------
# Convert Numeric Columns
# -----------------------------------------

import pandas as pd
import numpy as np

def convert_numeric_columns(df):

    # Numeric columns in your dataset
    numeric_columns = [
        "min_age",
        "max_age",
        "interest_rate",
        "repayment_period"
    ]

    for col in numeric_columns:

        if col in df.columns:

            # Convert to string first
            df[col] = df[col].astype(str)

            # Remove unwanted characters
            df[col] = (
                df[col]
                .str.replace("%", "", regex=False)
                .str.replace(",", "", regex=False)
                .str.replace("years", "", case=False, regex=False)
                .str.replace("year", "", case=False, regex=False)
                .str.replace("months", "", case=False, regex=False)
                .str.replace("month", "", case=False, regex=False)
                .str.strip()
            )

            # Convert to numeric
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df



# def convert_numeric_columns(df):

#     numeric_columns = [
#         "min_age",
#         "max_age",
#         "interest_rate",
#         "repayment_period"
#     ]

#     for col in numeric_columns:

#         if col in df.columns:
#             df[col] = pd.to_numeric(df[col], errors="coerce")

#     return df


# -----------------------------------------
# Fill Missing Values
# -----------------------------------------

def fill_missing_values(df):

    for col in df.columns:

        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna("Not Specified")

    return df

# -----------------------------------------
# Clean URLs
# -----------------------------------------

def clean_urls(df):

    if "official_website" in df.columns:

        df["official_website"] = (
            df["official_website"]
            .str.strip()
        )

    if "scheme_url" in df.columns:

        df["scheme_url"] = (
            df["scheme_url"]
            .str.strip()
        )

    return df


# -----------------------------------------
# Standardize Gender
# -----------------------------------------

def clean_gender(df):

    if "gender" not in df.columns:
        return df

    gender_map = {

        "male":"Male",
        "female":"Female",
        "both":"All",
        "all":"All",
        "men":"Male",
        "women":"Female"

    }

    df["gender"] = (
        df["gender"]
        .str.lower()
        .replace(gender_map)
    )

    return df


# -----------------------------------------
# Standardize State
# -----------------------------------------

def clean_state(df):

    if "state_ut" not in df.columns:
        return df

    df["state_ut"] = (
        df["state_ut"]
        .str.title()
        .str.strip()
    )

    return df


# -----------------------------------------
# Clean Ministry
# -----------------------------------------

def clean_ministry(df):

    if "ministry" not in df.columns:
        return df

    df["ministry"] = (
        df["ministry"]
        .str.title()
    )

    return df


# -----------------------------------------
# Clean Scheme Name
# -----------------------------------------

def clean_scheme_name(df):

    df["scheme_name"] = (
        df["scheme_name"]
        .str.title()
        .str.strip()
    )

    return df


# -----------------------------------------
# Remove Duplicate Schemes
# -----------------------------------------

def remove_duplicates(df):

    df = df.drop_duplicates(
        subset="scheme_name"
    )

    return df