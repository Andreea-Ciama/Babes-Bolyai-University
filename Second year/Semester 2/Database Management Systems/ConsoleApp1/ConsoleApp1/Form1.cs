using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace Lab1
{
    public partial class Form1 : Form
    {
        SqlConnection conn;
        SqlDataAdapter daParent;
        SqlDataAdapter daChild;
        DataSet dset;


        BindingSource bsParent;
        BindingSource bsChild;

        SqlCommandBuilder cmdBuilder;

        string queryParent;
        string queryChild;

        public Form1()
        {
            InitializeComponent();
            FillData();
            //this.dataGridView2.CellValidating += new DataGridViewCellValidatingEventHandler(dataGridView2_CellValidating);

        }

        private void dataGridView2_CellValidating(object sender, DataGridViewCellValidatingEventArgs e)
        {
            if (e.ColumnIndex == 0) // ID column
            {
                int id;
                if (!int.TryParse(e.FormattedValue.ToString(), out id))
                {
                    e.Cancel = true;
                    MessageBox.Show("The ID must be a valid integer.");
                }
            }
        }

        void FillData()
        {
            //sqlConnection
            conn = new SqlConnection(getConnectionString());

            queryParent = "SELECT * FROM Producer";
            queryChild = "SELECT * FROM Model";

            //SqlDataAdapter, DataSet
            daParent = new SqlDataAdapter(queryParent, conn);
            daChild = new SqlDataAdapter(queryChild, conn);
            dset = new DataSet();
            daParent.Fill(dset, "Producer");
            daChild.Fill(dset, "Model");

            //fill in insert, update, delete command
            cmdBuilder = new SqlCommandBuilder(daChild);

            //adding the paret-child rel to the dataset
            dset.Relations.Add("ParentChild",
                dset.Tables["Producer"].Columns["ProducerID"],//primary key din tabelul nostru
                dset.Tables["Model"].Columns["ProducerId"]); //foregin key din tabelul nostru



            //Method2: using data binding
            bsParent = new BindingSource();
            bsParent.DataSource = dset.Tables["Producer"];
            bsChild = new BindingSource(bsParent, "ParentChild"); //chaining mechanism

            this.dataGridView1.DataSource = bsParent;
            this.dataGridView2.DataSource = bsChild;

            cmdBuilder.GetUpdateCommand();

        }

        string getConnectionString()
        {
            return "Data Source=LAPTOP-72Q19S0C\\MSSQLSERVER01; Initial Catalog=practic2;" + "Integrated Security=true;";
        }

        private void updateButton_Click(object sender, EventArgs e)
        {

            try
            {
                daChild.Update(dset, "Model");
                MessageBox.Show("Data uploaded successfully!");

            }

            catch (SqlException ex)
            {
                if (ex.Number == 2627) // validates the primary key; checks if it appears already or not
                {
                    MessageBox.Show("A Producer with the same ID already exists");
                }
                else if (ex.Message.Contains("Cannot insert the value NULL into column"))
                {
                    MessageBox.Show("The ID field cannot be epmty. Please fill in the required field.");
                }
                else
                {
                    MessageBox.Show("An error occured while updating the data: " + ex.Message);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("An error occured while updating the data: " + ex.Message);
            }
        }

        private void insertButton_Click(object sender, EventArgs e)
        {
        }

        private void deleteButton_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }
}
