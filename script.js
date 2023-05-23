function review(gamelink) {
  console.log(gamelink);
  axios.post("https://8382ok6h0f.execute-api.us-east-2.amazonaws.com/test/review",
        {link: gamelink}
      ).then(function (response) {
        console.log(response);
        window.location.href = gamelink;
      }).catch(function (error) {
        console.log(error);
      });
}
