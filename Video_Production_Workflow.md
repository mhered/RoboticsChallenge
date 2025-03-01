# Video production workflow (update 28/2)



1. In Canva: update Slide 1 (thumbnail) add image (speaker's face or other) with transparent background, add thick white border. Export as PDF in FullHD (1920x1080) for Youtube thumbnail, then resize to 640x360 for repo
2. In Canva: update Slide 2 (intro animation) export as MP4 in FullHD
3. Screencast the background using GNOME screen recorder: `CTRL+ALT+SHIFT+R`
4. Assemble intro + screencast in Shotcut and export as `DayNN_bkg.mp4`. No sound, speed up if necessary. Target max. 66"
5. Improvise a voice over, transcribe it with iphone
6. Ask ChatGPT to review transcript with this prompt:

```
I am doing a 28-day robotics challenge with the goal to dive deeper into robotics - especially ROS2 - through a hands-on approach. In order to stay accountable, track progress and connect with the robotics community I am posting daily on twitter 1' videos with progress updates, main highlights and take aways.

With this context in mind, I want you help to prepare the voiceover for today's video.

After the prompt I will be posting a first draft of the voiceover and I want you to use it as a staerting point. Note that there may be mistakes in the draft because it is an automatic transcript of my improvised commentary of the video and I am not a native English speaker. Please review the flow, make it direct, informative, fresh and engaging and summarize it if necessary so it is no more than 1 minute long.

Afterwards, help me as well write a short fresh twitter cover post to go with the video.

Please confirm you are ready to receive the draft and stand by.
```

4. Record in OBS Studio (fullHD): speaker doing voiceover with chroma background and `DayNN_bkg.mp4` playing as background. Practice and fine tune script. Careful with eye contact when reading the script
6. Cut, speed up if necessary (with pitch compensation) strictly down to 1' in Shotcut and save as `DayNN.mp4` 
7. Add background music?
12. Export to mp4 in shotcut (should be FullHD by default same as intro and screencast)