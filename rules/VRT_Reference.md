# Bugcrowd VRT Reference — Web Security

**VRT Release Date:** 2026-07-08
**Source:** github.com/bugcrowd/vulnerability-rating-taxonomy
**Purpose:** Cross-check VRT path + priority before every Bugcrowd submission

---

## How to Use

1. Find `Category > Subcategory > Variant` that matches your finding
2. Copy the exact dotted ID (e.g. `broken_access_control.idor.read`) into the VRT field
3. Confirm the listed **priority matches your claimed severity** — triagers adjust down, not up
4. Between two variants: pick the lower priority (conservative)
5. "Software version disclosure" without working PoC = always P5 (no reward at NASA VDP)

---

## Common NASA VDP Submission Mistakes

| Wrong claim | Correct VRT | Priority |
|---|---|---|
| "CORS misconfiguration" (unauthenticated data only) | `server_security_misconfiguration.unsafe_cross-origin_resource_sharing_cors` | P4–P5, often NR at NASA |
| "Information disclosure" (version header, no PoC) | `sensitive_data_exposure.disclosure_of_secrets.software_version_disclosure` | P5, no reward |
| "SQLi" (Solr wildcard only, not standard SQL) | `server_side_injection.nosql_injection` | P3–P4 |
| IDOR on public/non-sensitive data | `broken_access_control.idor.read_-_sensitive_non_iterable` | P4 |
| WADL schema disclosure | `server_security_misconfiguration.exposed_portal.non-admin_portal` | P4 |
| Host header injection (no data theft shown) | Out-of-scope per NASA VDP policy | Rejected |

---

## Broken Access Control (BAC)
`broken_access_control`

### Bypass of Password Confirmation
`broken_access_control.bypass_of_password_confirmation`

- **P4 Low** — `broken_access_control.bypass_of_password_confirmation.change_password` — Change Password

### Exposed Sensitive Android Intent
`broken_access_control.exposed_sensitive_android_intent`


### Exposed Sensitive iOS URL Scheme
`broken_access_control.exposed_sensitive_ios_url_scheme`


### Insecure Direct Object References (IDOR)
`broken_access_control.idor`

- **P2 High** — `broken_access_control.idor.modify_sensitive_information_iterable_object_identifiers` — Modify Sensitive Information(Iterable Object Identifiers)
- **P4 Low** — `broken_access_control.idor.modify_view_sensitive_information_guid` — Modify/View Sensitive Information(Complex Object Identifiers GUID/UUID)
- **P1 Critical** — `broken_access_control.idor.modify_view_sensitive_information_iterable_object_identifiers` — Modify/View Sensitive Information(Iterable Object Identifiers)
- **P5 Informational** — `broken_access_control.idor.view_non_sensitive_information` — View Non-Sensitive Information
- **P3 Medium** — `broken_access_control.idor.view_sensitive_information_iterable_object_identifiers` — View Sensitive Information(Iterable Object Identifiers)

### Privilege Escalation
`broken_access_control.privilege_escalation`


### Username/Email Enumeration
`broken_access_control.username_enumeration`

- **P4 Low** — `broken_access_control.username_enumeration.non_brute_force` — Non-Brute Force

---

## Broken Authentication and Session Management
`broken_authentication_and_session_management`

### Authentication Bypass
`broken_authentication_and_session_management.authentication_bypass`

**Priority: P1 Critical**

### Cleartext Transmission of Session Token
`broken_authentication_and_session_management.cleartext_transmission_of_session_token`

**Priority: P4 Low**

### Concurrent Logins
`broken_authentication_and_session_management.concurrent_logins`

**Priority: P5 Informational**

### Failure to Invalidate Session
`broken_authentication_and_session_management.failure_to_invalidate_session`

- **P5 Informational** — `broken_authentication_and_session_management.failure_to_invalidate_session.all_sessions` — Concurrent Sessions On Logout
- **P5 Informational** — `broken_authentication_and_session_management.failure_to_invalidate_session.long_timeout` — Long Timeout
- **P5 Informational** — `broken_authentication_and_session_management.failure_to_invalidate_session.on_email_change` — On Email Change
- **P4 Low** — `broken_authentication_and_session_management.failure_to_invalidate_session.on_logout` — On Logout (Client and Server-Side)
- **P5 Informational** — `broken_authentication_and_session_management.failure_to_invalidate_session.on_logout_server_side_only` — On Logout (Server-Side Only)
- **P4 Low** — `broken_authentication_and_session_management.failure_to_invalidate_session.on_password_change` — On Password Reset and/or Change
- **P5 Informational** — `broken_authentication_and_session_management.failure_to_invalidate_session.on_two_fa_activation_change` — On 2FA Activation/Change
- **—** — `broken_authentication_and_session_management.failure_to_invalidate_session.permission_change` — On Permission Change

### SAML Replay
`broken_authentication_and_session_management.saml_replay`

**Priority: P5 Informational**

### Session Fixation
`broken_authentication_and_session_management.session_fixation`

- **P5 Informational** — `broken_authentication_and_session_management.session_fixation.local_attack_vector` — Local Attack Vector
- **P3 Medium** — `broken_authentication_and_session_management.session_fixation.remote_attack_vector` — Remote Attack Vector

### Second Factor Authentication (2FA) Bypass
`broken_authentication_and_session_management.two_fa_bypass`

**Priority: P3 Medium**

### Weak Login Function
`broken_authentication_and_session_management.weak_login_function`

