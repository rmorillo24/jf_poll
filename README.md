# jf_poll
Polling JellyFish API to check value changes

# How to use
- Create the environment variables
  - (hardcoded atm) improvement_id The improvement id to track
  - (hardcoded atm) improvement_slug The improvement slug to track
  - bearer Your JellyFish token

- Execute `python jf_poll.py`

# How it works
- Using jellyfish API endpoint, it will loop asking for `status` and checking for changes
- If the new value is `completed` it call the `notification()` 
- This is stateless and not persisted, but notification will not be called if the status is already completed