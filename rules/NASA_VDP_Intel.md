# NASA VDP Intelligence — CrowdStream Full Analysis
## All 46 Pages Scraped | 914 Accepted | 509 Disclosed | Updated 2026-09-02

---

## SCOPE & RULES OF ENGAGEMENT
*Scraped from nasa.gov/vulnerability-disclosure-policy — 2026-09-02*

### In-Scope Domains (ONLY these — all others are OOS)

| Domain | Notes |
|---|---|
| `*.nasa.gov` | All NASA-managed systems on the internet under nasa.gov |
| `usgeo.gov` | In scope |
| `globe.gov` | In scope |
| `nspires.nasaprs.com` | In scope |
| `nsc.nasa.gov` | In scope |

**Important:** "Any domain/property of NASA not listed in the targets section is OUT OF SCOPE. Any service not expressly listed above, such as connected services, are excluded."

### Explicitly Out-of-Scope Vulnerability Types

These are listed in the NASA official policy — submit any of these and risk account flags:

| Type | Policy wording |
|---|---|
| Social engineering | Not authorized (phishing, getting user to click links) |
| DoS / Rate Limiting / Spam | Layer 7 DoS, Slowloris, etc. |
| Clickjacking | Only on pages with NO sensitive actions |
| `xmlrpc.php` endpoint | **Any report** for this endpoint is out of scope |
| `/wp-json/wp/v2/users` endpoint | **Any report** for this endpoint is out of scope |
| Automated scans without PoC | Tool output alone is rejected |
| Software version disclosure | Only rejected without a working PoC demonstrating exploitability |
| Known-vulnerable library | Only rejected without evidence of exploitability |
| Missing best practices | Headers, captcha, insecure certs = instant reject |
| Missing security headers | HSTS, CSP, etc. — not accepted unless leads directly to a vuln |
| Insecure SSL/TLS | Ciphers, certs, TLS config |
| `autocomplete` attribute | Out of scope |
| Host header injection | Out of scope unless you can demonstrate data theft |
| Insecure cookies | Only for non-sensitive cookies |
| Directory listing | Out of scope |
| Outdated browser issues | Out of scope |
| Verbose error messages | Out of scope unless you can chain to something |

### Rules of Engagement (Policy Guardrails)

- **Use test/non-production environments** when available — NASA specifically says "Test in test.gcn.nasa.gov NOT in gcn.nasa.gov"
- **No data exfiltration** — stop as soon as you confirm the vuln; do not dump data
- **No pivoting** — don't use exploits to reach other systems
- **Keep confidential** until fixed — disclose only after NASA resolves
- **Bugcrowd only** — `bugcrowd.com/engagements/nasa-vdp` is the sole submission channel
- **No compensation** — VDP only, no bounty; Letters of Recognition awarded for P1–P4 validated+fixed

### Letters of Recognition (LOR) Rules

- Awarded for P1–P4 only (validated, accepted, confirmed fixed)
- Duplicates and known issues do NOT qualify
- P5 / Informational = no LOR, ever

---

## PROGRAM STATS

| Metric | Count |
|---|---|
| Total accepted submissions | 914 |
| Disclosed (public) | 509 |
| P1 (Critical) | 146 (16%) |
| P2 (High) | 71 (8%) |
| P3 (Medium) | 233 (25%) |
| P4 (Low) | 200 (22%) |
| P5 (Informational) | 256 (28%) |

**Primary targets by acceptance volume:**
- `https://nasa.gov` — 727 (80% of all accepted — exhausted, avoid)
- `https://globe.gov/` — 67
- `https://scijinks.gov/` — 5
- `https://usgeo.gov/` — 2

---

## PRE-SUBMIT GATE (7 gates — all must pass)

### GATE 1: Scope & Triager Verifiability
- [ ] Asset is explicitly in scope (`*.nasa.gov`, `*.jpl.nasa.gov`, `*.gsfc.nasa.gov`, `globe.gov`, `usgeo.gov`, `scijinks.gov`, etc.)
- [ ] `auth.launchpad.nasa.gov` → **NEVER test, never submit**
- [ ] Triager can reproduce without your credentials?
- [ ] If account required: can triager self-register on that site?

### GATE 2: Not a Duplicate — Check These First

**PATCHED / HIGH-DUPLICATE-RISK endpoints (do NOT submit):**
| Endpoint | Finding | Priority | Status |
|---|---|---|---|
| `trek.nasa.gov/moon/TrekServices/ws/outreach/eq/addManifest` | SSRF internal network access | P2 | Resolved Aug 2026 |
| `massloading.smce.nasa.gov/cgi-bin/eop_series.py` | OS command injection RCE | P1 | Resolved Aug 2026 |
| `spaceplace.nasa.gov/api/experiment/answer/new/` | Error-based SQLi via POST param name | P1 | Resolved Aug 2026 |
| `cmr.earthdata.nasa.gov` (AQL parser) | XXE injection → SSRF | P1 | Resolved |
| `cmr.earthdata.nasa.gov` (Clojure) | RCE via unsafe deserialization | P1 | Resolved |
| `cmr.earthdata.nasa.gov` (CMR Ingest) | XXE injection | P1 | Resolved |
| `cmr.earthdata.nasa.gov` (shapefile.clj) | Zip slip arbitrary file write | P2 | Resolved |
| `gitlab.smce.nasa.gov` / `git.smce.nasa.gov` | Account takeover | P1 | Resolved |
| `satcorps.smce.nasa.gov` | Admin access | P1 | Resolved |
| `vizss.czdt.smce.nasa.gov` | Deserialization RCE (CVE-2025-55182) | P1 | Resolved |
| NASA AMMOS AIT-GUI `/tlm/query` → `/script/run` | RCE file write chain | P1 | Resolved |
| AIT-Core BSC Logger (POST) | Path traversal | P1 | Resolved |
| JPL Hurricane Watch | Unauth CRUD + email relay | P1 | Resolved Sep 2026 |
| `heasarc.gsfc.nasa.gov/cgi-bin/W3Browse/w3hdprods.pl` | Error-based SQLi | P1 | Resolved |
| MODAPS OKAPI (`//` double-slash) | Auth bypass via path normalization | P1 | Resolved |
| NASA OCSSW Matchup Tools | Command injection via filename | P1 | Resolved |
| `GetVectorFile.php` (unauthenticated) | Restricted file read | P1 | Resolved |
| NASA GSFC HPLC | RCE via insecure deserialization | P1 | Resolved |
| SAML bypass on `scijinks.gov`/`nesdis.noaa.gov` | Unauth admin takeover | P1 | Resolved |
| `photojournal.jpl.nasa.gov` | Blind SQLi | P1 | Resolved |
| PROSAMS `/api/retrieve-certs.php` | IDOR exposing full PII | P1/P2 | Resolved |
| WordPress `/wp-json/*` CORS (unauthenticated data) | CORS NR pattern | — | Rejected 3× |
| `trek.nasa.gov` Solr injection (LFI + SSRF variant) | Internal Solr → LFI/SSRF | **P1** | Resolved Mar 2026 |

