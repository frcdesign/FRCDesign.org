---
hide:
  - navigation
  - toc
---
<center markdown>
# FRCDesign.org Merch Shop
</center>
<html>
<style>

  [data-md-color-scheme="slate"] h1, h2{
    color: white;
  }
  [data-md-color-scheme="default"] h1, h2  {
    color: white;
  }

  h1 {
    background-color: #4CAE4F;
    padding: 0.25rem;
    border-radius: 0.25rem;
    text-align: center;
    width: fit-content;
    padding: 0.5rem;
    color: white;
 }

 h2 {
    margin-top: 0rem !important;
    background-color: #4CAE4F;
    padding: 0.25rem;
    border-radius: 0.25rem;
    text-align: center;
    color: white;
 }

.container {
  display: flex;
  flex-direction: row;
  gap: 2rem;
  margin-top: 2rem;
}

.left-column {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  padding: 1rem;
  height: fit-content;
}


.right-column {
  flex: 2;
}

.slideshow-container {
  position: relative;
  max-width: 500px;
  margin: auto;
  border-radius: 0.5rem;
  overflow: hidden;
  padding: 1rem;
  border: 2px solid #ccc;
}

.mySlides {
  display: none;
}

.mySlides img {
  width: 100%;
  height: auto;
  border-radius: 0.5rem;
}

.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  margin-top: -22px;
  padding: 0.5rem;
  color: white;
  font-weight: bold;
  font-size: 18px;
  border: none;
  background-color: #000;
  border-radius: 3px;
  user-select: none;
}

.next {
  right: 10px;
}

.prev {
  left: 10px;
}

.buy-box {
  margin-top: 0;
  border-radius: 0.5rem;
  padding: 0rem;
  width: fit-content;
  font-weight: bold;
  color: white;
}

.BuyButton-Button {
  color: white !important;
}

</style>

<script async src="https://js.stripe.com/v3/buy-button.js"></script>

<div class="container">
  <div class="left-column">
    <div>
      <h2>FRCDesign.org Sweatshirts</h2>
      <p>Due to popular demand, we now have hoodies for sale! Proceeds will be used to support development, fund CADathons, and enable future merch sales.</p>
      <p>Independent trading IND4000 Heavyweight Pullover Hoodie</p>
      <p>70% Cotton/30% Polyester</p>
      <p>Printed and Shipped by FRCtees</p>
      <p>Hoodie design by David</p>
      <p>$65 USD + $8 Shipping</p>
    </div>

    <div class="buy-box">
      <stripe-buy-button
        buy-button-id="buy_btn_1RqyXORLFNRB375u8T84nq1H"
        publishable-key="pk_live_51Rqy1ERLFNRB375uEBFXymOFWJd0dpFsAecbC7Si6gTtUZIKnf8Av0yc4Ajx17sq4DFlzVL9ao4WCayYWgZ2M56800Hvb2PFAW"
      >
      </stripe-buy-button>
    </div>
  </div>

  <div class="right-column">
    <div class="slideshow-container">
      <div id="slide1" class="mySlides fade">
        <figure>
          <img src="/img/shop/drop1/hoodie-back.webp">
          <figcaption style="text-align:center; color: white;">Hoodie Back</figcaption>
        </figure>
      </div>

      <div class="mySlides fade">
        <figure>
          <img src="/img/shop/drop1/hoodie-front.webp">
          <figcaption style="text-align:center; color: white;">Hoodie Front</figcaption>
        </figure>
      </div>

      <!-- Navigation buttons -->
      <button class="prev" onclick="plusSlides(-1,0)">&#10094;</button>
      <button class="next" onclick="plusSlides(1,0)">&#10095;</button>
    </div>
  </div>
</div>
</html>
