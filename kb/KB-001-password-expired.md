# KB-001 Password expired: how to change it

**Symptom:** at login you see `Your password has expired. You must change your password now.`

**Steps**
1. Enter your current password.
2. Enter a new password twice: at least 12 characters, not used before.
3. Log in again with the new password.

**Still blocked?** Create a ticket with your username and the exact message. The engineer checks `sudo chage -l <user>` and `passwd -S <user>`.