⚠️ **TREK ALERT**: Trek Solr P1 (`item_UUID` field, LFI+SSRF variant) was patched March 2026 by YeJunWon. The `uuid=*` wildcard at `getLayerServices` was confirmed still live September 2026 (different impact: data dump only, not LFI). Our TREK-WADL-001 Solr component may face duplicate scrutiny — lead with the WADL internal hostname disclosure, not the Solr injection.

### GATE 3: Evidence Standard ("Demonstrated Risk")
| Finding type | What triager needs |
|---|---|
| CORS | Live fetch of victim's authenticated account data (PII/session) |
| SQLi | Error output or blind delay with payload in request+response |
| RCE | Command output in response — not theoretical |
| SSRF | OOB callback received OR internal host response body confirmed |
| IDOR | Two accounts: attacker reads/modifies victim's data |
| Auth bypass | Screenshot of accessing protected page/data without credentials |
| Exposed endpoint | Raw HTTP response showing sensitive data unauthenticated |

**"Could potentially" = instant kill.**

### GATE 4: VRT Accuracy
| What you found | Correct VRT path |
|---|---|
| CORS + credentialed data | `Server Security Misconfiguration > Unsafe Cross-Origin Resource Sharing` |
| Admin console accessible WITH NO AUTH (you can use it without logging in) | `Server Security Misconfiguration > Exposed Portal > Admin Portal` — P2 |
| Admin login page visible on internet (auth required) | **NOT a finding** — P5 at best, NR at NASA VDP |
| Non-admin API exposing internal data | `Server Security Misconfiguration > Exposed Portal > Non-Admin Portal` |
| WADL schema + internal hostname | `Server Security Misconfiguration > Exposed Portal > Non-Admin Portal` |
| OAuth missing state | `Server Security Misconfiguration > OAuth Misconfiguration > Missing/Broken State Parameter` |
| OAuth http:// redirect URI | `Server Security Misconfiguration > OAuth Misconfiguration > Insecure Redirect URI` |
| Version in headers | `Server Security Misconfiguration > Fingerprinting/Banner Disclosure > Software Versions Disclosed in Response Headers` — **P5, no reward** |
| Solr/NoSQL injection | `Injection > NoSQL Injection` |
| Error-based SQLi | `Injection > SQL Injection > Error Based` |
| DOM XSS | `Cross-Site Scripting (XSS) > DOM-Based` |
| Reflected XSS | `Cross-Site Scripting (XSS) > Reflected` |
| IDOR exposing PII | `Broken Access Control > IDOR > Sensitive Data Exposure` |
| Open redirect | `Server Security Misconfiguration > Unvalidated Redirect` |
| CSRF | `Broken Authentication and Session Management > CSRF` |

**Does NOT exist — never use:**
- `Lack of Security Controls`
- `Sensitive Admin Interface Exposed`
- `Authentication > OAuth` (top-level)
- `Insecure CORS Policy > Origin Reflection with Credentials`

### GATE 5: Acceptance Pattern

**P1 patterns (confirmed from CrowdStream):**
| Pattern | Example |
|---|---|
| Unauthenticated CRUD on production API | JPL Hurricane Watch |
| OS Command Injection in CGI | massloading eop_series.py |
| Error-based SQLi (unauthenticated) | spaceplace.nasa.gov, HEASARC W3Browse |
| Blind SQLi | photojournal.jpl.nasa.gov, `label` parameter |
| RCE via file write chain | AMMOS AIT-GUI |
| RCE via insecure deserialization | CMR (Clojure), GSFC HPLC, vizss Struts2 |
| RCE via path traversal + upload | AIT-Core BSC logger |
| Auth bypass via path normalization | MODAPS OKAPI `//` double slash |
| SAML auth bypass → admin takeover | scijinks.gov/nesdis.noaa.gov |
| GitLab/Git account takeover | gitlab.smce.nasa.gov |
| Command injection via filename | NASA OCSSW Matchup Tools |
| Unauthenticated file read (restricted) | GetVectorFile.php |
| CI/CD secret exfil via GitLab runner token | oguzhan_00 |
| XXE injection in CMR AQL parsing | CMR earthdata |
| IDOR exposing full PII (mass) | PROSAMS application users |
| Default credentials live in production | Teamwork Cloud |
| Leaked valid credentials (live, working) | EDRN Focus Biomarker Database |

**P2 patterns:**
| Pattern | Example |
|---|---|
| SSRF with confirmed internal host reachability | Trek addManifest |
| Unauthenticated dashboard (Flink, MMGIS webhooks) | LokeshTiwary, oversudo |
| Auth bypass — any password creates admin session | NASA SIPS |
| Zip slip arbitrary file write (unauth) | CMR earthdata |
| Exposed .svn metadata → file access | Mon3m |
| GraphQL exposing all groups/users (internal structure) | vinax |
| IDOR exposing PII (name/email/phone) | PROSAMS, mttc.jpl.nasa.gov |
| Stored XSS via file upload | anthonyjsaab |
| HTTP verb tampering → auth bypass | Mon3m |
| GoAccess logs exposed (JPL) | erh |

**P3 patterns:**
| Pattern | Example |
|---|---|
| DOM XSS (confirmed in browser) | Cesium Sandcastle |
| Admin config file with auth hashes | JulienZgh |
| Reflected XSS (NASA VPN portal, GSFC, JPL XSS) | Multiple |
| IDOR on users API (PII + internal hostnames) | ghaddarittoo |
| IDOR on team members API | SamSazzad |
| Broken function-level auth → funding manager PII | c3L0Mu1d3R |
| Public .env / .git / credential files | Multiple |
| Public Google Drive with write access linked from NASA | Multiple |
| External SMTP unauth email delivery to internal domain | sardarzabihunter |
| Publicly accessible admin pages (SWEHB) | Ozgun32 |
| ION-DTN integer overflow → heap buffer overflow | Excal1bur |
| SSRF in NASA Worldwind API | thomasito |
| Reflected DOM XSS in VOTable viewer | sriveros |
| RXSS on CGI endpoints (skyview, gsfc) | Multiple |
| Chained CSRF + XSS | Multiple |
| Login bypass → internal information disclosure | LokeshTiwary |
| Mass PII disclosure via headless API IDOR | Nicholas-K70n0s510-Mullenski |
| Public exposure of PII in internal XLSX/PDF files | Multiple |
| User creation in AWS Cognito (unauthenticated) | 1-day |
| NASA internal server exposed via IP | JustifyMe |