- **P5 Informational** — `broken_authentication_and_session_management.weak_login_function.not_operational` — Not Operational or Intended Public Access
- **P4 Low** — `broken_authentication_and_session_management.weak_login_function.other_plaintext_protocol_no_secure_alternative` — Other Plaintext Protocol with no Secure Alternative
- **P4 Low** — `broken_authentication_and_session_management.weak_login_function.over_http` — Over HTTP

### Weak Registration Implementation
`broken_authentication_and_session_management.weak_registration_implementation`

- **P4 Low** — `broken_authentication_and_session_management.weak_registration_implementation.over_http` — Over HTTP

### Excessive JSON Web Token (JWT) Lifetime
`broken_authentication_and_session_management.excessive_jwt_lifetime`

**Priority: P5 Informational**

### Secret Questions Used for Account Verification
`broken_authentication_and_session_management.secret_questions_account_verification`

**Priority: P5 Informational**

---

## Client-Side Injection
`client_side_injection`

### Binary Planting
`client_side_injection.binary_planting`

- **P5 Informational** — `client_side_injection.binary_planting.no_privilege_escalation` — No Privilege Escalation
- **P5 Informational** — `client_side_injection.binary_planting.non_default_folder_privilege_escalation` — Non-Default Folder Privilege Escalation
- **P3 Medium** — `client_side_injection.binary_planting.privilege_escalation` — Default Folder Privilege Escalation

---

## Cross-Site Request Forgery (CSRF)
`cross_site_request_forgery_csrf`

### Action-Specific
`cross_site_request_forgery_csrf.action_specific`

- **—** — `cross_site_request_forgery_csrf.action_specific.authenticated_action` — Authenticated Action
- **P5 Informational** — `cross_site_request_forgery_csrf.action_specific.logout` — Logout
- **—** — `cross_site_request_forgery_csrf.action_specific.unauthenticated_action` — Unauthenticated Action

### Application-Wide
`cross_site_request_forgery_csrf.application_wide`

**Priority: P2 High**

### CSRF Token Not Unique Per Request
`cross_site_request_forgery_csrf.csrf_token_not_unique_per_request`

**Priority: P5 Informational**

### Flash-Based
`cross_site_request_forgery_csrf.flash_based`

**Priority: P5 Informational**

---

## Cross-Site Scripting (XSS)
`cross_site_scripting_xss`

### Cookie-Based
`cross_site_scripting_xss.cookie_based`

**Priority: P5 Informational**

### Flash-Based
`cross_site_scripting_xss.flash_based`

**Priority: P5 Informational**

### IE-Only
`cross_site_scripting_xss.ie_only`

**Priority: P5 Informational**

### Off-Domain
`cross_site_scripting_xss.off_domain`

- **P4 Low** — `cross_site_scripting_xss.off_domain.data_uri` — Data URI

### Referer
`cross_site_scripting_xss.referer`

**Priority: P4 Low**

### Reflected
`cross_site_scripting_xss.reflected`

- **P3 Medium** — `cross_site_scripting_xss.reflected.non_self` — Non-Self
- **P5 Informational** — `cross_site_scripting_xss.reflected.self` — Self

### Stored
`cross_site_scripting_xss.stored`

- **P2 High** — `cross_site_scripting_xss.stored.non_admin_to_anyone` — Non-Privileged User to Anyone
- **P4 Low** — `cross_site_scripting_xss.stored.privileged_user_to_no_privilege_elevation` — Privileged User to No Privilege Elevation
- **P3 Medium** — `cross_site_scripting_xss.stored.privileged_user_to_privilege_elevation` — Privileged User to Privilege Elevation
- **P5 Informational** — `cross_site_scripting_xss.stored.self` — Self
- **P3 Medium** — `cross_site_scripting_xss.stored.url_based` — CSRF/URL-Based

### TRACE Method
`cross_site_scripting_xss.trace_method`

**Priority: P5 Informational**

### Universal (UXSS)
`cross_site_scripting_xss.universal_uxss`

**Priority: P4 Low**

---

## Cryptographic Weakness
`cryptographic_weakness`

### Broken Cryptography
`cryptographic_weakness.broken_cryptography`

- **P3 Medium** — `cryptographic_weakness.broken_cryptography.use_of_broken_cryptographic_primitive` — Use of Broken Cryptographic Primitive
- **P4 Low** — `cryptographic_weakness.broken_cryptography.use_of_vulnerable_cryptographic_library` — Use of Vulnerable Cryptographic Library

### Incomplete Cleanup of Keying Material
`cryptographic_weakness.incomplete_cleanup_of_keying_material`

**Priority: P5 Informational**

### Insecure Implementation
`cryptographic_weakness.insecure_implementation`

- **—** — `cryptographic_weakness.insecure_implementation.improper_following_of_specification` — Improper Following of Specification (Other)
- **—** — `cryptographic_weakness.insecure_implementation.missing_cryptographic_step` — Missing Cryptographic Step

### Insecure Key Generation
`cryptographic_weakness.insecure_key_generation`

- **—** — `cryptographic_weakness.insecure_key_generation.improper_asymmetric_exponent_selection` — Improper Asymmetric Exponent Selection
- **—** — `cryptographic_weakness.insecure_key_generation.improper_asymmetric_prime_selection` — Improper Asymmetric Prime Selection
- **P3 Medium** — `cryptographic_weakness.insecure_key_generation.insufficient_key_space` — Insufficient Key Space
- **—** — `cryptographic_weakness.insecure_key_generation.insufficient_key_stretching` — Insufficient Key Stretching
- **P4 Low** — `cryptographic_weakness.insecure_key_generation.key_exchange_without_entity_authentication` — Key Exchage Without Entity Authentication

