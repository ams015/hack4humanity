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

  //   useEffect(() => {
  //     console.log(location.latitude, location.longitude);
  //   }, [location]);

  return (
    <div className="map-container">
      <iframe
        title="Google Map"
        width="600"
        height="450"
        frameBorder="0"
        style={{ border: 0 }}
        // src={`https://www.google.com/maps/embed/v1/view?key=AIzaSyAne-wDQnG40i8ukL3Y1-4zVdP88d5SM5o&center=${location.latitude},${location.longitude}&zoom=15`}
        src={`https://www.google.com/maps/embed/v1/place?q=${location.latitude},${location.longitude}&key=AIzaSyAne-wDQnG40i8ukL3Y1-4zVdP88d5SM5o&zoom=18`}
        allowFullScreen
      />
    </div>
  );
};

export default Map;