**P4 patterns:**
| Pattern | Example |
|---|---|
| Exposed non-admin portal (health/SBOM/schema) | Harmony SBOM, CMR health, NLSP sidemenu |
| Broken link hijacking (social media, YouTube) | muhammadabdillah64edc3, muhsyahrirhamdani |
| OAuth http:// redirect URI | Dagster AETC |
| SAML RelayState open redirect | 2yuk |
| Password reset token in HTTP (unencrypted) | edrn-labcas.jpl.nasa.gov |
| phpinfo() publicly accessible | MattKingst |
| Apache server-status endpoint exposed | Yonatan_Natanael_Tampi |
| Reflected XSS + HTML injection (cce-signin.gsfc.nasa.gov) | ItsS4LEH |
| Grafana CVE-2025-4123 open redirect | Gokuleshwaran_B |
| CSRF account deletion | wbossw |
| GoAccess logs (JPL subdomain) | erh |
| Publicly editable Google Slides linked from nasa.gov | Epenetus-Matias-Putra |
| Open redirect via SAML RelayState | 2yuk |
| Next.js build artifacts + config disclosure | Abuhuzaifa786 |
| Unauthenticated Grafana/metrics endpoint | whitebear_0one |
| Steal auth token via open redirect + XSS chain | aqibshah |

### GATE 6: Less-Visited Asset Priority

**Hunt here first (low competition, high acceptance):**
1. `*.smce.nasa.gov`, `*.sciencecloud.nasa.gov` — legacy CGI/Python scripts, `cgi-bin/`, old Tomcat
2. `*.jpl.nasa.gov` apps with REST APIs (JPL has many sub-apps with poor auth)
3. `trek.nasa.gov` remaining TrekServices endpoints (WADL-revealed, mostly untested)
4. `heasarc.gsfc.nasa.gov` — old CGI (`w3browse.pl`, `sia.pl` etc.) — Perl/Bash legacy
5. `earthdatacloud.nasa.gov` — newer platform, IDOR via CSRF found; OAuth chains
6. AMMOS tools (other instances of AIT, Aerie, MPSA — not all are patched)
7. `*.appdat.jsc.nasa.gov` — JSC apps with Keycloak/OAuth, staging exposed
8. NASA GitHub/GitLab public repos — leaked tokens, `.env`, SFTP credentials

**Avoid (saturated, duplicate rate >80%):**
- `www.nasa.gov` WordPress — exhausted
- `science.nasa.gov` WordPress — exhausted
- `earthdata.nasa.gov` main site — exhausted
- CORS on any WordPress `/wp-json/*` without authenticated victim demo

### GATE 7: 7-Question Gate
1. Can attacker do this RIGHT NOW with a single HTTP request? (No login required)
2. Does it cross a real security boundary?
3. What is the blast radius?
4. Is there real evidence in the HTTP response — not inferred?
5. Would triager reproduce this in 5 minutes?
6. Is VRT path correct and severity calibrated?
7. Has this pattern already been rejected at NASA VDP?

**NO to 1–5 or YES to 7 → kill the finding.**

---

## KNOWN REJECTIONS

| Pattern | Verdict | Rejection reason |
|---|---|---|
| CORS on WordPress REST API (unauthenticated data) | NR 5× (P1 submissions) | "Sensitive data must belong to victim's account"; triager cannot self-verify P1 impact without logged-in test account |
| CORS at P5 / informational framing | P5 informational (plus.nasa.gov — reproducible but no auth data shown) | Triager CAN reproduce headers; they just rate it P5 without demonstrated authenticated impact |
| CORS without authenticated victim data demo | NR | Triager cannot log in to verify |
| Theoretical chains without live proof | NR | "Demonstrated risk" standard |
| Subdomain takeover (no confirmed registration) | NR | Must show successful registration |
| Version string in headers alone | P5 | Zero reward |
| Self-XSS | N/A | Explicitly excluded from scope |
| Health status endpoints (Grafana /health, etc.) | NR | "Not inherently sensitive" |
| Keycloak admin console internet-accessible (login required) | P5 | Not "Exposed Admin Portal" — admin features require auth |
| Grafana login page internet-accessible (login required) | P5/NR | Same: login page ≠ admin access |
| Multiple exposed login portals bundled in one report | NR | "Health endpoints + version disclosure, not a vulnerability" |

### ⚠️ "EXPOSED ADMIN PORTAL" — Triager Definition (Sept 2026 clarification)

> **"We only apply the 'Exposed Admin Portal' VRT entry when the administrative features of the panel are accessible WITHOUT authentication."**
> — lmz_bugcrowd, Sep 2026

**What this means:**
- A Keycloak login page reachable on the internet = **NOT** an Exposed Admin Portal finding
- A Grafana login page reachable on the internet = **NOT** an Exposed Admin Portal finding
- "Exposed Admin Portal" = you can click past the login and access admin functions with NO credentials
- To submit under this VRT: must demonstrate bypassing auth (e.g., direct URL access, default creds, auth bypass)

**Rejected specifically as P5 (Sept 2026):**
- `auth.appdat.jsc.nasa.gov` — Keycloak login page
- `keycloak.luna.nasa.gov` — Keycloak login page  
- `idfs.earthdatacloud.nasa.gov` — Keycloak login page

**Rejected as NR (Sept 2026):**
- Luna platform (Grafana 13.1.3, Harbor, Dagster, ADAPT, Explorer) — health endpoints + login pages bundled
- `appdat.jsc.nasa.gov` Grafana — Grafana login page + version disclosure

**Path to escalate:** Try to bypass Keycloak auth (default creds, CVE, path manipulation). If you can access admin features without credentials, THEN it's a valid Exposed Admin Portal finding.

---

## ALL 509 DISCLOSED SUBMISSIONS (newest first)

### P1 Disclosures (recent — 2026)