### Insufficient Entropy
`cryptographic_weakness.insufficient_entropy`

- **P5 Informational** — `cryptographic_weakness.insufficient_entropy.initialization_vector_reuse` — Initialization Vector (IV) Reuse
- **P4 Low** — `cryptographic_weakness.insufficient_entropy.limited_rng_entropy_source` — Limited Random Number Generator (RNG) Entropy Source
- **P4 Low** — `cryptographic_weakness.insufficient_entropy.predictable_initialization_vector` — Predictable Initialization Vector (IV)
- **P4 Low** — `cryptographic_weakness.insufficient_entropy.predictable_prng_seed` — Predictable Pseudo-Random Number Generator (PRNG) Seed
- **P5 Informational** — `cryptographic_weakness.insufficient_entropy.prng_seed_reuse` — Pseudo-Random Number Generator (PRNG) Seed Reuse
- **P4 Low** — `cryptographic_weakness.insufficient_entropy.small_seed_space_in_prng` — Small Seed Space in Pseudo-Random Number Generator (PRNG)
- **P5 Informational** — `cryptographic_weakness.insufficient_entropy.use_of_trng_for_nonsecurity_purpose` — Use of True Random Number Generator (TRNG) for Non-Security Purpose

### Insufficient Verification of Data Authenticity
`cryptographic_weakness.insufficient_verification_of_data_authenticity`

- **—** — `cryptographic_weakness.insufficient_verification_of_data_authenticity.cryptographic_signature` — Cryptographic Signature
- **P4 Low** — `cryptographic_weakness.insufficient_verification_of_data_authenticity.identity_check_value` — Integrity Check Value (ICV)

### Key Reuse
`cryptographic_weakness.key_reuse`

- **P2 High** — `cryptographic_weakness.key_reuse.inter_environment` — Inter-Environment
- **P5 Informational** — `cryptographic_weakness.key_reuse.intra_environment` — Intra-Environment
- **P4 Low** — `cryptographic_weakness.key_reuse.lack_of_perfect_forward_secrecy` — Lack of Perfect Forward Secrecy

### Side-Channel Attack
`cryptographic_weakness.side_channel_attack`

- **—** — `cryptographic_weakness.side_channel_attack.differential_fault_analysis` — Differential Fault Analysis
- **P5 Informational** — `cryptographic_weakness.side_channel_attack.emanations_attack` — Emanations Attack
- **P4 Low** — `cryptographic_weakness.side_channel_attack.padding_oracle_attack` — Padding Oracle Attack
- **P5 Informational** — `cryptographic_weakness.side_channel_attack.power_analysis_attack` — Power Analysis Attack
- **P4 Low** — `cryptographic_weakness.side_channel_attack.timing_attack` — Timing Attack

### Use of Expired Cryptographic Key (or Certificate)
`cryptographic_weakness.use_of_expired_cryptographic_key_or_cert`

**Priority: P4 Low**

### Weak Hash
`cryptographic_weakness.weak_hash`

- **—** — `cryptographic_weakness.weak_hash.lack_of_salt` — Lack of Salt
- **—** — `cryptographic_weakness.weak_hash.predictable_hash_collision` — Predictable Hash Collision
- **P5 Informational** — `cryptographic_weakness.weak_hash.use_of_predictable_salt` — Use of Predictable Salt

---

## Insecure Data Storage
`insecure_data_storage`

### Non-Sensitive Application Data Stored Unencrypted
`insecure_data_storage.non_sensitive_application_data_stored_unencrypted`

**Priority: P5 Informational**

### Screen Caching Enabled
`insecure_data_storage.screen_caching_enabled`

**Priority: P5 Informational**

### Sensitive Application Data Stored Unencrypted
`insecure_data_storage.sensitive_application_data_stored_unencrypted`

- **P4 Low** — `insecure_data_storage.sensitive_application_data_stored_unencrypted.on_external_storage` — On External Storage
- **P5 Informational** — `insecure_data_storage.sensitive_application_data_stored_unencrypted.on_internal_storage` — On Internal Storage

### Server-Side Credentials Storage
`insecure_data_storage.server_side_credentials_storage`

- **P4 Low** — `insecure_data_storage.server_side_credentials_storage.plaintext` — Plaintext

---

## Insecure Data Transport
`insecure_data_transport`

### Cleartext Transmission of Sensitive Data
`insecure_data_transport.cleartext_transmission_of_sensitive_data`


### Executable Download
`insecure_data_transport.executable_download`

- **P4 Low** — `insecure_data_transport.executable_download.no_secure_integrity_check` — No Secure Integrity Check
- **P5 Informational** — `insecure_data_transport.executable_download.secure_integrity_check` — Secure Integrity Check

---

## Sensitive Data Exposure
`sensitive_data_exposure`

### Disclosure of Known Public Information
`sensitive_data_exposure.disclosure_of_known_public_information`

**Priority: P5 Informational**

### Disclosure of Secrets
`sensitive_data_exposure.disclosure_of_secrets`

