import {TextField} from '@material-ui/core'


function TextForm({disabled = false, value, label,
onChange}){

    return (
        <TextField
          onChange={onChange}
          disabled={disabled}
          id="standard-multiline-static"
          label={label}
          multiline
          rows={10}
          value={value}
          variant="standard"
          color='success'
        />
    )
    
}

export default TextForm