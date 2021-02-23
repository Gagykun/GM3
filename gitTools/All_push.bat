@echo off
cd ..
echo Adding files to commit
git add .
echo.
echo Pushing to "beta" branch
echo.
git push origin beta
echo.
echo Pushing to "stable" branch
echo.
git push origin stable
echo.
echo Pushing to "wip" branch
echo.
git push origin wip