- **P5 Informational** — `sensitive_data_exposure.disclosure_of_secrets.data_traffic_spam` — Data/Traffic Spam
- **P3 Medium** — `sensitive_data_exposure.disclosure_of_secrets.for_internal_asset` — For Internal Asset
- **P1 Critical** — `sensitive_data_exposure.disclosure_of_secrets.for_publicly_accessible_asset` — For Publicly Accessible Asset
- **P5 Informational** — `sensitive_data_exposure.disclosure_of_secrets.intentionally_public_sample_or_invalid` — Intentionally Public, Sample or Invalid
- **P5 Informational** — `sensitive_data_exposure.disclosure_of_secrets.non_corporate_user` — Non-Corporate User
- **P4 Low** — `sensitive_data_exposure.disclosure_of_secrets.pay_per_use_abuse` — Pay-Per-Use Abuse
- **—** — `sensitive_data_exposure.disclosure_of_secrets.pii_leakage_exposure` — PII Leakage/Exposure
- **P5 Informational** — `sensitive_data_exposure.disclosure_of_secrets.sensitive_information_disclosed_jwt` — Sensitive Information Disclosed in JSON Web Token (JWT)
- **P5 Informational** — `sensitive_data_exposure.disclosure_of_secrets.publicly_accessible_robots` — Publicly accessible Robots.txt

### EXIF Geolocation Data Not Stripped From Uploaded Images
`sensitive_data_exposure.exif_geolocation_data_not_stripped_from_uploaded_images`

- **P3 Medium** — `sensitive_data_exposure.exif_geolocation_data_not_stripped_from_uploaded_images.automatic_user_enumeration` — Automatic User Enumeration
- **P4 Low** — `sensitive_data_exposure.exif_geolocation_data_not_stripped_from_uploaded_images.manual_user_enumeration` — Manual User Enumeration

### GraphQL Introspection Enabled
`sensitive_data_exposure.graphql_introspection_enabled`

**Priority: P5 Informational**

### Internal IP Disclosure
`sensitive_data_exposure.internal_ip_disclosure`

**Priority: P5 Informational**

### JSON Hijacking
`sensitive_data_exposure.json_hijacking`

**Priority: P5 Informational**

### Mixed Content (HTTPS Sourcing HTTP)
`sensitive_data_exposure.mixed_content`

**Priority: P5 Informational**

### Non-Sensitive Token in URL
`sensitive_data_exposure.non_sensitive_token_in_url`

**Priority: P5 Informational**

### Sensitive Data Hardcoded
`sensitive_data_exposure.sensitive_data_hardcoded`

- **P5 Informational** — `sensitive_data_exposure.sensitive_data_hardcoded.file_paths` — File Paths
- **P5 Informational** — `sensitive_data_exposure.sensitive_data_hardcoded.oauth_secret` — OAuth Secret

### Sensitive Token in URL
`sensitive_data_exposure.sensitive_token_in_url`

- **P5 Informational** — `sensitive_data_exposure.sensitive_token_in_url.in_the_background` — In the Background
- **P5 Informational** — `sensitive_data_exposure.sensitive_token_in_url.on_password_reset` — On Password Reset
- **P4 Low** — `sensitive_data_exposure.sensitive_token_in_url.user_facing` — User Facing

### Token Leakage via Referer
`sensitive_data_exposure.token_leakage_via_referer`

- **P4 Low** — `sensitive_data_exposure.token_leakage_via_referer.over_http` — Over HTTP
- **P5 Informational** — `sensitive_data_exposure.token_leakage_via_referer.password_reset_token` — Password Reset Token
- **P5 Informational** — `sensitive_data_exposure.token_leakage_via_referer.trusted_third_party` — Trusted 3rd Party
- **P4 Low** — `sensitive_data_exposure.token_leakage_via_referer.untrusted_third_party` — Untrusted 3rd Party

### Via localStorage/sessionStorage
`sensitive_data_exposure.via_localstorage_sessionstorage`

- **P5 Informational** — `sensitive_data_exposure.via_localstorage_sessionstorage.non_sensitive_token` — Non-Sensitive Token
- **P4 Low** — `sensitive_data_exposure.via_localstorage_sessionstorage.sensitive_token` — Sensitive Token

### Visible Detailed Error/Debug Page
`sensitive_data_exposure.visible_detailed_error_page`

- **P5 Informational** — `sensitive_data_exposure.visible_detailed_error_page.descriptive_stack_trace` — Descriptive Stack Trace
- **P4 Low** — `sensitive_data_exposure.visible_detailed_error_page.detailed_server_configuration` — Detailed Server Configuration
- **P5 Informational** — `sensitive_data_exposure.visible_detailed_error_page.full_path_disclosure` — Full Path Disclosure

### Weak Password Reset Implementation
`sensitive_data_exposure.weak_password_reset_implementation`

- **P4 Low** — `sensitive_data_exposure.weak_password_reset_implementation.password_reset_token_sent_over_http` — Password Reset Token Sent Over HTTP
- **P2 High** — `sensitive_data_exposure.weak_password_reset_implementation.token_leakage_via_host_header_poisoning` — Token Leakage via Host Header Poisoning

### Cross Site Script Inclusion (XSSI)
`sensitive_data_exposure.xssi`


---

## Server Security Misconfiguration
`server_security_misconfiguration`

### Bitsquatting
`server_security_misconfiguration.bitsquatting`

**Priority: P5 Informational**

### Cache Deception
`server_security_misconfiguration.cache_deception`


### Cache Poisoning
`server_security_misconfiguration.cache_poisoning`


### CAPTCHA
`server_security_misconfiguration.captcha`

- **P5 Informational** — `server_security_misconfiguration.captcha.brute_force` — Brute Force
- **P4 Low** — `server_security_misconfiguration.captcha.implementation_vulnerability` — Implementation Vulnerability
- **P5 Informational** — `server_security_misconfiguration.captcha.missing` — Missing

### Clickjacking
`server_security_misconfiguration.clickjacking`

