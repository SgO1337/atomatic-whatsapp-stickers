// Select all <img> elements with style="width: 100%;" and src attribute starting with "blob"
const images = document.querySelectorAll('img[style="width: 100%;"][src^="blob"]');

// Iterate over the selected images
images.forEach((image, index) => {
  // Extract the image URL
  const imageURL = image.src;

  // Create a link element
  const link = document.createElement('a');
  link.href = imageURL;
  link.download = `automatic_whatsap_image_scraper_${index + 1}.jpg`; // Set a unique name for each downloaded image

  // Simulate a click event on the link to trigger the download
  link.click();
});