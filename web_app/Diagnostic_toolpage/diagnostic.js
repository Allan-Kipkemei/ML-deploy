function upload() {
    const fileUploadInput = document.querySelector(".file-uploader");
    const diseaseStatus = document.getElementById("disease-status");
    const recommendationText = document.getElementById("recommendation-text");

    if (!fileUploadInput.value) {
        return;
    }

    const image = fileUploadInput.files[0];

    if (!image.type.includes("image")) {
        return alert("Only images are allowed!");
    }

    if (image.size > 10_000_000) {
        return alert("Maximum upload size is 10MB!");
    }

    const fileReader = new FileReader();
    fileReader.readAsDataURL(image);

    fileReader.onload = (fileReaderEvent) => {
        const profilePicture = document.querySelector(".profile-picture");
        profilePicture.style.backgroundImage = `url(${fileReaderEvent.target.result})`;

        const formData = new FormData();
        formData.append('image', image);

        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                diseaseStatus.textContent = "Error: " + data.error;
                recommendationText.textContent = "";
            } else {
                diseaseStatus.textContent = "Disease Detected: " + data.disease;

                recommendationText.innerHTML = `
                    <strong>Description:</strong> ${data.recommendation.Description}<br>
                    <strong>Diagnosis:</strong> ${data.recommendation.Diagnosis}<br>
                    <strong>Recommended Action:</strong> ${data.recommendation.Recommended_Action}<br>
                    <strong>Treatment:</strong> ${data.recommendation.Treatment}<br>
                    <strong>Treatment Timing:</strong> ${data.recommendation.Treatment_Timing}<br>
                    <strong>Prevention:</strong> ${data.recommendation.Prevention}<br>
                    <strong>Monitoring:</strong> ${data.recommendation.Monitoring}<br>
                    <strong>Cultural Practices:</strong> ${data.recommendation.Cultural_Practices}<br>
                    <strong>Physical Controls:</strong> ${data.recommendation.Physical_Controls}<br>
                    <strong>Biological Controls:</strong> ${data.recommendation.Biological_Controls}
                `;
            }
        })
        .catch(error => {
            console.error("Error:", error);
            diseaseStatus.textContent = "Error detecting disease.";
            recommendationText.textContent = "";
        });
    };
}