- **P5 Informational** — `server_security_misconfiguration.clickjacking.form_input` — Form Input
- **P5 Informational** — `server_security_misconfiguration.clickjacking.non_sensitive_action` — Non-Sensitive Action
- **P4 Low** — `server_security_misconfiguration.clickjacking.sensitive_action` — Sensitive Click-Based Action

### Cookie Scoped to Parent Domain
`server_security_misconfiguration.cookie_scoped_to_parent_domain`

**Priority: P5 Informational**

### Database Management System (DBMS) Misconfiguration
`server_security_misconfiguration.dbms_misconfiguration`

- **P4 Low** — `server_security_misconfiguration.dbms_misconfiguration.excessively_privileged_user_dba` — Excessively Privileged User / DBA

### Directory Listing Enabled
`server_security_misconfiguration.directory_listing_enabled`

- **P5 Informational** — `server_security_misconfiguration.directory_listing_enabled.non_sensitive_data_exposure` — Non-Sensitive Data Exposure
- **—** — `server_security_misconfiguration.directory_listing_enabled.sensitive_data_exposure` — Sensitive Data Exposure

### Email Verification Bypass
`server_security_misconfiguration.email_verification_bypass`

**Priority: P5 Informational**

### Exposed Portal
`server_security_misconfiguration.exposed_portal`

- **P1 Critical** — `server_security_misconfiguration.exposed_portal.admin_portal` — Admin Portal
- **P3 Medium** — `server_security_misconfiguration.exposed_portal.non_admin_portal` — Non-Admin Portal
- **P5 Informational** — `server_security_misconfiguration.exposed_portal.protected` — Protected

> ⚠️ **NASA VDP TRIAGER DEFINITION (confirmed Sep 2026, 5 rejections):**
> - `admin_portal` (P1) = admin features accessible **WITHOUT authentication** — you can use the admin UI without any credentials
> - `non_admin_portal` (P3) = non-admin portal accessible without authentication
> - `protected` (P5) = portal is visible but **requires authentication** — a Keycloak/Grafana/Kibana login page on the internet falls here
> - A login page being publicly reachable = `protected` P5 at best, NR at NASA VDP
> - To qualify for `admin_portal`: demonstrate bypassing auth (default creds, auth bypass CVE, path traversal)

### Fingerprinting/Banner Disclosure
`server_security_misconfiguration.fingerprinting_banner_disclosure`

- **P5 Informational** — `server_security_misconfiguration.fingerprinting_banner_disclosure.software_version_in_response_headers` — Software Versions Disclosed in Response Headers

### Insecure SSL
`server_security_misconfiguration.insecure_ssl`

- **P5 Informational** — `server_security_misconfiguration.insecure_ssl.certificate_error` — Certificate Error
- **P5 Informational** — `server_security_misconfiguration.insecure_ssl.insecure_cipher_suite` — Insecure Cipher Suite
- **P5 Informational** — `server_security_misconfiguration.insecure_ssl.lack_of_forward_secrecy` — Lack of Forward Secrecy

### Lack of Password Confirmation
`server_security_misconfiguration.lack_of_password_confirmation`

- **P5 Informational** — `server_security_misconfiguration.lack_of_password_confirmation.change_email_address` — Change Email Address
- **P5 Informational** — `server_security_misconfiguration.lack_of_password_confirmation.change_password` — Change Password
- **P4 Low** — `server_security_misconfiguration.lack_of_password_confirmation.delete_account` — Delete Account
- **P5 Informational** — `server_security_misconfiguration.lack_of_password_confirmation.manage_two_fa` — Manage 2FA

### Lack of Security Headers
`server_security_misconfiguration.lack_of_security_headers`

- **P5 Informational** — `server_security_misconfiguration.lack_of_security_headers.cache_control_for_a_non_sensitive_page` — Cache-Control for a Non-Sensitive Page
- **P4 Low** — `server_security_misconfiguration.lack_of_security_headers.cache_control_for_a_sensitive_page` — Cache-Control for a Sensitive Page
- **P5 Informational** — `server_security_misconfiguration.lack_of_security_headers.content_security_policy` — Content-Security-Policy
- **P5 Informational** — `server_security_misconfiguration.lack_of_security_headers.content_security_policy_report_only` — Content-Security-Policy-Report-Only
- **P5 Informational** — `server_security_misconfiguration.lack_of_security_headers.public_key_pins` — Public-Key-Pins
- **P5 Informational** — `server_security_misconfiguration.lack_of_security_headers.strict_transport_security` — Strict-Transport-Security
- **P5 Informational** — `server_security_misconfiguration.lack_of_security_headers.x_content_security_policy` — X-Content-Security-Policy
- **P5 Informational** — `server_security_misconfiguration.lack_of_security_headers.x_content_type_options` — X-Content-Type-Options
- **P5 Informational** — `server_security_misconfiguration.lack_of_security_headers.x_frame_options` — X-Frame-Options
- **P5 Informational** — `server_security_misconfiguration.lack_of_security_headers.x_webkit_csp` — X-Webkit-CSP
- **P5 Informational** — `server_security_misconfiguration.lack_of_security_headers.x_xss_protection` — X-XSS-Protection

### Mail Server Misconfiguration
`server_security_misconfiguration.mail_server_misconfiguration`

