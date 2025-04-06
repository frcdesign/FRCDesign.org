# 0B: Onshape Setup

## Performance Tuning

!!! Tip
    You can test your current performance at the [OnShape Compatibility Check Page](https://cad.onshape.com/check "Compatibility Check").


The first time you enter Onshape, it will prompt you to set up your account, including the default units and mouse controls used when doing CAD. You can also set a profile picture and a nickname (we recommend keeping this as your real name). Finally, Onshape will run a browser check, to ensure compatibility.


!!! Note
    If the browser check fails, you may want to try a different browser. Currently, chromium browsers like Chrome, Edge, Opera, and Arc are the best supported browsers for Onshape, but Firefox usually works with no issues as well. Safari is not well supported.


### Improving Chrome Performance
If you are using Chrome, an additional setup step may be required.

First, type `chrome://settings/` in your searchbar to navigate to chrome settings. Make sure that "Use graphics acceleration when available" is enabled. Relaunch chrome if you have updated it to enable it.

<center><img src="/img/learning-course/stage0/setup/chrome/graphicsacceleration.webp" style="border:5px solid #ADADAD; border-radius: 2%"></center>

Next, go to `chrome://flags/` and enable these:

<center><img src="/img/learning-course/stage0/setup/chrome/flags.webp" style="border:5px solid #ADADAD; border-radius: 2%"></center>

Please note that performance will depend on your individual computer setup. We suggest trying the following for each available ANGLE graphics backends:
- [Choose an ANGLE graphics backend](chrome://flags/#use-angle "Choose an ANGLE graphics backend")
- Click the Relaunch button
- [Check your performance](https://cad.onshape.com/check "Compatibility Check")

and using whichever is the most performant. Here are some examples all taken from the same machine.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure markdown="span">
      <img src="/img/learning-course/stage0b/performance-examples/default.png" style="width:100%; data-description="The default configuration">
      <figcaption>The default configuration</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure markdown="span">
      <img src="/img/learning-course/stage0b/performance-examples/opengl.png" style="width:100%; data-description="OpenGL performance">
      <figcaption>OpenGL</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure markdown="span">
      <img src="/img/learning-course/stage0b/performance-examples/D3D9.png" style="width:100%; data-description="Direct3D9">
      <figcaption>Direct3D 9</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure markdown="span">
      <img src="/img/learning-course/stage0b/performance-examples/D3D11.png" style="width:100%; data-description="Direct3D11">
      <figcaption>Direct3D 11</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure markdown="span">
      <img src="/img/learning-course/stage0b/performance-examples/D3D11on12.png" style="width:100%; data-description="Direct3don12">
      <figcaption>Direct3D 11 on 12</figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <button class="prev" onclick="plusSlides(-1,0)" style="background-color: #000; color: #fff;">&#10094;</button>
  <button class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</button>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

In the above example, Direct3D 11 narrowly beats out OpenGL, but that won't always be the case.