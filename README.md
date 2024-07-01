# Overview

This repository hosts GDHCN trustlists as DIDs.
The trustlist documents and specification is published via GitHub pages.


## Trustlist Specification 2.0.0

| Status | Description                                                 |
| ------ |-------------------------------------------------------------|
| Draft  | 2.0.0 is in prereleased state for verification and feedback |

Disclaimer: Only the version in the production environment is stable and authoritative for use.

The specification of trustlists in version 2.0.0 introduces two versions of the trust lists - embedded and by reference.  
The root/main trust list contains all keys available on the TNG (either embedded or by reference).  

The trustlist documents should be reachable with the Following URLs:

https://tng-cdn.who.int/v2.0.0/trustlist/did.json
https://tng-cdn.who.int/v2.0.0/trustlist-ref/did.json

### Path Structure

The following path structure is applied to support more fine grained resolution of key material:

* tng-cdn.who.int/v2.0.0/trustlist/<DOMAIN>/<PARTICIPANT_CODE> matches all key usages (DSC, SCA, etc) for a specific domain or participant code
* tng-cdn.who.int/v2.0.0/trustlist/<DOMAIN>/<PARTICIPANT_CODE>/<USAGE> matches all keys for a specific usage for a specific domain or participant code
* tng-cdn.who.int//v2.0.0/trustlist/-/<PARTICIPANT_CODE> matches all domains for a specific participant for all usage codes
* tng-cdn.who.int//v2.0.0/trustlist/-/<PARTICIPANT_CODE>/<USAGE> matches all domains for a specific participant and usage code
* tng-cdn.who.int//v2.0.0/trustlist/<DOMAIN>/-/<USAGE> matches all participants for a specific domain

Note that "-" character is used as a wildcard.

### Folder Structure

Repository Folder structure (under a version folder):

* trustlist
  * did.json contains all keys embedded
    * DDCC
      * did.json contains all keys for DDCC domain embedded
      * FRA
        * did.json contains all keys for France for DDCC Domain embedded
        * DSC
          * did.json contains DSCs for France for DDCC Domain
        * SCA
          * did.json contains DSCs for France for DDCC Domain
      * IND
        * did.json contains all keys for Indonesia for DDCC Domain
        * IPS
          * did.json contains all keys for IPS domain embedded
          * FRA
            * did.json contains all keys for France for IPS Domain embedded
            * DSC
              * did.json contains DSCs for France for IPS Domain
            * SCA
              * did.json contains DSCs for France for IPS Domain
    * "-"
      * FRA
        * did.json contains all keys for France for all domains embedded
      * IND
        * did.json contains all keys for Indonesia for all domain embedded

* trustlist-ref
  * contains all keys by reference
    * ...same structure as above...


## Trustlist Specification 1.0.0


| Status     | Description                                         |
|------------|-----------------------------------------------------|
| Deprecated | 1.0.0 is deprecated and superseded by version 2.0.0 |