import pandas as pd
import numpy as np


def combine_text_columns(df):

    columns = [

        "scheme_name",
        "short_title",
        "category",
        "scheme_for",
        "gender",
        "occupation",
        "eligibility",
        "key_benefits",
        "documents_required",
        "description",
        "tags"

    ]

    existing = [col for col in columns if col in df.columns]

    df["combined_text"] = df[existing].fillna("").agg(" ".join, axis=1)

    return df


def description_length(df):

    df["description_length"] = (

        df["description"]

        .astype(str)

        .str.len()

    )

    return df


def scheme_name_length(df):

    df["scheme_name_length"] = (

        df["scheme_name"]

        .astype(str)

        .str.len()

    )

    return df


def eligible_age(df):

    df["eligible_age"] = (

        df["min_age"]

        .astype(str)

        +

        "-"

        +

        df["max_age"]

        .astype(str)

    )

    return df


def government_level(df):

    df["government_level"] = df["level"]

    return df

def beneficiary_count(df):

    df["beneficiary_count"] = (

        df["scheme_for"]

        .astype(str)

        .apply(

            lambda x: len(x.split(","))

        )

    )

    return df


def document_count(df):

    df["document_count"] = (

        df["documents_required"]

        .astype(str)

        .apply(

            lambda x: len(x.split(","))

        )

    )

    return df

def benefit_length(df):

    df["benefit_length"] = (

        df["key_benefits"]

        .astype(str)

        .str.len()

    )

    return df


def tag_count(df):

    df["tag_count"] = (

        df["tags"]

        .astype(str)

        .apply(

            lambda x: len(x.split(","))

        )

    )

    return df



def recommendation_text(df):

    df["recommendation_text"] = (

        df["combined_text"]

        +

        " "

        +

        df["eligible_age"]

    )

    return df