- **P5 Informational** — `server_security_misconfiguration.mail_server_misconfiguration.email_spoofing_on_non_email_domain` — Email Spoofing on Non-Email Domain
- **P4 Low** — `server_security_misconfiguration.mail_server_misconfiguration.email_spoofing_to_inbox_due_to_missing_or_misconfigured_dmarc_on_email_domain` — Email Spoofing to Inbox due to Missing or Misconfigured DMARC on Email Domain
- **P5 Informational** — `server_security_misconfiguration.mail_server_misconfiguration.email_spoofing_to_spam_folder` — Email Spoofing to Spam Folder
- **P5 Informational** — `server_security_misconfiguration.mail_server_misconfiguration.missing_or_misconfigured_spf_and_or_dkim` — Missing or Misconfigured SPF and/or DKIM
- **P3 Medium** — `server_security_misconfiguration.mail_server_misconfiguration.no_spoofing_protection_on_email_domain` — No Spoofing Protection on Email Domain

### Misconfigured DNS
`server_security_misconfiguration.misconfigured_dns`

- **P5 Informational** — `server_security_misconfiguration.misconfigured_dns.missing_caa_record` — Missing Certification Authority Authorization (CAA) Record
- **P3 Medium** — `server_security_misconfiguration.misconfigured_dns.subdomain_takeover` — Subdomain Takeover
- **P4 Low** — `server_security_misconfiguration.misconfigured_dns.zone_transfer` — Zone Transfer

### Missing DNSSEC
`server_security_misconfiguration.missing_dnssec`

**Priority: P5 Informational**

### Missing Secure or HTTPOnly Cookie Flag
`server_security_misconfiguration.missing_secure_or_httponly_cookie_flag`

- **P5 Informational** — `server_security_misconfiguration.missing_secure_or_httponly_cookie_flag.non_session_cookie` — Non-Session Cookie
- **P4 Low** — `server_security_misconfiguration.missing_secure_or_httponly_cookie_flag.session_token` — Session Token

### Missing Subresource Integrity
`server_security_misconfiguration.missing_subresource_integrity`

**Priority: P5 Informational**

### No Rate Limiting on Form
`server_security_misconfiguration.no_rate_limiting_on_form`

- **P5 Informational** — `server_security_misconfiguration.no_rate_limiting_on_form.change_password` — Change Password
- **P4 Low** — `server_security_misconfiguration.no_rate_limiting_on_form.email_triggering` — Email-Triggering
- **P4 Low** — `server_security_misconfiguration.no_rate_limiting_on_form.login` — Login
- **P4 Low** — `server_security_misconfiguration.no_rate_limiting_on_form.registration` — Registration
- **P4 Low** — `server_security_misconfiguration.no_rate_limiting_on_form.sms_triggering` — SMS-Triggering

### OAuth Misconfiguration
`server_security_misconfiguration.oauth_misconfiguration`

- **P4 Low** — `server_security_misconfiguration.oauth_misconfiguration.account_squatting` — Account Squatting
- **P2 High** — `server_security_misconfiguration.oauth_misconfiguration.account_takeover` — Account Takeover
- **—** — `server_security_misconfiguration.oauth_misconfiguration.insecure_redirect_uri` — Insecure Redirect URI
- **—** — `server_security_misconfiguration.oauth_misconfiguration.missing_state_parameter` — Missing/Broken State Parameter

### Path Traversal
`server_security_misconfiguration.path_traversal`


### Potentially Unsafe HTTP Method Enabled
`server_security_misconfiguration.potentially_unsafe_http_method_enabled`

- **P5 Informational** — `server_security_misconfiguration.potentially_unsafe_http_method_enabled.options` — OPTIONS
- **P5 Informational** — `server_security_misconfiguration.potentially_unsafe_http_method_enabled.trace` — TRACE

### Race Condition
`server_security_misconfiguration.race_condition`


### HTTP Request Smuggling
`server_security_misconfiguration.request_smuggling`


### Reflected File Download (RFD)
`server_security_misconfiguration.rfd`

**Priority: P5 Informational**

### Same-Site Scripting
`server_security_misconfiguration.same_site_scripting`

**Priority: P5 Informational**

### Server-Side Request Forgery (SSRF)
`server_security_misconfiguration.server_side_request_forgery_ssrf`

- **P5 Informational** — `server_security_misconfiguration.server_side_request_forgery_ssrf.external_dns_query_only` — External - DNS Query Only
- **P5 Informational** — `server_security_misconfiguration.server_side_request_forgery_ssrf.external_low_impact` — External - Low impact
- **P2 High** — `server_security_misconfiguration.server_side_request_forgery_ssrf.internal_secrets_exposure` — Internal Secrets Exposure
- **P3 Medium** — `server_security_misconfiguration.server_side_request_forgery_ssrf.internal_data_exposure` — Internal Data Exposure
- **P3 Medium** — `server_security_misconfiguration.server_side_request_forgery_ssrf.internal_port_service_scan` — Internal Port Service Scan
- **P4 Low** — `server_security_misconfiguration.server_side_request_forgery_ssrf.internal_exposure_presence_data_secrets` — Internal Exposure of the Presence of Data/Secrets
- **P4 Low** — `server_security_misconfiguration.server_side_request_forgery_ssrf.internal_port_scan_only` — Internal Port Scan Only

### Software Package Takeover
`server_security_misconfiguration.software_package_takeover`


### SSL Attack (BREACH, POODLE etc.)
`server_security_misconfiguration.ssl_attack_breach_poodle_etc`


### Unsafe Cross-Origin Resource Sharing
`server_security_misconfiguration.unsafe_cross_origin_resource_sharing`


### Unsafe File Upload
`server_security_misconfiguration.unsafe_file_upload`

- **P5 Informational** — `server_security_misconfiguration.unsafe_file_upload.file_extension_filter_bypass` — File Extension Filter Bypass
- **P5 Informational** — `server_security_misconfiguration.unsafe_file_upload.no_antivirus` — No Antivirus
- **P5 Informational** — `server_security_misconfiguration.unsafe_file_upload.no_size_limit` — No Size Limit