| Title | Researcher | Accepted | URL |
|---|---|---|---|
| Unauthenticated Create, Read, and Delete of Any User's Data + Email Relay on JPL Hurricane Watch | Aman12321 | 19 Aug 2026 | https://bugcrowd.com/disclosures/eb823c31-5e78-4bf9-9b2a-4c339918e879/unauthenticated-create-read-and-delete-of-any-user-s-data-email-relay-on-jpl-hurricane-watch |
| Unauthenticated OS Command Injection (RCE) in NASA International Mass Loading Service CGI (massloading.smce.nasa.gov /cgi-bin/eop_series.py) | radithyaputra | 11 Aug 2026 | https://bugcrowd.com/disclosures/9fd428e5-c863-49d4-aea7-e91d2ba9199b/unauthenticated-os-command-injection-rce-in-nasa-international-mass-loading-service-cgi-massloading-smce-nasa-gov-cgi-bin-eop_series-py |
| Unauthenticated Error-Based SQL Injection via POST Parameter Name in /api/experiment/answer/new/ | iaramsri | 12 Aug 2026 | https://bugcrowd.com/disclosures/2b1df6dc-0ea2-42ee-a16a-9bbfc33e151a/unauthenticated-error-based-sql-injection-via-post-parameter-name-in-api-experiment-answer-new |
| Unauthenticated Remote Code Execution in NASA AMMOS AIT-GUI 2.5.0 via /tlm/query file write chained to /script/run code execution | ward0 | 16 Jul 2026 | https://bugcrowd.com/disclosures/e7ef226d-895b-4cfa-859a-59f83475ee60/unauthenticated-remote-code-execution-in-nasa-ammos-ait-gui-2-5-0-via-tlm-query-file-write-chained-to-script-run-code-execution |
| Unauthorized Access to CI/CD Infrastructure and Project Secrets via Compromised GitLab Runner Token | oguzhan_00 | 6 May 2026 | https://bugcrowd.com/disclosures/cc46ad29-f297-4847-abcd-9f5da5a85621/unauthorized-access-to-ci-cd-infrastructure-and-project-secrets-via-compromised-gitlab-runner-token |
| Blind SQL Injection in Search Functionality Leads to Full Database Extraction | molany | 2 Jul 2026 | https://bugcrowd.com/disclosures/4b4a2cd5-2fee-4407-b09f-74c14a8257df/blind-sql-injection-in-search-functionality-leads-to-full-database-extraction |
| Critical Authentication Bypass via Path Normalization (Double Slash) on Live NASA MODAPS OKAPI Production Instance | marcelojr | 6 Jul 2026 | https://bugcrowd.com/disclosures/c6b4ca39-0432-4180-995d-93ddec8ff614/critical-authentication-bypass-via-path-normalization-double-slash-on-live-nasa-modaps-okapi-production-instance |
| Command Injection via Unsanitized Filename in NASA OCSSW Matchup Tools | KaranKurani | 22 Jun 2026 | https://bugcrowd.com/disclosures/10cb4a9f-9173-4aca-9429-1b994a6233e6/command-injection-via-unsanitized-filename-in-nasa-ocssw-matchup-tools |
| Unauthenticated Restricted File Read and Out-of-Tree File Disclosure via GetVectorFile.php | freebird | 28 May 2026 | https://bugcrowd.com/disclosures/72e039d9-7e6c-4548-b1c3-4e278e573c6e/unauthenticated-restricted-file-read-and-out-of-tree-file-disclosure-via-getvectorfile-php |
| Remote Code Execution (RCE) via Insecure Deserialization in NASA GSFC HPLC Precision Analysis | kernely | 7 May 2026 | https://bugcrowd.com/disclosures/d9b460c2-f9b1-4f8d-a0ec-3236f702dacf/remote-code-execution-rce-via-insecure-deserialization-in-nasa-gsfc-hplc-precision-analysis |
| SAML Authentication Bypass Leading To Unauthenticated Admin Takeover on scijinks.gov / nesdis.noaa.gov | meeranh | 2 Mar 2026 | https://bugcrowd.com/disclosures/abfa03c7-9c7d-46f7-b255-9766199dac4a/saml-authentication-bypass-leading-to-unauthenticated-admin-takeover-on-scijinks-gov-nesdis-noaa-gov |
| Unauthenticated Remote Code Execution (RCE) via Unsafe Clojure Deserialization on cmr.earthdata.nasa.gov | obaskly | 23 Feb 2026 | https://bugcrowd.com/disclosures/948921ed-6603-4d2b-9022-f25f6552138f/unauthenticated-remote-code-execution-rce-via-unsafe-clojure-deserialization-on-cmr-earthdata-nasa-gov |
| XML External Entity (XXE) Injection via Regex Bypass in CMR AQL Parsing Enables SSRF, Service Enumeration and Blind File Reads | dewankpant | 5 Feb 2026 | https://bugcrowd.com/disclosures/9d2c7b28-7ff7-439c-9149-f74a883815e3/xml-external-entity-xxe-injection-via-regex-bypass-in-cmr-aql-parsing-enables-ssrf-service-enumeration-and-blind-file-reads |
| XML External Entity Injection in NASA CMR Ingest API - info dump | thomasito | 31 Oct 2025 | https://bugcrowd.com/disclosures/8c24664f-682e-43b6-83eb-885508405ac3/xml-external-entity-injection-in-nasa-cmr-ingest-api-info-dump |
| Internal Solr Query Injection enabling Local File Inclusion and Potential SSRF on trek.nasa.gov | YeJunWon | 2 Mar 2026 | https://bugcrowd.com/disclosures/ef50e1dd-1cc5-4c85-908d-cdc384a89bd3/internal-solr-query-injection-enabling-local-file-inclusion-and-potential-ssrf-on-trek-nasa-gov |
| Blind Boolean-Based SQL Injection in label Parameter Allows Unauthenticated Database Enumeration | martindios | 21 Apr 2026 | https://bugcrowd.com/disclosures/d854e13a-f8fb-47a1-bd86-93538c60f1c6/blind-boolean-based-sql-injection-in-label-parameter-allows-unauthenticated-database-enumeration |
| Path Traversal in AIT-Core BSC Logger via Unauthenticated POST Request | Excal1bur | 22 May 2026 | https://bugcrowd.com/disclosures/1614d1e0-56a7-4fab-bfc9-c6e1ca37e3ee/path-traversal-in-ait-core-bsc-logger-via-unauthenticated-post-request |
| Critical Admin Access Vulnerability on NASA's *.satcorps.smce.nasa.gov Subdomain | aashutoshdevkota | 24 Jun 2024 | https://bugcrowd.com/disclosures/b14596f7-3e6a-472b-9c0f-83996e53969a/critical-admin-access-vulnerability-on-nasa-s-satcorps-smce-nasa-gov-subdomain |
| SECURITY VULNERABILITY REPORT React2Shell CVE-2025-55182 | Dennisec_N00b | 8 Dec 2025 | https://bugcrowd.com/disclosures/e07fc7bd-9d1f-421e-978c-71c2802b2697/security-vulnerability-report-txt-version-react2shell-cve-2025-55182 |
| [CVE-2025-55182] Deserialization on vizss.czdt.smce.nasa.gov → RCE | R4XxH4 | 8 Dec 2025 | https://bugcrowd.com/disclosures/41e70d21-db93-463c-a80e-4ee03942a481/cve-2025-55182-deserialization-on-vizss-czdt-smce-nasa-gov-through-via-post-parameter-0-leads-to-remote-code-execution-rce |
| IDOR disclosing Username, Email, PIN, FirstName, LastName, UEI, FirmName, Address, PhoneNumbers of PROSAMS users | INUMA_CYBERSECURITY | 7 Nov 2025 | https://bugcrowd.com/disclosures/5c2ca864-dc69-43b1-bdd4-c61c81a08b09/idor-that-allows-disclosing-username-email-pin-firstname-lastname-uei-firmname-address-phonenumbers-etc-of-prosams-application-users |
| IDOR disclosing Username, Email, FirstName, LastName, Address, PhoneNumbers of PROSAMS users | INUMA_CYBERSECURITY | 30 Sep 2025 | https://bugcrowd.com/disclosures/68f4566e-2358-40c2-92d0-3a5e21023908/idor-that-allows-disclosing-username-email-firstname-lastname-address-phonenumbers-of-prosams-application-users |
| Authentication Bypass + exposure of PII + reflected XSS | snillx | 25 Jul 2025 | https://bugcrowd.com/disclosures/26e60aee-7c0d-4205-a531-9ef8742024ec/authentication-bypass-exposure-of-pii-reflected-xss |
| Unauthenticated Error-Based SQL Injection in HEASARC W3Browse w3hdprods.pl | Anon0x0 | 7 Jul 2026 | https://bugcrowd.com/disclosures/e0f7b8d5-b90a-4a50-b531-2da37e802c84/unauthenticated-error-based-sql-injection-in-heasarc-w3browse-w3hdprods-pl |
| Unauthorized Login Bypass & Malicious File Upload executed in NASA target system | AndreaAmaddio | 21 Mar 2025 | https://bugcrowd.com/disclosures/e31911c3-1c03-4808-94a6-ed7989b37259/unauthorized-login-bypass-malicious-file-upload-sent-delivered-and-executed-in-nasa-target-system |
| Leaked Valid Credentials for The EDRN Focus Biomarker Database (BMDB) | MiguelSantareno | 5 Feb 2024 | https://bugcrowd.com/disclosures/c3213329-654e-4b51-93ff-086c70215610/leaked-valid-credentials-for-the-edrn-focus-biomarker-database-bmdb |
| Blind SQL Injection at photojournal.jpl.nasa.gov | MiguelSegoviaGil | 26 Jan 2024 | https://bugcrowd.com/disclosures/e1e58b97-af59-49ae-acca-52bccab96e33/blind-sql-injection-at-photojournal-jpl-nasa-gov |
| Account takeover at https://gitlab.smce.nasa.gov/ | SaeidMicro | 26 Jan 2024 | https://bugcrowd.com/disclosures/13e938f6-9461-4280-9c11-3bd217d91cd9/account-take-over-at-https-gitlab-smce-nasa-gov |
| Account takeover at https://git.smce.nasa.gov | SaeidMicro | 17 Jan 2024 | https://bugcrowd.com/disclosures/8414f6bd-5eda-463a-86b3-7b855f749a42/account-take-over-at-https-git-smce-nasa-gov |
| PII Exposure in NASA NSSC Internal Procedure PDF | Daniyal_khan | 17 Feb 2026 | https://bugcrowd.com/disclosures/7c919b14-e9df-47a1-bae0-206f77c1379c/pii-exposure-in-nasa-nssc-internal-procedure-pdf |
| Default credentials for Teamwork Cloud | jpablo | 3 Oct 2025 | https://bugcrowd.com/disclosures/6cea28c5-b3a9-45a8-8617-826ba0649279/default-credentials-for-teamwork-cloud |
| Sensitive Data Exposure – Restricted NASA Document Publicly Accessible | sivasankardas | 11 Apr 2025 | https://bugcrowd.com/disclosures/b564c052-0e21-448e-9c38-0da86e3b9810/sensitive-data-exposure-restricted-nasa-document-publicly-accessible |

