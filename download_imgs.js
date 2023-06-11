const images = document.querySelectorAll('img:not([draggable="false"])[style="width: 100%;"][src^="blob"]');

images.forEach((image, index) => {
  const imageURL = image.src;
  const link = document.createElement('a');
  link.href = imageURL;
  link.download = `automatic_whatsap_image_scraper_${index + 1}.jpg`;
  link.click();
});