### Username/Email Enumeration
`server_security_misconfiguration.username_enumeration`

- **P5 Informational** — `server_security_misconfiguration.username_enumeration.brute_force` — Brute Force

### Using Default Credentials
`server_security_misconfiguration.using_default_credentials`

**Priority: P1 Critical**

### Web Application Firewall (WAF) Bypass
`server_security_misconfiguration.waf_bypass`

- **P4 Low** — `server_security_misconfiguration.waf_bypass.direct_server_access` — Direct Server Access

### Misconfigured File Share
`server_security_misconfiguration.misconfigured_file_share`

- **—** — `server_security_misconfiguration.misconfigured_file_share.anonymous_ftp_enabled` — Anonymous FTP Enabled
- **—** — `server_security_misconfiguration.misconfigured_file_share.anonymous_smb_enabled` — Anonymous SMB Enabled
- **P5 Informational** — `server_security_misconfiguration.misconfigured_file_share.non_sensitive_data_exposure_ftp_smb` — Non-Sensitive Data Exposure via Anonymous FTP/SMB Enabled

### Misconfigured Security Headers 
`server_security_misconfiguration.misconfigured_security_headers`

- **P5 Informational** — `server_security_misconfiguration.misconfigured_security_headers.insecure_csp` — Insecure Content-Security-Policy

---

## Server-Side Injection
`server_side_injection`

### Content Spoofing
`server_side_injection.content_spoofing`

- **P4 Low** — `server_side_injection.content_spoofing.email_html_injection` — Email HTML Injection
- **P5 Informational** — `server_side_injection.content_spoofing.email_hyperlink_injection_based_on_email_provider` — Email Hyperlink Injection Based on Email Provider
- **P4 Low** — `server_side_injection.content_spoofing.external_authentication_injection` — External Authentication Injection
- **P5 Informational** — `server_side_injection.content_spoofing.flash_based_external_authentication_injection` — Flash Based External Authentication Injection
- **P5 Informational** — `server_side_injection.content_spoofing.homograph_idn_based` — Homograph/IDN-Based
- **P5 Informational** — `server_side_injection.content_spoofing.html_content_injection` — HTML Content Injection
- **P3 Medium** — `server_side_injection.content_spoofing.iframe_injection` — iframe Injection
- **P4 Low** — `server_side_injection.content_spoofing.impersonation_via_broken_link_hijacking` — Impersonation via Broken Link Hijacking
- **P5 Informational** — `server_side_injection.content_spoofing.rtlo` — Right-to-Left Override (RTLO)
- **P5 Informational** — `server_side_injection.content_spoofing.text_injection` — Text Injection
- **P5 Informational** — `server_side_injection.content_spoofing.self_email_html_injection` — Self Email HTML Injection

### Exposed Data
`server_side_injection.exposed_data`

- **P5 Informational** — `server_side_injection.exposed_data.non_sensitive_data` — Non Sensitive Data
- **—** — `server_side_injection.exposed_data.sensitive_data` — Sensitive Data

### File Inclusion
`server_side_injection.file_inclusion`

- **P1 Critical** — `server_side_injection.file_inclusion.local` — Local

### HTTP Response Manipulation
`server_side_injection.http_response_manipulation`

- **P3 Medium** — `server_side_injection.http_response_manipulation.response_splitting_crlf` — Response Splitting (CRLF)

### LDAP Injection
`server_side_injection.ldap_injection`


### Parameter Pollution
`server_side_injection.parameter_pollution`

- **P5 Informational** — `server_side_injection.parameter_pollution.social_media_sharing_buttons` — Social Media Sharing Buttons

### Remote Code Execution (RCE)
`server_side_injection.remote_code_execution_rce`

**Priority: P1 Critical**

### SQL Injection
`server_side_injection.sql_injection`

**Priority: P1 Critical**

### Server-Side Template Injection (SSTI)
`server_side_injection.ssti`

- **P4 Low** — `server_side_injection.ssti.basic` — Basic
- **—** — `server_side_injection.ssti.custom` — Custom

### XML External Entity Injection (XXE)
`server_side_injection.xml_external_entity_injection_xxe`

**Priority: P1 Critical**

---

## Unvalidated Redirects and Forwards
`unvalidated_redirects_and_forwards`

### Lack of Security Speed Bump Page
`unvalidated_redirects_and_forwards.lack_of_security_speed_bump_page`

**Priority: P5 Informational**

### Open Redirect
`unvalidated_redirects_and_forwards.open_redirect`

- **P5 Informational** — `unvalidated_redirects_and_forwards.open_redirect.flash_based` — Flash-Based
- **P4 Low** — `unvalidated_redirects_and_forwards.open_redirect.get_based` — GET-Based
- **P5 Informational** — `unvalidated_redirects_and_forwards.open_redirect.header_based` — Header-Based
- **P5 Informational** — `unvalidated_redirects_and_forwards.open_redirect.post_based` — POST-Based

### Tabnabbing
`unvalidated_redirects_and_forwards.tabnabbing`

**Priority: P5 Informational**

---

## Using Components with Known Vulnerabilities
`using_components_with_known_vulnerabilities`

### Captcha Bypass
`using_components_with_known_vulnerabilities.captcha_bypass`

- **P5 Informational** — `using_components_with_known_vulnerabilities.captcha_bypass.ocr_optical_character_recognition` — OCR (Optical Character Recognition)