### P2 Disclosures (selected key ones)

| Title | Researcher | Accepted | URL |
|---|---|---|---|
| Unauthenticated SSRF in NASA Trek addManifest allows internal network access | n0RollBack | 28 May 2026 | https://bugcrowd.com/disclosures/652ddcf8-f52a-44f5-8a72-2e4a61f7c9ce/unauthenticated-ssrf-in-nasa-trek-addmanifest-allows-internal-network-access-from-the-trek-server |
| Unauthenticated Access to MMGIS Webhooks | oversudo | 26 Sep 2025 | https://bugcrowd.com/disclosures/c20138e9-28af-423f-a92b-0a2a1f85b3b2/unauthenticated-access-to-mmgis-webhooks |
| Authentication Bypass - Session Created for NASA SIPS Administrator Account with Any Password | IldevertDakouof | 19 Feb 2026 | https://bugcrowd.com/disclosures/ac8d1f0e-c0cf-4784-97b2-ba10e7b49da4/authentication-bypass-session-created-for-nasa-sips-administrator-account-with-any-password |
| Unauthenticated Arbitrary File Write (Zip Slip) via shapefile.clj on cmr.earthdata.nasa.gov | obaskly | 19 Mar 2026 | https://bugcrowd.com/disclosures/6f9e5cf2-23e8-474c-b402-7bf5ed0a8e52/unauthenticated-arbitrary-file-write-zip-slip-via-shapefile-clj-on-cmr-earthdata-nasa-gov |
| Unauthenticated Apache Flink Dashboard Access | LokeshTiwary | 10 Feb 2026 | https://bugcrowd.com/disclosures/caaf6992-f58f-46ce-8b34-cb256859804e/unauthenticated-apache-flink-dashboard-access |
| Source Code and Internal Infrastructure Disclosure via Publicly Exposed GitLab Repository on git.smce.nasa.gov | Franco_Andino | 16 Apr 2026 | https://bugcrowd.com/disclosures/b080842d-1a0c-4eaa-9c91-989a01c48a54/source-code-and-internal-infrastructure-disclosure-via-publicly-exposed-gitlab-repository-on-git-smce-nasa-gov |
| Stored Cross-Site Scripting (XSS) via Arbitrary File Upload | anthonyjsaab | 30 Jan 2026 | https://bugcrowd.com/disclosures/5c4a754b-c7b7-441f-b3db-89e1c82c78dc/stored-cross-site-scripting-xss-via-arbitrary-file-upload |
| SBN-Client Stack Buffer Overflow — recv_msg() and ingest_app_message() | Excal1bur | 22 Apr 2026 | https://bugcrowd.com/disclosures/757bcc0b-fe6e-4eb0-b914-1bbbf8a3f057/sbn-client-stack-buffer-overflow-recv_msg-and-ingest_app_message |
| Broken Access Control: Unauthenticated Mass Data Extraction and Arbitrary Item Deletion | Asier | 21 Apr 2026 | https://bugcrowd.com/disclosures/ba2df973-58fc-48be-9fb2-8205cca4e7c0/broken-access-control-unauthenticated-mass-data-extraction-and-arbitrary-item-deletion |
| Access to NASA Slack channel via Live Slack Invitation Link | Kartik_tantubai | 16 Jan 2025 | https://bugcrowd.com/disclosures/bd8f2801-752f-45d7-86cf-090471b3bd29/access-to-nasa-slack-channel-vai-live-slack-invitation-link-https-join-slack-com-t-nasa-ammos-shared_invite-zt-1mlgmk5c2-mgqvsykzvruwrxy87fnqpw |
| Exposed Emails and Names on https://mttc.jpl.nasa.gov/api/retrieve-certs.php | erh | 3 Oct 2025 | https://bugcrowd.com/disclosures/7eff8bb1-c894-4f2b-8f23-88593c987b95/exposed-emails-and-names-on-https-mttc-jpl-nasa-gov-api-retrieve-certs-php |
| Exposed .svn Metadata Leads to Information Disclosure and Unauthenticated File Access | Mon3m | 15 Aug 2025 | https://bugcrowd.com/disclosures/2b53813a-7264-46ed-9df9-ae2215c8353d/exposed-svn-metadata-leads-to-information-disclosure-and-unauthenticated-file-access |
| GraphQL API exposes all groups and group users leaking internal structure, full names and emails | vinax | 11 Jul 2025 | https://bugcrowd.com/disclosures/fe712f13-87e1-4a53-87bb-bdf360f1f962/graphql-api-exposes-all-groups-and-goups-users-leaking-internal-stucture-full-names-and-emails |
| HTTP Verb Tampering Leads to Authorization Bypass on /archive/exist/team/ Directory | Mon3m | 27 Jun 2025 | https://bugcrowd.com/disclosures/b5a435ec-c13c-4208-81f7-64431b1b7a4e/http-verb-tampering-leads-to-authorization-bypass-on-archive-exist-team-directory |
| IDOR disclosing Username, Email, PIN, address, phone (PROSAMS) | INUMA_CYBERSECURITY | 7 Nov 2025 | https://bugcrowd.com/disclosures/5c2ca864-dc69-43b1-bdd4-c61c81a08b09/idor-that-allows-disclosing-username-email-pin-firstname-lastname-uei-firmname-address-phonenumbers-etc-of-prosams-application-users |
| Editable internal Google Docs exposed via Google dork on eospso.nasa.gov | Kent_Shane14 | 17 Dec 2025 | https://bugcrowd.com/disclosures/d97ff466-3335-46fd-9503-d0648b211bac/editable-internal-google-docs-exposed-via-google-dork-on-eospso-nasa-gov |
| Stored XSS in Comment Field of Observation – Leads to Cookie Theft | GKData | 8 Aug 2025 | https://bugcrowd.com/disclosures/f2f4a65f-b225-4a0e-b018-104b8793ae5e/stored-xss-in-comment-field-of-observation-leads-to-cookie-theft-and-js-execution |

