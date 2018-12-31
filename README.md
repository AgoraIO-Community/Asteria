# Asteria

## Intro & Demo
https://www.youtube.com/watch?v=lNmZe53QK3A

## Inspiration
We wanted a simple way for teams to collaborate online as comfortably as they do in person. The application is meant to address some of the biggest challenges when working as a team over a video call.

## What it does
The app allows users to join a video broadcast and collaborate by writing on the screen with just their hands.

The server looks at the video feed from your camera, and using computer vision, it converts your hand gestures into drawings that everyone else in the call can see.

## How we built it
The back-end was writting in node.js and deployed on Heroku. We used openCV for the computer vision. The video call web application was built with the Agora web SDK, Materialize, jQuery, and Bootstrap.
