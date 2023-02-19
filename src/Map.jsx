import React, { useEffect, useState } from "react";

const Map = () => {
  const [location, setLocation] = useState({ latitude: null, longitude: null });
  useEffect(() => {
    const intervalId = setInterval(() => {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          setLocation({
            latitude: position.coords.latitude,
            longitude: position.coords.longitude,
          });
          console.log(position.coords.latitude, position.coords.longitude);
        },
        (error) => {
          console.log(error);
        }
      );
    }, 10000);
    return () => clearInterval(intervalId);
  }, []);

  const handleSOSClick = () => {
    // handle SOS click event here
    console.log("SOS button clicked!");
  };

  return (
    <div
      style={{ display: "flex", flexDirection: "column", alignItems: "center" }}
    >
      <div className="map-container" style={{ textAlign: "center" }}>
        <iframe
          title="Google Map"
          width="600"
          height="450"
          frameBorder="0"
          style={{ border: 0 }}
          src={`https://www.google.com/maps/embed/v1/place?q=${location.latitude},${location.longitude}&key=AIzaSyAne-wDQnG40i8ukL3Y1-4zVdP88d5SM5o&zoom=18`}
          allowFullScreen
        />
      </div>
      <button
        onClick={handleSOSClick}
        style={{
          backgroundColor: "red",
          color: "white",
          fontSize: "2rem",
          padding: "1rem 2rem",
          marginTop: "1rem",
          border: "none",
          borderRadius: "50%",
          width: "10rem",
          height: "10rem",
        }}
      >
        SOS
      </button>
    </div>
  );
};

export default Map;