### P3 Disclosures (selected key ones)

| Title | Researcher | URL |
|---|---|---|
| DOM-based XSS through publicly exposed Cesium Sandcastle shared-code feature | iaramsri | https://bugcrowd.com/disclosures/6765826c-df24-47cd-afa4-c158bde0e4b6/dom-based-cross-site-scripting-through-the-publicly-exposed-cesium-sandcastle-shared-code-feature |
| Publicly Accessible Administrative Configuration File Exposes Auth Hashes and Internal Configuration | JulienZgh | https://bugcrowd.com/disclosures/e2794469-0dec-4c81-a5ca-916a663f35c5/publicly-accessible-administrative-configuration-file-exposes-authentication-hashes-and-internal-configuration |
| Reflected XSS in NASA JPL Solar System Simulator | cyb3rk1d | https://bugcrowd.com/disclosures/8c0c8259-00ab-4b82-a995-e59dd9efa53c/reflected-xss-in-nasa-jpl-solar-system-simulator |
| Reflected XSS in NASA VPN Portal | A0XTrojan | https://bugcrowd.com/disclosures/1fa25156-f094-40f8-8569-028f9518d4aa/reflected-xss-in-nasa-vpn-portal |
| IDOR / Broken Access Control: /users/{id} exposes other users' PII and password hash | p3iv2 | https://bugcrowd.com/disclosures/fdb0f70d-1cb2-4709-ad64-78f078d8e2be/idor-broken-access-control-users-id-exposes-other-users-pii-and-password-hash-password_ |
| Unauthenticated IDOR on Users API leading to Information Disclosure of Internal Hostnames and PII | ghaddarittoo | https://bugcrowd.com/disclosures/713064c8-35c7-41ac-b6b3-443c1c9daeaa/unauthenticated-idor-on-users-api-leading-to-information-disclosure-of-internal-hostnames-and-pii |
| RXSS & HTML Injection in cdn.earthdata.nasa.gov via Docson viewer | jesssuwu | https://bugcrowd.com/disclosures/193a57e6-91cb-480c-850f-1a149419e881/rxss-html-injection-in-cdn-earthdata-nasa-gov-via-docson-viewer-enabling-phishing-attacks |
| Broken Function-Level Authorization: Standard Users Access Internal Funding Manager PII | c3L0Mu1d3R | https://bugcrowd.com/disclosures/003aefd2-dd3a-41a2-9e3a-448ba90403d1/broken-function-level-authorization-allows-standard-users-to-access-internal-funding-manager-pii-via-project-funding-api |
| External SMTP submission allows unauthenticated email delivery to internal NASA domain | sardarzabihunter | https://bugcrowd.com/disclosures/350eedae-27d6-4d94-a1aa-bec8fc480c69/external-smtp-submission-allows-unauthenticated-email-delivery-to-internal-nasa-domain-recipients-with-potential-for-spoofed-sender-identity-display |
| Internal Scan through SSRF in NASA Worldwind API | thomasito | https://bugcrowd.com/disclosures/6296825c-7c02-4771-80d8-9d1496331981/internal-scan-through-ssrf-in-nasa-worldwind-api |
| Reflected DOM XSS in VOTable Viewer leads to authenticated ARK user PII exfiltration | sriveros | https://bugcrowd.com/disclosures/00cb5011-6768-4b68-a4a2-6b48a9ae35b3/reflected-dom-xss-in-votable-viewer-leads-to-authenticated-ark-user-pii-exfiltration-via-same-origin-xhr |
| IDOR in Team Members API Exposes Private Emails and Roles of Any Team | SamSazzad | https://bugcrowd.com/disclosures/1e63488a-ca15-4ed4-99f3-c0298c72a638/idor-in-team-members-api-exposes-private-emails-and-roles-of-any-team |
| Integer Overflow to Heap Buffer Overflow in NASA ION-DTN startImportSession | Excal1bur | https://bugcrowd.com/disclosures/e083d54b-793b-4d3f-a50d-7a0d3f13d551/integer-overflow-to-heap-buffer-overflow-in-nasa-ion-dtn-startimportsession-libltpp-c-5781 |
| Bypassing restrictions to load Jupyter Notebook ipynb from orgs other than NASA | mateuszek | https://bugcrowd.com/disclosures/8c0bef28-3ae4-40f8-ab4c-5446255ffa2c/bypassing-the-restrictions-to-load-the-jupyter-notebook-ipynb-from-organizations-other-than-nasa-on-https-lb-gesdisc-eosdis-nasa-gov-meditor |
| Publicly accessible NASA internal server (WFF-NENS-WEB1) exposed via IP 128.154.105.100 | JustifyMe | https://bugcrowd.com/disclosures/ed9e7789-f064-4736-80fe-e7a1109eb03c/publicly-accessible-nasa-internal-server-wff-nens-web1-exposed-via-ip-128-154-105-100 |
| Mass PII Disclosure (Emails/Phones) via IDOR on Headless API | Nicholas-K70n0s510-Mullenski | https://bugcrowd.com/disclosures/ab0208c1-df67-47ac-a671-990ce55996d8/mass-pii-disclosure-emails-phones-via-insecure-direct-object-reference-idor-on-headless-api |
| Unauthenticated Access to NASA SWEHB Admin Pages | Ozgun32 | https://bugcrowd.com/disclosures/f425b701-318e-4fd6-ba9e-4710130a8ca7/unauthenticated-access-to-nasa-swehb-admin-pages |
| Login bypass leads to internal information disclosure | LokeshTiwary | https://bugcrowd.com/disclosures/ff4614f2-3260-4653-ab10-16fccbb6bb58/login-bypass-leads-to-internal-information-disclosure |
| Unauthenticated user creation in AWS Cognito user Pool | 1-day | https://bugcrowd.com/disclosures/cbe0edab-82a9-46ae-9ed3-f3a0b30d1cca/unauthenticated-user-creation-in-aws-cognito-user-pool |
| RXSS at https://skyview.gsfc.nasa.gov/current/cgi/vo/sia.pl | GxbNt | https://bugcrowd.com/disclosures/2534d5fe-6a7e-48bb-9117-ce357cfa0c9f/rxss-at-https-skyview-gsfc-nasa-gov-current-cgi-vo-sia-pl |
| Exposed Credentials in Public .env File on NASA Git Repository | Hunt3rboy | https://bugcrowd.com/disclosures/a9ba7ee3-bb0e-4945-9834-34171056a680/exposed-credentials-in-public-env-file-on-nasa-git-repository |

