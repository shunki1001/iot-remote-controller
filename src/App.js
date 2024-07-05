import React, { useState } from "react";
import {
  Button,
  Grid,
  Container,
  Typography,
  Backdrop,
  CircularProgress,
  Snackbar,
} from "@mui/material";
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

const App = () => {
  const [open, setOpen] = useState(false);
  const [bdOpen, setBdOpen] = useState(false);
  const [response, setResponse] = useState("");

  const handleClickOpen = async (endpoint) => {
    setBdOpen(true);
    axios
      .get(host_domain + endpoint)
      .then((response) => {
        console.log(response);
        const data = response.data;
        console.log(data);
        // レスポンスを設定
        setResponse(JSON.stringify(data, null, 2));

        // ダイアログを開く
        setBdOpen(false);
        setOpen(true);
      })
      .catch((error) => {
        console.log(error);
        setResponse("error");
        setBdOpen(false);
        setOpen(true);
      });
  };

  const handleClose = () => {
    setOpen(false);
    setBdOpen(false);
  };
  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Smart Home Remote
      </Typography>
      <Grid container spacing={2}>
        {buttons.map((button, index) => (
          <Grid item xs={12} sm={6} md={6} key={index}>
            <Button
              variant="contained"
              color="primary"
              fullWidth
              onClick={() => handleClickOpen(button.endpoint)}
              sx={{ height: "100px", fontSize: "2em" }}
            >
              {button.label}
            </Button>
          </Grid>
        ))}
      </Grid>
      <Backdrop
        sx={{ color: "#fff", zIndex: (theme) => theme.zIndex.drawer + 1 }}
        open={bdOpen}
        onClick={handleClose}
      >
        <CircularProgress color="inherit" />
      </Backdrop>
      <Snackbar
        open={open}
        autoHideDuration={6000}
        onClose={handleClose}
        message={response}
        severity="success"
      />
    </Container>
  );
};

export default App;
