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
  {
    label: "リビングエアコンON",
    endpoint: "/living-ac/on",
    category: "error",
  },
  {
    label: "リビングエアコンOFF",
    endpoint: "/living-ac/off",
    category: "error",
  },
  { label: "書斎エアコンON", endpoint: "/desk-ac/on", category: "primary" },
  { label: "書斎エアコンOFF", endpoint: "/desk-ac/off", category: "primary" },
  {
    label: "リビング電気ON",
    endpoint: "/living-light/on",
    category: "error",
  },
  {
    label: "リビング電気OFF",
    endpoint: "/living-light/off",
    category: "error",
  },
  {
    label: "リビング電気明るく",
    endpoint: "/living-light/dinner",
    category: "error",
  },
  {
    label: "リビング電気暗く",
    endpoint: "/living-light/lunch",
    category: "error",
  },
  { label: "書斎電気ON", endpoint: "/desk-light/on", category: "primary" },
  { label: "書斎電気OFF", endpoint: "/desk-light/off", category: "primary" },
  {
    label: "書斎電気明るく",
    endpoint: "/desk-light/brighten",
    category: "primary",
  },
  {
    label: "書斎電気暗く",
    endpoint: "/desk-light/darken",
    category: "primary",
  },
  { label: "TVの電源", endpoint: "/tv/on", category: "primary" },
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
              color={button.category}
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
