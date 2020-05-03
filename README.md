# Churp in Cloudlab

This is a collection of scripts which download and compile churp (and its dps), and then execute a simple test.

To modify the tests, modify `runBulletin.sh` and `runNode.sh`. 

You can also modify the Churp code if needed, and then change the repository in `installChurp.sh`. 

To change the count of simulated nodes, please adjust `profile.py`.

Please take care when editing any of the other files, the paths/permissions/environment are a bit fragile.