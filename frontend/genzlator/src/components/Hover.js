// Source: https://mui.com/components/popover/
import * as React from 'react';
import Popover from '@mui/material/Popover';
import Typography from '@mui/material/Typography';

export default function MouseOverPopover() {
    const [anchorEl, setAnchorEl] = React.useState(null);
  
    const handlePopoverOpen = (event) => {
      setAnchorEl(event.currentTarget);
    };
  
    const handlePopoverClose = () => {
      setAnchorEl(null);
    };
  
    const open = Boolean(anchorEl);

function HoverableText () {
      return( <div>
        <Typography
        aria-owns={open ? 'mouse-over-popover' : undefined}
        aria-haspopup="true"
        onMouseEnter={handlePopoverOpen}
        onMouseLeave={handlePopoverClose}>
            We want the word YEET to have a hoverable effect.
        </Typography>
    <Popover
      id="mouse-over-popover"
      sx={{
        pointerEvents: 'none',
      }}
      open={open}
      anchorEl={anchorEl}
      anchorOrigin={{
        vertical: 'bottom',
        horizontal: 'left',
      }}
      transformOrigin={{
        vertical: 'top',
        horizontal: 'left',
      }}
      onClose={handlePopoverClose}
      disableRestoreFocus
    >
      <Typography sx={{ p: 1 }}>I use Popover.</Typography>
    </Popover>
  </div>)};
}

//pass in typography
//receive typography WITH hoverable text component


//const OutputThing = <Typography> Output </Typography> 
//<HoverableText input={OutputThing} />

//--> return <Typography>