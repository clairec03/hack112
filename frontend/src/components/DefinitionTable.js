import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

const bull = (
  <Box
    component="span"
    sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
  >
    •
  </Box>
);

export default function DefintionTable({word, def, ex, pos}) {
  return (
    <Card sx={{ minWidth: 275 }}>
      <CardContent>
        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
          Slang Word
        </Typography>
        <Typography variant="h5" component="div">
          {`${word.substring(0,1).toUpperCase() + word.substring(1)}`}
        </Typography>
        <Typography sx={{ mb: 1.5 }} color="text.secondary">
          {pos}
        </Typography>
        <Typography variant="body2">
          {def}
          <br />
          {ex}
        </Typography>
      </CardContent>
      {/* <CardActions>
        <Button size="small">See on Website</Button>
      </CardActions> */}
    </Card>
  );
}