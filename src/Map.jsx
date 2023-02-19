import React, { useState } from "react";

const Map = () => {
  const [location, setLocation] = useState({ latitude: null, longitude: null });
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
  return (
    // <div className="map-container">
    //   <iframe
    //     title="Google Map"
    //     width="600"
    //     height="450"
    //     frameBorder="0"
    //     style={{ border: 0 }}
    //     src={`https://www.google.com/maps/embed/v1/view?key=YOUR_API_KEY&center=${latitude},${longitude}&zoom=15`}
    //     allowFullScreen
    //   />
    // </div>
    <div>map test</div>
  );
};

export default Map;