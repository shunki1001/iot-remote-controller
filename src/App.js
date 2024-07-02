import React from "react";
import { Button, Grid, Container, Typography } from "@mui/material";
import axios from "axios";

const buttons = [
  { label: "Turn On Light", endpoint: "/api/light/on" },
  { label: "Turn Off Light", endpoint: "/api/light/off" },
  { label: "Lock Door", endpoint: "/api/door/lock" },
  { label: "Unlock Door", endpoint: "/api/door/unlock" },
];

const handleButtonClick = (endpoint) => {
  axios
    .post(endpoint)
    .then((response) => {
      console.log("Success:", response.data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

const App = () => {
  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Smart Home Remote
      </Typography>
      <Grid container spacing={2}>
        {buttons.map((button, index) => (
          <Grid item xs={12} sm={6} md={4} key={index}>
            <Button
              variant="contained"
              color="primary"
              fullWidth
              onClick={() => handleButtonClick(button.endpoint)}
            >
              {button.label}
            </Button>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
};

export default App;
