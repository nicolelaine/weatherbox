function wordInput(feeling) {
  if (words.includes(feeling)) {
    console.log(`Wow, you are indeed ${feeling}`);
  } else {
    console.log(`${feeling} is not a recognized feeling. Try again!`);
  }
}

wordInput("bonkers");