### P4 Disclosures (selected key ones)

| Title | Researcher | URL |
|---|---|---|
| Impersonation via Broken Link Hijacking on NASA Earth Matters Blog Page | muhammadabdillah64edc3 | https://bugcrowd.com/disclosures/081a696d-d1d2-4d7d-acb7-29b313c9aa9b/impersonation-via-broken-link-hijacking-on-nasa-earth-matters-blog-page |
| Arbitrary External Redirect Through SAML RelayState After Successful Authentication | 2yuk | https://bugcrowd.com/disclosures/a1363cea-d7c2-4e36-901d-cc25f0123c26/arbitrary-external-redirect-through-saml-relaystate-after-successful-authentication |
| Password Reset Token Exposed via Unencrypted HTTP - edrn-labcas.jpl.nasa.gov | 0xdk27 | https://bugcrowd.com/disclosures/59c5a5c1-33e1-465b-9b20-6344d614dcbb/password-reset-token-exposed-via-unencrypted-http-edrn-labcas-jpl-nasa-gov |
| Reflected XSS and HTML Injection on cce-signin.gsfc.nasa.gov via popup_flag parameter | ItsS4LEH | https://bugcrowd.com/disclosures/7773707b-09b0-46ec-9891-682546e02434/reflected-xss-and-html-injection-on-cce-signin-gsfc-nasa-gov-via-popup_flag-parameter |
| Public Apache Server Status Endpoint Causes Sensitive Data Exposure | Yonatan_Natanael_Tampi | https://bugcrowd.com/disclosures/7c9313ff-516f-4f8f-820f-eb693843f2b2/public-apache-server-status-endpoint-causes-sensitive-data-exposure-of-internal-system-information |
| Publicly accessible phpinfo() exposes detailed server configuration | MattKingst | https://bugcrowd.com/disclosures/41e4cef6-b0bf-4a9c-9a5d-9a34747ad7c4/publicly-accessible-phpinfo-exposes-detailed-server-configuration |
| Unauthenticated Metrics Endpoint Exposes Sensitive Internal Grafana & NASA Infrastructure Data | whitebear_0one | https://bugcrowd.com/disclosures/a2dbc42c-f4e5-4af4-97e0-0ce9c49f14be/unauthenticated-metrics-endpoint-exposes-sensitive-internal-grafana-nasa-infrastructure-data |
| Exposed Next.js Build Artifacts & Sensitive Configuration Disclosure | Abuhuzaifa786 | https://bugcrowd.com/disclosures/62588ff6-5ae0-444c-9b3b-bd40339c2033/exposed-next-js-build-artifacts-sensitive-configuration-disclosure |
| Internal Proprietary Financial Report (AEPR) for internal use, publicly accessible | Wiz-Zero | https://bugcrowd.com/disclosures/1570570b-5149-493d-b6e3-1a162794ce78/internal-proprietary-financial-report-aepr-for-internal-use-publicly-accessible |
| NASA NLSP API discloses internal usernames and system role mappings to unauthenticated users | c3L0Mu1d3R | https://bugcrowd.com/disclosures/87458826-6d92-4102-ad25-2d697efeea30/nasa-nlsp-api-discloses-internal-usernames-and-system-role-mappings-to-unauthenticated-users |
| Broken YouTube Link enables Channel Impersonation (@DarkEnergyExplorers) | muhsyahrirhamdani | https://bugcrowd.com/disclosures/30a99b17-c10c-4afd-86b2-ed2a2c843e3f/broken-youtube-link-on-nasa-citizen-science-page-enables-potential-channel-impersonation-darkenergyexplorers |
| Critical CSRF Vulnerability Exploiting Account Deletion on NASA Subscription Service | wbossw | https://bugcrowd.com/disclosures/e97add76-3838-4d24-a86a-ae850003ad15/critical-csrf-vulnerability-exploiting-account-deletion-on-nasa-subscription-service |
| Unauthorized access to goto.jpl.nasa.gov | erh | https://bugcrowd.com/disclosures/c13f5fb6-b31d-4420-b878-4ef12bb60eba/unauthorized-access-to-goto-jpl.nasa.gov |
| Unauthorised Access to GoAccess Logs on https://mwsci.jpl.nasa.gov | erh | https://bugcrowd.com/disclosures/23d4bb50-16b4-4667-a538-e6a502c9277e/unauthorised-access-to-goaccess-logs-on-https-mwsci-jpl-nasa-gov |
| Open Redirect via displayFile parameter on lmse.larc.nasa.gov | Rootk1d-- | https://bugcrowd.com/disclosures/7aa47bd3-0d9b-4ff0-bad0-6082c10b7858/open-redirect-via-displayfile-parameter-on-lmse-larc-nasa-gov |
| Session Hijacking via Reusable JSESSIONID Exposes OAuth Token and Profile Data | Lalit24__ | https://bugcrowd.com/disclosures/553cc72a-72b5-4217-8b72-7c4a32ceffed/critical-session-hijacking-via-reusable-jsessionid-exposes-oauth-token-and-profile-data |

