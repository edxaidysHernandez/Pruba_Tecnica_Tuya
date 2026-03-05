
# Data Engineering Technical Exercise – Phone Numbers Dataset

## 1. Objective

Design a **reliable dataset of customer phone numbers** that can be used by business teams to improve
communication with users. The dataset must include:

- Data validation
- Data normalization
- Traceability of the data
- Quality monitoring
- Automated pipeline

The solution should follow **data engineering best practices** and be deployable through CI/CD.

---

# 2. Data Sources

Customer phone numbers may originate from multiple operational systems.

| Source | Description |
|------|------| CRM | Customer profile information |
| Mobile App | User registration or account updates |
| Call Center | Phone numbers provided during support calls |
| Web Forms | Customer signup forms |

Because these systems are independent, **data quality may vary** and requires validation.

---

# 3. Pipeline Architecture

The dataset is generated through an automated pipeline.

```
            Data Sources
                 |
                 v
           Data Extraction
                 |
                 v
            Raw Storage
                 |
                 v
       Data Cleaning / Normalization
                 |
                 v
           Data Validation
                 |
                 v
          Trusted Dataset
                 |
                 v
       Analytics / KPI Monitoring
```

This pipeline runs automatically on a scheduled basis (for example daily).

---

# 4. Data Layers

A layered architecture is used to preserve traceability.

| Layer | Purpose |
|-----|-----| Raw | Stores data exactly as received |
| Clean | Standardized and normalized data |
| Trusted | Validated dataset ready for business usage |

---

# 5. Data Model

### Raw Table

| Field | Description |
|------|------| source_system | Origin of the data |
| customer_id | Unique identifier of the customer |
| phone_raw | Phone number as received |
| ingestion_timestamp | Timestamp when the record was ingested |

### Clean Table

| Field | Description |
|------|------| customer_id | Customer identifier |
| phone_number | Normalized phone number |
| country_code | Country prefix |
| phone_length | Number length |
| normalization_status | Status of normalization |

### Trusted Dataset

| Field | Description |
|------|------| customer_id | Customer identifier |
| phone_number | Validated phone number |
| validation_status | Valid / Invalid |
| confidence_score | Quality score |
| last_updated | Last update timestamp |

---

# 6. Data Normalization

Phone numbers are standardized to a common format.

Example:

Input values:

```
+57 3001234567
300-123-4567
003573001234567
```

Normalized format:

```
+573001234567
```

---

# 7. Validation Rules

The pipeline applies several validation rules.

| Rule | Description |
|----|----| Format validation | Phone must contain only numeric characters |
| Length validation | Number length must match country standard |
| Duplicate detection | Remove duplicated phone numbers |
| Customer consistency | Phone must be associated with a valid customer |

---

# 8. Example Validation Pseudocode

```python
def validate_phone(phone):

    phone = normalize(phone)

    if not only_digits(phone):
        return "invalid"

    if not valid_length(phone):
        return "invalid"

    return "valid"
```

---

# 9. Confidence Score

Each phone number receives a score representing data reliability.

Example:

| Condition | Score |
|------|------| Valid format | +0.4 |
| Used recently | +0.3 |
| Not duplicated | +0.3 |

Total score:

```
confidence_score = validation + recency + uniqueness
```

---

# 10. CI/CD Integration

The pipeline is deployed using CI/CD practices.

Typical workflow:

```
Developer pushes code
        |
        v
Automated tests executed
        |
        v
Pipeline deployed automatically
        |
        v
Scheduled execution
```

CI/CD ensures:

- reproducible deployments
- version control
- automated testing

---

# 11. Data Quality Monitoring

A monitoring layer calculates **KPIs about phone data quality**.

### Example KPIs

| KPI | Description |
|----|----| Valid phone rate | Percentage of valid phone numbers |
| Duplicate rate | Percentage of duplicated numbers |
| Coverage | Customers with at least one phone |
| Update recency | Average time since last update |

These metrics help business teams monitor dataset health.

---

# 12. Traceability

Traceability is ensured through:

- ingestion timestamps
- source system tracking
- validation logs
- historical updates

This allows identifying **where each phone number came from and how it was processed**.

---

# 13. Final Result

The final dataset provides:

- Clean and validated phone numbers
- High reliability for communication campaigns
- Data quality monitoring through KPIs
- Full traceability of the data lifecycle

This architecture enables a **scalable and automated data pipeline** suitable for enterprise environments.

