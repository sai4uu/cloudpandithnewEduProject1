# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# range functions to generate value from 0 to 99
df =spark.range(100)

#display data
display(df)