import React, { Component } from "react";
import DataTable from "react-data-table-component"
import { Button } from "@mui/material/";
import { Link } from "react-router-dom";

export default class PkmnInverted extends Component {
  constructor(props) {
    super(props);
    this.state = {
      pokemons: [],
      columns : [
          {
            name: "ID",
            selector: (row) => row.pkm_id,
          },
          {
            name: "Nombre",
            selector: (row) => row.inverted_name,
          },
          {
            name: "Tipo",
            selector: (row) => row.type,
          },
          {
            name: "Peso",
            selector: (row) => row.weight,
          },
          {
            name: "Altura",
            selector: (row) => row.height,
          },
        ]
      
    };
    this.getPkmnDetials();
  }

  // Se obtienen los pokemones que cumplen con la 
  // condicion desde la api
  getPkmnDetials(){
    fetch("/api/inverted_name")
    .then((response) => response.json())
    .then((data) => {
      this.setState({
        pokemons : data
      });
    });
    
  }

  render() {
    return( 

      <div style={{ margin: "20px" }}>     
      {/* Se muestran los pokemon en una tabla */}
      <DataTable
        title="Nombres de los Pokemon invertidos"
        columns={this.state.columns}
        data={this.state.pokemons}
        dense
        direction="auto"
        fixedHeader
        fixedHeaderScrollHeight="500px"
        highlightOnHover
        pagination
        responsive
        striped
        subHeaderAlign="right"
        subHeaderWrap
      />
      {/* Menu de navegación */}
      <Button color="secondary" variant="contained" to="/" component={Link}> 
          Pagina Principal
        </Button>

      <Button color="primary" variant="contained" to="/grass" component={Link}> 
          Grass
        </Button>

        <Button color="primary" variant="contained" to="/weight" component={Link}> 
            30 {'<'} Peso {'<'} 80
        </Button>
      
      <Button color="primary" variant="contained" to="/flying_10" component={Link}> 
        Flying/Altura {'>'} 10
        </Button>
    </div>
    
    );  
  }
}