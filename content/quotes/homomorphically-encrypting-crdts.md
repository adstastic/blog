---
title: "Homomorphically Encrypting CRDTs"
date: 2025-06-22
slug: "homomorphically-encrypting-crdts"
tags:
  - quote
ref: https://jakelazaroff.com/words/homomorphically-encrypted-crdts/?utm_source=tldrnewsletter
---

Quoting [jakelazaroff.com](https://jakelazaroff.com/words/homomorphically-encrypted-crdts/?utm_source=tldrnewsletter):

> A last write wins register holds a single value and two additional bits of metadata: a “clock” that gets incremented by one whenever the value is set, and an ID indicating the peer who last wrote to it. Like all CRDTs, it also has a merge function that describes how it should be combined with another of the same type.

> The last write wins register merge algorithm works like this:

•   If the received clock is less than the local clock, the register doesn’t change its state.
•   If the received clock is greater than the local clock, the register overwrites its local value with the received value. It also stores the received clock and peer ID.
•   Ties are broken by comparing the local peer ID to the peer ID in the received state.

> we can’t retrieve any information by operating on the encrypted data — *including information about the results of intermediate steps*.

> our merge function must *eagerly* evaluate all branches in our code. It also means that all loops must run for a statically-known number of iterations. More generally, **our code must always execute as though operating on the worst case input**, because altering behavior based on the input would leak information about it.

> ciphertexts of dozens or hundreds of *kilobytes* require keys on the order of *gigabytes*.

> The unencrypted one averaged a merge time of 0.52 nanoseconds.

The encrypted one? *1.06 seconds*. That’s not a typo: the homomorphically encrypted merge is *two billion times slower*.[5](https://jakelazaroff.com/words/homomorphically-encrypted-crdts/#user-content-fn-gpu)

> A homomorphically encrypted map CRDT couldn’t do that. Since it must assume a worst-case input, it must store the keys *densely*: limiting the size to a fixed number of keys and reserving all the space up front. Merging two identical maps would be exactly as computationally intensive as merging two maps in which *every* key was updated.[7](https://jakelazaroff.com/words/homomorphically-encrypted-crdts/#user-content-fn-op)

> The requirement that homomorphically encrypted code performs as though operating on the worst-case input dramatically increases both the space and time required to update.