---

## LESSONS LEARNED

### CORS (5× NR at P1 — confirmed pattern 2026-09-09)

**Never submit CORS at P1 or P2 without a live, self-contained authenticated exfiltration PoC the triager can verify themselves.**

**Root cause:** Confirmed from 5 `not_reproducible` closures (www.nasa.gov, science.nasa.gov, oig.nasa.gov, nasa.gov ×2 — all P1) vs. 1 `informational P5` (plus.nasa.gov). The triager CAN reproduce CORS headers — they proved it on plus.nasa.gov → P5. The NR verdict on the others is NOT a CDN/geo issue. At P1, the triager must confirm authenticated data theft end-to-end, and they cannot do this without a logged-in test account on NASA WordPress VIP sites. Submitting curl header output alone is insufficient for P1 impact verification.

| Scenario | What to do | Expected verdict |
|---|---|---|
| CORS with curl-only PoC (headers only) | Submit at P3; never P1 | P5 informational |
| CORS with live ngrok/interactsh PoC showing auth data received | Submit at P2; include screenshot of attacker receiving victim's authenticated data + instruction "Log into [site] before visiting PoC" | P2–P3 possible |
| CORS on site with public registration (e.g. NASA+) | Include triager test account steps; still expect P4–P5 unless you demo account-specific data | P4–P5 |
| CORS on WordPress VIP (www/science/oig/nccs — no public signups) | Accept P5 ceiling; only escalate if you record video of your own authenticated session data being exfiltrated | P5 informational |

**Never submit CORS on WordPress REST API (`/wp-json/*`) endpoints returning only public/unauthenticated data.** Triager standard verbatim: "sensitive data must belong to the victim's account and not be publicly accessible."

### CVE Claims — Never Claim a CVE Without Firing It Against the Live Target (Critical lesson — phpBB N/A)

**Rule:** Never name a CVE in a submission unless you have confirmed it applies to this specific target by actually running the PoC against the live endpoint and capturing the result.

**What happened:** phpBB CVE-2023-42498 was submitted for `forum.earthdata.nasa.gov`. CVE-2023-42498 is a **Liferay Portal** CVE — it has nothing to do with phpBB. The submission contained false claims and exaggerations. NASA triager escalated to the NASA security team (the only submission that made it to NASA directly), and NASA confirmed not applicable. Submission marked `not_applicable`.

**Why:** Rule 22 in hunting.md is explicit: "A CVE database hit... does not confirm the bug exists on this target. Treat it as `tentative` until the PoC actually runs against the live target." The phpBB submission applied a CVE for a different product entirely.

**How to apply:**
- Search CVE → find a match → this is a LEAD, not a finding
- Fire the PoC against the live target → capture the HTTP response proving exploitation → THEN write a report
- If the PoC fails to reproduce, kill the lead and move on
- Never claim a CVE number without confirmed exploitation evidence on the specific target
- A wrong CVE claim = false claims = account flag risk + wastes NASA security team time

### Trek Solr (P1 already accepted)
YeJunWon accepted P1 (Solr LFI+SSRF) March 2026. Patched but `getLayerServices?uuid=*` wildcard still returns 11,440 records Sept 2026. If submitting Trek Solr: differentiate from the LFI/SSRF pattern; focus on wildcard enumeration. Lead with the WADL hostname disclosure instead.

### Saturated targets
`nasa.gov`, `www.nasa.gov`, `science.nasa.gov` — 80% of all submissions go here. Duplicate rate is >95%. Focus on smce/sciencecloud/jpl/appdat.jsc subdomains.

### Version disclosure alone
Never submit a standalone Tomcat/Jersey/jQuery version header finding. P5 informational with zero reward. Bundle it into a larger finding (as in TREK-WADL-001) where the primary issue is a functional vulnerability.

### Evidence standard
NASA VDP triager applies "demonstrated risk." If you can't show the actual HTTP response proving the impact, the finding will be closed as "not demonstrated."

### Exposed Portal ≠ login page visible (critical — 5 NR/P5 in Sept 2026)
Five reports rejected in one batch for the same reason: treating internet-accessible login pages (Keycloak, Grafana) as "Exposed Admin Portal" findings. The triager is explicit: "Exposed Admin Portal" VRT applies ONLY when admin features are accessible WITHOUT authentication. A login page being visible is not the finding — bypassing that login is the finding. Next time: attempt auth bypass first (default creds, Keycloak CVEs, path traversal), then submit only if you can access admin functions without credentials.

### Health endpoints + login pages bundled = NR
Bundling multiple "login page accessible" items + health endpoints in one report still gets NR. Each item is individually non-qualifying. The triager won't approve a bundle of weak findings.

### Admin console VRT — correct vs wrong
| Scenario | VRT | Priority |
|---|---|---|
| Admin panel accessible WITH authentication only | Not a finding — login page being public is normal | — |
| Admin panel accessible WITHOUT auth (you can use it) | `server_security_misconfiguration.exposed_portal.admin_portal` | P2 |
| Non-admin API returning data without auth | `server_security_misconfiguration.exposed_portal.non-admin_portal` | P3–P4 |
| Keycloak/Grafana login page visible, auth required | P5 at best, likely NR | P5/NR |

---

*Source: Bugcrowd CrowdStream JSON API — all 46 pages scraped 2026-09-02*
*Researcher handles, URLs, and vulnerability data reproduced verbatim from public disclosures*
