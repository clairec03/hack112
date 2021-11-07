import {TextField} from '@material-ui/core'


function TextForm({disabled = false, defaultValue}){

    return (
        <TextField
          disabled={disabled}
          id="standard-multiline-static"
          label="Multiline"
          multiline
          rows={10}
          defaultValue={defaultValue}
          variant="standard"
          color='success'
        />
    )
    
}

export default TextForm