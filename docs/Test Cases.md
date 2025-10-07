# Test Cases for Testing GooseTrack API

## 1. User Authentication (UserAuth)
* T01: Create a new user with a valid email, password, and name.
* T02: Create a new user with an invalid email.
* T03: Create a new user with an invalid password.
* T04: Create a new user with an already existing email.
* T05: Create a new user without a password.
* T06: Create a new user without a name.
* T07: Create a new user without an email.
* T08: Log in with valid email and password.
* T09: Log in with a valid email that is not registered.
* T10: Log in with an invalid email.
* T11: Log in with an invalid password.
* T12: Log in without a password.
* T13: Log out from the account.
* T14: Log out with an invalid token.
* T15: Refresh tokens.
* T16: Get current user info.
* T17: Get current user info with an invalid token.
* T18: Update user info with valid data.
* T19: Update user info with an empty name.
* T20: Update user info with an invalid email.
* T21: Update user info with an invalid token.

## 2. Task Management (Task)
* T22: Create a task with valid data.
* T23: Get the list of tasks.
* T24: Create a task with an empty title.
* T25: Create a task with an invalid priority.
* T26: Create a task with an invalid category.
* T27: Create a task without start/end fields.
* T28: Create a task with an invalid time.
* T29: Create a task with an invalid date format.
* T30: Update an existing task with valid data.
* T31: Update an existing task with an empty title.
* T32: Update an existing task with an invalid time.
* T33: Update an existing task with an invalid priority.
* T34: Update an existing task with an invalid category.
* T35: Delete one of the existing tasks.
* T36: Delete a task that has already been deleted.
* T37: Attempt to delete another user's task.
* T38: Attempt to update a task that belongs to another user.
