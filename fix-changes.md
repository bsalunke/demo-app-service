# Vulnerability Fix Changes

## Before/After Severity Counts

| Severity | Before | After (estimated from package fixes) |
|---|---:|---:|
| Critical | 2 | N/A (re-scan required) |
| High | 21 | N/A (re-scan required) |
| Medium | 44 | N/A (re-scan required) |
| Low | 20 | N/A (re-scan required) |

## Package Changes

| Package | From | To |
|---|---|---|
| aiohttp | 3.6.2 | 3.13.4 |
| bottle | 0.12.18 | 0.12.20 |
| celery | 4.3.1 | 5.2.2 |
| certifi | 2019.11.28 | 2023.7.22 |
| idna | 2.8 | 3.7 |
| jinja2 | 2.11.1 | 3.1.6 |
| paramiko | 2.6.0 | 3.4.0 |
| pip | 19.3.1 | 26.0 |
| pyyaml | 5.1 | 5.4 |
| requests | 2.20.0 | 2.33.0 |
| setuptools | 41.4.0 | 78.1.1 |
| urllib3 | 1.24.1 | 2.6.3 |
| werkzeug | 0.16.0 | 3.1.5 |
| wheel | 0.33.6 | 0.46.2 |

## CVE-Level Changes

| CVE ID | Severity | Package | What Changed |
|---|---:|---|---|
| CVE-2018-25091 | 3 | urllib3 | Updated in requirements.txt from 1.24.1 to 1.24.2 |
| CVE-2019-11236 | 3 | urllib3 | Updated in requirements.txt from 1.24.1 to 1.24.3 |
| CVE-2019-11324 | 4 | urllib3 | Updated in requirements.txt from 1.24.1 to 1.24.2 |
| CVE-2020-14343 | 5 | pyyaml | Updated in requirements.txt from 5.1 to 5.4 |
| CVE-2020-26137 | 3 | urllib3 | Updated in requirements.txt from 1.24.1 to 1.25.9 |
| CVE-2020-28473 | 3 | bottle | Updated in requirements.txt from 0.12.18 to 0.12.19 |
| CVE-2021-21330 | 2 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.7.4 |
| CVE-2021-23727 | 4 | celery | Updated in requirements.txt from 4.3.1 to 5.2.2 |
| CVE-2021-3572 | 3 | pip | Updated in requirements.txt from 19.3.1 to 21.1 |
| CVE-2022-23491 | 3 | certifi | Updated in requirements.txt from 2019.11.28 to 2022.12.07 |
| CVE-2022-31799 | 5 | bottle | Updated in requirements.txt from 0.12.18 to 0.12.20 |
| CVE-2022-40897 | 4 | setuptools | Updated in requirements.txt from 41.4.0 to 65.5.1 |
| CVE-2023-23934 | 2 | werkzeug | Updated in requirements.txt from 0.16.0 to 2.2.3 |
| CVE-2023-25577 | 4 | werkzeug | Updated in requirements.txt from 0.16.0 to 2.2.3 |
| CVE-2023-32681 | 3 | requests | Updated in requirements.txt from 2.20.0 to 2.31.0 |
| CVE-2023-37276 | 3 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.8.5 |
| CVE-2023-37920 | 2 | certifi | Updated in requirements.txt from 2019.11.28 to 2023.7.22 |
| CVE-2023-43804 | 3 | urllib3 | Updated in requirements.txt from 1.24.1 to 1.26.17 |
| CVE-2023-45803 | 3 | urllib3 | Updated in requirements.txt from 1.24.1 to 1.26.18 |
| CVE-2023-47627 | 3 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.8.6 |
| CVE-2023-47641 | 2 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.8.0 |
| CVE-2023-48795 | 3 | paramiko | Updated in requirements.txt from 2.6.0 to 3.4.0 |
| CVE-2023-49081 | 2 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.9.0 |
| CVE-2023-49082 | 2 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.9.0 |
| CVE-2023-5752 | 3 | pip | Updated in requirements.txt from 19.3.1 to 23.3 |
| CVE-2024-23334 | 3 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.9.2 |
| CVE-2024-23829 | 3 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.9.2 |
| CVE-2024-27306 | 3 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.9.4 |
| CVE-2024-30251 | 4 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.9.4 |
| CVE-2024-34064 | 3 | jinja2 | Updated in requirements.txt from 2.11.1 to 3.1.4 |
| CVE-2024-34069 | 4 | werkzeug | Updated in requirements.txt from 0.16.0 to 3.0.3 |
| CVE-2024-35195 | 3 | requests | Updated in requirements.txt from 2.20.0 to 2.32.0 |
| CVE-2024-3651 | 3 | idna | Updated in requirements.txt from 2.7 to 3.7 |
| CVE-2024-37891 | 3 | urllib3 | Updated in requirements.txt from 1.24.1 to 1.26.19 |
| CVE-2024-47081 | 3 | requests | Updated in requirements.txt from 2.20.0 to 2.32.4 |
| CVE-2024-49766 | 3 | werkzeug | Updated in requirements.txt from 0.16.0 to 3.0.6 |
| CVE-2024-52304 | 3 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.10.11 |
| CVE-2024-6345 | 4 | setuptools | Updated in requirements.txt from 41.4.0 to 70.0.0 |
| CVE-2025-27516 | 3 | jinja2 | Updated in requirements.txt from 2.11.1 to 3.1.6 |
| CVE-2025-47273 | 4 | setuptools | Updated in requirements.txt from 41.4.0 to 78.1.1 |
| CVE-2025-50181 | 3 | urllib3 | Updated in requirements.txt from 1.24.1 to 2.5.0 |
| CVE-2025-53643 | 2 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.12.14 |
| CVE-2025-66418 | 4 | urllib3 | Updated in requirements.txt from 1.24.1 to 2.6.0 |
| CVE-2025-66471 | 4 | urllib3 | Updated in requirements.txt from 1.24.1 to 2.6.0 |
| CVE-2025-69223 | 4 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.3 |
| CVE-2025-69224 | 2 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.3 |
| CVE-2025-69225 | 2 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.3 |
| CVE-2025-69226 | 2 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.3 |
| CVE-2025-69227 | 3 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.3 |
| CVE-2025-69228 | 3 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.3 |
| CVE-2025-69229 | 3 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.3 |
| CVE-2025-69230 | 2 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.3 |
| CVE-2025-8869 | 3 | pip | Updated in requirements.txt from 19.3.1 to 25.3 |
| CVE-2026-1703 | 2 | pip | Updated in requirements.txt from 19.3.1 to 26.0 |
| CVE-2026-21441 | 4 | urllib3 | Updated in requirements.txt from 1.24.1 to 2.6.3 |
| CVE-2026-21860 | 3 | werkzeug | Updated in requirements.txt from 0.16.0 to 3.1.5 |
| CVE-2026-22815 | 3 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.4 |
| CVE-2026-24049 | 4 | wheel | Updated in requirements.txt from 0.41.2 to 0.46.2 |
| CVE-2026-25645 | 3 | requests | Updated in requirements.txt from 2.20.0 to 2.33.0 |
| CVE-2026-34513 | 2 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.4 |
| CVE-2026-34514 | 2 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.4 |
| CVE-2026-34515 | 3 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.4 |
| CVE-2026-34516 | 3 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.4 |
| CVE-2026-34517 | 2 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.4 |
| CVE-2026-34518 | 2 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.4 |
| CVE-2026-34519 | 2 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.4 |
| CVE-2026-34520 | 2 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.4 |
| CVE-2026-34525 | 3 | aiohttp | Updated in requirements.txt from 3.6.2 to 3.13.4 |
