<template>
  <q-layout>
    <q-toolbar class="q-pa-md">
      <q-btn icon="keyboard_arrow_left" flat label="Back to Home" to="/home" />
    </q-toolbar>
    <q-card class="center q-pa-xl">
      <q-card-section class="text-h5 text-bold"
        >Thank you for supporting us!</q-card-section
      >
      <p class="q-pt-xl text-body1">
        Your order is being prepared... Please look out for a confirmation email
        in your inbox with the email you registered with!
      </p>
      <p class="q-pt-md text-body1">
        Love, Venus
      </p>
    </q-card>
  </q-layout>
</template>

<style scoped>
.center {
  margin: auto;
  width: 50%;
  text-align: center;
}
</style>
