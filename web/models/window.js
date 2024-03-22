document.addEventListener('keydown', function(event) {
  if (event.ctrlKey || event.altKey || event.metaKey) {
    event.preventDefault();
  }
});

document.addEventListener('keydown', function(event) {
  if (event.keyCode >= 112 && event.keyCode <= 123) {
    event.preventDefault();
  }
});

document.addEventListener('contextmenu', event => event.preventDefault());
