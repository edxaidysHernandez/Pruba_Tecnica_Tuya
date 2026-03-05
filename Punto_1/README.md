# Customer Phone Dataset Pipeline

## Objective

Design a conceptual data pipeline to build a reliable dataset of customer phone numbers, including validation, traceability, and data quality monitoring.

## Solution Overview

The proposed solution implements an automated data pipeline that:

1. Extracts phone numbers from multiple systems
2. Stores raw data for traceability
3. Normalizes phone numbers
4. Applies validation rules
5. Generates a curated dataset for business consumption
6. Monitors data quality through KPIs

## Pipeline Architecture

![Pipeline](diagrams/pipeline_architecture.png)

## Data Model

The system uses a layered approach:

- Raw layer
- Validation layer
- Curated dataset

Details can be found in the documentation folder.

## Data Quality Monitoring

The pipeline includes several KPIs to monitor phone data quality, including:

- percentage of valid phones
- duplicate rate
- invalid phone rate
- phone distribution by source
