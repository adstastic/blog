---
title: "Homomorphically Encrypting CRDTs"
date: 2025-06-21
slug: "homomorphically-encrypting-crdts"
tags:
  - quote
ref: https://jakelazaroff.com/words/homomorphically-encrypted-crdts/?utm_source=tldrnewsletter
---

Quoting [jakelazaroff.com](https://jakelazaroff.com/words/homomorphically-encrypted-crdts/?utm_source=tldrnewsletter):

> **if you add or multiply two homomorphically encrypted values, then decrypt them, *you get the respective sum or product of the original plaintext values***.

> •   **Partially homomorphic encryption** allows only one of the two operations: *either* addition *or* multiplication, but not both.
•   **Somewhat homomorphic encryption** and **leveled homomorphic encryption** allow both operations, but limit the amount of times they can be used.
•   **Fully homomorphic encryption** allows an unlimited amount of both operations.

> All other logical operations can be created by combining only XOR and AND, which means that adding and multiplying the encrypted data is sufficient to simulate arbitrary Boolean logic.
