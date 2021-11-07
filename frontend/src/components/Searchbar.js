import {TextField, makeStyles, Button} from '@material-ui/core'

const useStyles = makeStyles(theme => ({
    inline: {
        display:'flex',
       flexDirection: 'row',
        justifyContent:'center',
        // justifyContent: 'center'
        margin: 20
        
    }
}))


function Searchbar({onChange, onSearch}){
   
    const classes = useStyles()
    return (
        <div className={classes.inline}>
        <TextField
        onChange={onChange}
          id="outlined-search"
          label={'Search'}
          value={'hi'}
          variant="standard"
          color='success'
        />
        <Button onClick={onSearch}>Search</Button>
        </div>
    )
    
}

export default Searchbar