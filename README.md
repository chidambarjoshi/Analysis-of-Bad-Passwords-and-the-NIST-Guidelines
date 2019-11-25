1.	Project Title

The project “Analysis of Bad Passwords and the NIST Guidelines” provides technical guidelines to agencies for the implementation of digital authentication.
2.	Introduction

Almost every web service you join will require you to come up with a password. But what makes a good password? In June 2017 the National Institute of Standards and Technology (NIST) published publication 800-63B titled “Digital Identity Guidelines: Authentication and Lifecycle Management”. This publication doesn't tell you what is a good password, but it does have specific rules for what is a bad password.
In this project, you will take a list of user passwords and, using publication 800-63B, you will write code that automatically detects and flags the bad passwords.

3.	Literature Survey

Digital identity is the unique representation of a subject engaged in an online transaction. A digital identity is always unique in the context of a digital service, but does not necessarily need to be traceable back to a specific real-life subject. In other words, accessing a digital service may not mean that the underlying subject’s real-life representation is known.
Digital authentication is the process of determining the validity of one or more authenticators used to claim a digital identity. Authentication establishes that a subject attempting to access a digital service is in control of the technologies used to authenticate.

3.1.	Existing System
Present NIST guidelines advocated a conventional approach to password security based on policies such as strict complexity rules, regular password resets and restricted password reuse.

3.2	. Proposed System
  NIST’s new standards take a radically different approach. For example, password changes are not required unless there is evidence of a compromise, and strict complexity rules have been replaced by construction flexibility, expanded character types, greater length and the prohibition of “bad” (i.e., insecure) passwords. NIST’s new guidelines have the potential to make password-based authentication less frustrating for users and more effective at guarding access to IT resources, but there are tradeoffs.
The password requirement basics under the updated NIST SP 800-63-3 guidelines are:
Length—8-64 characters are recommended.
Character types—Nonstandard characters, such as emoticons, are allowed when possible.
Construction—Long passphrases are encouraged. They must not match entries in the prohibited password dictionary.
Reset— Required only if the password is compromised or forgotten.
Multifactor— Encouraged in all but the least sensitive applications.

