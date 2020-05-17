<template>
  <q-layout>
    <q-container>
      <div class="row">
        <img class="col-12 cover-photo" src="../assets/coverphoto.jpg" />
        <div class="text-pos-1 text-h2" style="letter-spacing:2px">REFRESHING KOMBUCHA</div>
        <div class="text-pos-2 text-h2" style="letter-spacing:2px">MADE WITH LOVE</div>
        <div class="text-pos-3 text-h2" style="letter-spacing:2px">FOR YOU</div>
      </div>
      <div class="row center text-h4 q-pa-xl">
        <div
          class="q-pa-xl"
          style="letter-spacing:2px"
        >A tasty store created to fundraise for the elite club ultimate frisbee team in Montreal</div>
      </div>
      <div class="row">
        <img class="col-6" src="../assets/ferment-kom.jpg" />
        <div
          class="col-6 center text-h4"
          style="letter-spacing:2px"
        >Help support us to go to Nationals</div>
      </div>
      <div class="row">
        <img class="col-6" src="../assets/strawberry.jpg" />
        <img class="col-6" src="../assets/blueberry.jpg" />
      </div>
    </q-container>
  </q-layout>
</template>

<style scoped>
.cover-photo {
  object-fit: cover;
  opacity: 0.75;
}
.text-pos-1 {
  text-align: center;
  position: absolute;
  top: 10%;
  left: 0;
  transform: translate3d(0, -50%, 0);
  z-index: 7;
  width: 100%;
  max-width: 100%;
}
.text-pos-2 {
  text-align: center;
  position: absolute;
  top: 15%;
  left: 0;
  transform: translate3d(0, -50%, 0);
  z-index: 7;
  width: 100%;
  max-width: 100%;
}
.text-pos-3 {
  text-align: center;
  position: absolute;
  top: 20%;
  left: 0;
  transform: translate3d(0, -50%, 0);
  z-index: 7;
  width: 100%;
  max-width: 100%;
}
.custom-font {
  font: "customfont";
}
.center {
  margin: auto;
  width: 50%;
  text-align: center;
}
</style>