import React from "react";
import { Button, Grid, Container, Typography } from "@mui/material";
import axios from "axios";

const host_domain = process.env.REACT_APP_HOST_DOMAIN;

const buttons = [
  { label: "/tv/on", endpoint: "/tv/on" },
  { label: "/living-ac/on", endpoint: "/living-ac/on" },
  { label: "/living-ac/off", endpoint: "/living-ac/off" },
  { label: "/desk-ac/on", endpoint: "/desk-ac/on" },
  { label: "/desk-ac/off", endpoint: "/desk-ac/off" },
  { label: "/living-light/on", endpoint: "/living-light/on" },
  { label: "/living-light/off", endpoint: "/living-light/off" },
  { label: "/living-light/dinner", endpoint: "/living-light/dinner" },
  { label: "/living-light/lunch", endpoint: "/living-light/lunch" },
  { label: "/desk-light/on", endpoint: "/desk-light/on" },
  { label: "/desk-light/off", endpoint: "/desk-light/off" },
  { label: "/desk-light/brighten", endpoint: "/desk-light/brighten" },
  { label: "/desk-light/darken", endpoint: "/desk-light/darken" },
];

const handleButtonClick = (endpoint) => {
  axios
    .get(host_domain + endpoint)
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