### Outdated Software Version
`using_components_with_known_vulnerabilities.outdated_software_version`

**Priority: P5 Informational**

### Rosetta Flash
`using_components_with_known_vulnerabilities.rosetta_flash`

**Priority: P5 Informational**

### Unpatched Javascript Libraries
`using_components_with_known_vulnerabilities.unpatched_javascript_libraries`

**Priority: P5 Informational**

---

## AI Application Security
`ai_application_security`

### Adversarial Example Injection
`ai_application_security.adversarial_example_injection`

- **P4 Low** — `ai_application_security.adversarial_example_injection.ai_misclassification_attacks` — AI Misclassification Attacks

### AI Safety
`ai_application_security.ai_safety`

- **P4 Low** — `ai_application_security.ai_safety.misinformation_wrong_factual_data` — Misinformation / Wrong Factual Data

### Denial-of-Service (DoS)
`ai_application_security.denial_of_service_dos`

- **P2 High** — `ai_application_security.denial_of_service_dos.application_wide` — Application-Wide
- **P4 Low** — `ai_application_security.denial_of_service_dos.tenant_scoped` — Tenant-Scoped

### Improper Input Handling
`ai_application_security.improper_input_handling`

- **P5 Informational** — `ai_application_security.improper_input_handling.ansi_escape_codes` — ANSI Escape Codes
- **P5 Informational** — `ai_application_security.improper_input_handling.rtl_overrides` — RTL Overrides
- **P5 Informational** — `ai_application_security.improper_input_handling.unicode_confusables` — Unicode Confusables

### Improper Output Handling
`ai_application_security.improper_output_handling`

- **P3 Medium** — `ai_application_security.improper_output_handling.cross_site_scripting_xss` — Cross-Site Scripting (XSS)
- **P4 Low** — `ai_application_security.improper_output_handling.markdown_html_injection` — Markdown/HTML Injection

### Insufficient Rate Limiting
`ai_application_security.insufficient_rate_limiting`

- **P4 Low** — `ai_application_security.insufficient_rate_limiting.query_flooding_api_token_abuse` — Query Flooding / API Token Abuse

### Model Extraction
`ai_application_security.model_extraction`

- **P1 Critical** — `ai_application_security.model_extraction.api_query_based_model_reconstruction` — API Query-Based Model Reconstruction

### Prompt Injection
`ai_application_security.prompt_injection`

- **P2 High** — `ai_application_security.prompt_injection.system_prompt_leakage` — System Prompt Leakage

### Remote Code Execution
`ai_application_security.remote_code_execution`

- **P1 Critical** — `ai_application_security.remote_code_execution.full_system_compromise` — Full System Compromise
- **P2 High** — `ai_application_security.remote_code_execution.sandboxed_container_code_execution` — Sandboxed Container Code Execution

### Sensitive Information Disclosure
`ai_application_security.sensitive_information_disclosure`

- **P1 Critical** — `ai_application_security.sensitive_information_disclosure.cross_tenant_pii_leakage_exposure` — Cross-Tenant PII Leakage/Exposure
- **P1 Critical** — `ai_application_security.sensitive_information_disclosure.key_leak` — Key Leak

### Training Data Poisoning
`ai_application_security.training_data_poisoning`

- **P1 Critical** — `ai_application_security.training_data_poisoning.backdoor_injection_bias_manipulation` — Backdoor Injection / Bias Manipulation

### Vector and Embedding Weaknesses
`ai_application_security.vector_and_embedding_weaknesses`

- **P2 High** — `ai_application_security.vector_and_embedding_weaknesses.embedding_exfiltration_model_extraction` — Embedding Exfiltration / Model Extraction
- **P3 Medium** — `ai_application_security.vector_and_embedding_weaknesses.semantic_indexing` — Semantic Indexing

---

## Cloud Security
`cloud_security`

### Identity and Access Management (IAM) Misconfigurations
`cloud_security.identity_and_access_management_iam_misconfigurations`

- **P2 High** — `cloud_security.identity_and_access_management_iam_misconfigurations.overly_permissive_iam_roles` — Overly Permissive IAM Roles
- **P1 Critical** — `cloud_security.identity_and_access_management_iam_misconfigurations.publicly_accessible_iam_credentials` — Publicly Accessible IAM Credentials

### Logging and Monitoring Issues
`cloud_security.logging_and_monitoring_issues`

- **P5 Informational** — `cloud_security.logging_and_monitoring_issues.disabled_or_insufficient_logging` — Disabled or Insufficient Logging

### Misconfigured Services and APIs
`cloud_security.misconfigured_services_and_apis`

- **—** — `cloud_security.misconfigured_services_and_apis.exposed_debug_or_admin_interfaces` — Exposed Debug or Admin Interfaces
- **P4 Low** — `cloud_security.misconfigured_services_and_apis.insecure_api_endpoints` — Insecure API Endpoints

### Network Configuration Issues
`cloud_security.network_configuration_issues`

- **P3 Medium** — `cloud_security.network_configuration_issues.lack_of_network_segmentation` — Lack of Network Segmentation
- **P3 Medium** — `cloud_security.network_configuration_issues.open_management_ports_to_the_internet` — Open Management Ports to the Internet

### Storage Misconfigurations
`cloud_security.storage_misconfigurations`

- **—** — `cloud_security.storage_misconfigurations.publicly_accessible_cloud_storage` — Publicly Accessible Cloud Storage
- **P2 High** — `cloud_security.storage_misconfigurations.unencrypted_sensitive_data_at_rest` — Unencrypted Sensitive Data at Rest

---
