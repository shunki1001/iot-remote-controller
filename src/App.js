import React, { useEffect, useState } from "react";
import {
  Button,
  Grid,
  Container,
  Typography,
  Backdrop,
  CircularProgress,
  Snackbar,
  CardContent,
  Card,
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
  { label: "TVの電源", endpoint: "/tv/on", category: "primary" },
  { label: "書斎エアコンON", endpoint: "/desk-ac/on", category: "primary" },
  { label: "書斎エアコンOFF", endpoint: "/desk-ac/off", category: "primary" },
  {
    label: "電気ON",
    endpoint: "/light/on",
    category: "error",
  },
  {
    label: "電気OFF",
    endpoint: "/light/off",
    category: "error",
  },
];

const App = () => {
  const [open, setOpen] = useState(false);
  const [bdOpen, setBdOpen] = useState(false);
  const [response, setResponse] = useState("");
  const [thermodata, setThermodata] = useState([]);
  const [fetchTime, setFetchTime] = useState(new Date());

  useEffect(() => {
    // APIを定期的に呼び出す関数
    const fetchData = async () => {
      try {
        const response = await axios.get(host_domain + "/thermo-sensor");
        setThermodata(response.data["status"]);
        setFetchTime(new Date());
      } catch (error) {
        setThermodata([
          {
            place: "living",
            temperature: "error",
            humidity: "error",
          },
          {
            place: "desk",
            temperature: "error",
            humidity: "error",
          },
          {
            place: "bedroom",
            temperature: "error",
            humidity: "error",
          },
        ]);
        setFetchTime(new Date());
      }
    };

    // 初回のデータフェッチ
    fetchData();

    // 一定時間ごとにfetchDataを実行
    const intervalId = setInterval(fetchData, 900000);

    // クリーンアップ関数でインターバルをクリア
    return () => clearInterval(intervalId);
  }, []);

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
        {thermodata.map((item, index) => (
          <Grid item xs={4} sm={4} md={4}>
            <Card sx={{ minwidth: 275 }}>
              <CardContent>
                <Typography
                  sx={{ fontSize: 14 }}
                  color="text.secondary"
                  gutterBottom
                >
                  {item["place"]}
                </Typography>
                <Typography
                  sx={{ fontSize: 14 }}
                  color="text.secondary"
                  gutterBottom
                >
                  <span style={{ fontSize: "32px" }}>
                    {item["temperature"]} ℃ / {item["humidity"]} ％
                  </span>
                </Typography>
                <Typography
                  sx={{ fontSize: 14 }}
                  color="text.secondary"
                  gutterBottom
                >
                  ミスナール指数：
                  <span style={{ fontSize: "32px" }}>
                    {Math.floor(
                      37 -
                        (37 - item["temperature"]) /
                          (0.68 - 0.0014 * item["humidity"] + 1 / 1.76) -
                        0.29 *
                          item["temperature"] *
                          (1 - item["humidity"] / 100)
                    )}
                  </span>
                </Typography>
                <Typography
                  sx={{ fontSize: 12, textAlign: "right" }}
                  color="text.secondary"
                  gutterBottom
                >
                  {fetchTime.toLocaleTimeString()} 時点
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
        {buttons.map((button, index) => (
          <Grid item xs={12} sm={4} md={4} key={index}>
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
